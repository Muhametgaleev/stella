from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Set

from stella_types import (
    StellaType, TypeBool, TypeNat, TypeUnit,
    TypeFun, TypeTuple, TypeRecord, TypeSum, TypeList, TypeVariant,
    BOOL, NAT, UNIT
)
from errors import (
    TypeCheckError,
    ERROR_MISSING_MAIN, ERROR_UNDEFINED_VARIABLE, ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
    ERROR_NOT_A_FUNCTION, ERROR_NOT_A_TUPLE, ERROR_NOT_A_RECORD, ERROR_NOT_A_LIST,
    ERROR_UNEXPECTED_LAMBDA, ERROR_UNEXPECTED_TYPE_FOR_PARAMETER,
    ERROR_UNEXPECTED_TUPLE, ERROR_UNEXPECTED_RECORD, ERROR_UNEXPECTED_VARIANT,
    ERROR_UNEXPECTED_LIST, ERROR_UNEXPECTED_INJECTION, ERROR_MISSING_RECORD_FIELDS,
    ERROR_UNEXPECTED_RECORD_FIELDS, ERROR_UNEXPECTED_FIELD_ACCESS,
    ERROR_UNEXPECTED_VARIANT_LABEL, ERROR_TUPLE_INDEX_OUT_OF_BOUNDS,
    ERROR_UNEXPECTED_TUPLE_LENGTH, ERROR_AMBIGUOUS_SUM_TYPE, ERROR_AMBIGUOUS_VARIANT_TYPE,
    ERROR_AMBIGUOUS_LIST, ERROR_ILLEGAL_EMPTY_MATCHING, ERROR_NONEXHAUSTIVE_MATCH_PATTERNS,
    ERROR_UNEXPECTED_PATTERN_FOR_TYPE, ERROR_DUPLICATE_RECORD_FIELDS,
    ERROR_DUPLICATE_RECORD_TYPE_FIELDS, ERROR_DUPLICATE_VARIANT_TYPE_FIELDS,
    ERROR_DUPLICATE_FUNCTION_DECLARATION
)
from context import TypeEnv
from pretty import pretty_type, pretty_expr

class TypeChecker:
    def __init__(self, extensions: set):
        self.extensions = extensions
        self.functions: Dict[str, TypeFun] = {}
        self.current_fn: Optional[str] = None

        self.has_pairs = '#pairs' in extensions
        self.has_tuples = '#tuples' in extensions
        self.has_records = '#records' in extensions
        self.has_let = '#let-bindings' in extensions
        self.has_sum_types = '#sum-types' in extensions
        self.has_lists = '#lists' in extensions
        self.has_variants = '#variants' in extensions
        self.has_fixpoint = '#fixpoint-combinator' in extensions
        self.has_type_ascriptions = '#type-ascriptions' in extensions

        self.type_aliases: Dict[str, StellaType] = {}

    def parse_type(self, ctx) -> StellaType:
        name = ctx.__class__.__name__

        if name == 'TypeBoolContext':
            return BOOL
        elif name == 'TypeNatContext':
            return NAT
        elif name == 'TypeUnitContext':
            return UNIT
        elif name == 'TypeFunContext':
            param_types = [self.parse_type(p) for p in ctx.paramTypes]
            ret_type = self.parse_type(ctx.returnType)
            return TypeFun(param_types, ret_type)
        elif name == 'TypeTupleContext':
            types = [self.parse_type(t) for t in ctx.types]
            return TypeTuple(types)
        elif name == 'TypeRecordContext':
            seen_labels = set()
            fields = []
            for ft in ctx.fieldTypes:
                label = ft.label.text
                if label in seen_labels:
                    raise TypeCheckError(
                        ERROR_DUPLICATE_RECORD_TYPE_FIELDS,
                        f"Duplicate field '{label}' in record type"
                    )
                seen_labels.add(label)
                fields.append((label, self.parse_type(ft.type_)))
            return TypeRecord(fields)
        elif name == 'TypeSumContext':
            return TypeSum(
                self.parse_type(ctx.left),
                self.parse_type(ctx.right)
            )
        elif name == 'TypeListContext':
            return TypeList(self.parse_type(ctx.type_))
        elif name == 'TypeVariantContext':
            seen_labels = set()
            fields = []
            for ft in ctx.fieldTypes:
                label = ft.label.text
                if label in seen_labels:
                    raise TypeCheckError(
                        ERROR_DUPLICATE_VARIANT_TYPE_FIELDS,
                        f"Duplicate label '{label}' in variant type"
                    )
                seen_labels.add(label)
                if ft.type_ is not None:
                    fields.append((label, self.parse_type(ft.type_)))
                else:
                    fields.append((label, None))
            return TypeVariant(fields)
        elif name == 'TypeVarContext':
            var_name = ctx.name.text
            if var_name in self.type_aliases:
                return self.type_aliases[var_name]
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Undefined type: {var_name}"
            )
        elif name == 'TypeParensContext':
            return self.parse_type(ctx.type_)
        else:
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Unknown type context: {name}"
            )

    def _expect_type(self, expr, actual: StellaType, expected: StellaType):
        if actual != expected:
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Expected type {pretty_type(expected)}, but got {pretty_type(actual)}"
                + (f" for expression {pretty_expr(expr)}" if expr is not None else "")
            )

    def check_program(self, program_ctx):
        for decl in program_ctx.decls:
            if decl.__class__.__name__ == 'DeclTypeAliasContext':
                name = decl.name.text
                self.type_aliases[name] = self.parse_type(decl.atype)

        seen_names = set()
        for decl in program_ctx.decls:
            cname = decl.__class__.__name__
            if cname == 'DeclFunContext':
                fn_name = decl.name.text
                if fn_name in seen_names:
                    raise TypeCheckError(
                        ERROR_DUPLICATE_FUNCTION_DECLARATION,
                        f"Duplicate function declaration: {fn_name}"
                    )
                seen_names.add(fn_name)

        global_env = TypeEnv()
        for decl in program_ctx.decls:
            cname = decl.__class__.__name__
            if cname == 'DeclFunContext':
                fn_type = self._get_fun_type(decl)
                self.functions[decl.name.text] = fn_type
                global_env = global_env.extend(decl.name.text, fn_type)

        if 'main' not in self.functions:
            raise TypeCheckError(
                ERROR_MISSING_MAIN,
                "Missing 'main' function"
            )

        for decl in program_ctx.decls:
            cname = decl.__class__.__name__
            if cname == 'DeclFunContext':
                self._check_fun_decl(decl, global_env)

    def _get_fun_type(self, decl) -> TypeFun:
        param_types = []
        for pd in decl.paramDecls:
            param_types.append(self.parse_type(pd.paramType))

        if decl.returnType is not None:
            ret_type = self.parse_type(decl.returnType)
        else:
            ret_type = UNIT

        return TypeFun(param_types, ret_type)

    def _check_fun_decl(self, decl, global_env: TypeEnv):
        self.current_fn = decl.name.text
        fn_type = self.functions[decl.name.text]

        env = global_env
        for pd, param_type in zip(decl.paramDecls, fn_type.param_types):
            env = env.extend(pd.name.text, param_type)

        local_functions = {}
        for local_decl in decl.localDecls:
            local_cname = local_decl.__class__.__name__
            if local_cname == 'DeclFunContext':
                local_fn_type = self._get_fun_type(local_decl)
                local_functions[local_decl.name.text] = local_fn_type
                env = env.extend(local_decl.name.text, local_fn_type)

        for local_decl in decl.localDecls:
            local_cname = local_decl.__class__.__name__
            if local_cname == 'DeclFunContext':
                old_fn = self.functions.get(local_decl.name.text)
                self.functions[local_decl.name.text] = local_functions[local_decl.name.text]
                self._check_fun_decl(local_decl, env)
                if old_fn is None:
                    del self.functions[local_decl.name.text]
                else:
                    self.functions[local_decl.name.text] = old_fn

        ret_type = fn_type.return_type
        actual = self.infer_with_expected(decl.returnExpr, env, ret_type)
        self._expect_type(decl.returnExpr, actual, ret_type)

    def infer_with_expected(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        return self._infer(expr, env, expected)

    def infer(self, expr, env: TypeEnv) -> StellaType:
        return self._infer(expr, env, None)

    def check(self, expr, expected: StellaType, env: TypeEnv):
        actual = self._infer(expr, env, expected)
        self._expect_type(expr, actual, expected)

    def _infer(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        name = expr.__class__.__name__

        if name == 'ParenthesisedExprContext':
            return self._infer(expr.expr_, env, expected)

        if name == 'TerminatingSemicolonContext':
            return self._infer(expr.expr_, env, expected)

        if name == 'ConstTrueContext':
            return BOOL
        if name == 'ConstFalseContext':
            return BOOL
        if name == 'ConstUnitContext':
            return UNIT
        if name == 'ConstIntContext':
            return NAT

        if name == 'VarContext':
            var_name = expr.name.text
            t = env.lookup(var_name)
            if t is None:
                raise TypeCheckError(
                    ERROR_UNDEFINED_VARIABLE,
                    f"Undefined variable: {var_name}"
                )
            return t

        if name == 'SuccContext':
            self.check(expr.n, NAT, env)
            return NAT

        if name == 'PredContext':
            self.check(expr.n, NAT, env)
            return NAT

        if name == 'IsZeroContext':
            self.check(expr.n, NAT, env)
            return BOOL

        if name == 'NatRecContext':
            self.check(expr.n, NAT, env)
            if expected is not None:
                z_type = expected
            else:
                z_type = self.infer(expr.initial, env)
            self.check(expr.initial, z_type, env)
            step_type = TypeFun([NAT], TypeFun([z_type], z_type))
            self.check(expr.step, step_type, env)
            return z_type

        if name == 'IfContext':
            self.check(expr.condition, BOOL, env)
            if expected is not None:
                self.check(expr.thenExpr, expected, env)
                self.check(expr.elseExpr, expected, env)
                return expected
            else:
                then_type = self.infer(expr.thenExpr, env)
                self.check(expr.elseExpr, then_type, env)
                return then_type

        if name == 'AbstractionContext':
            return self._infer_abstraction(expr, env, expected)

        if name == 'ApplicationContext':
            return self._infer_application(expr, env, expected)

        if name == 'LetContext':
            return self._infer_let(expr, env, expected)

        if name == 'TypeAscContext':
            asc_type = self.parse_type(expr.type_)
            actual = self._infer(expr.expr_, env, asc_type)
            self._expect_type(expr.expr_, actual, asc_type)
            return asc_type

        if name == 'TupleContext':
            return self._infer_tuple(expr, env, expected)

        if name == 'DotTupleContext':
            return self._infer_dot_tuple(expr, env)

        if name == 'RecordContext':
            return self._infer_record(expr, env, expected)

        if name == 'DotRecordContext':
            return self._infer_dot_record(expr, env)

        if name == 'InlContext':
            return self._infer_inl(expr, env, expected)

        if name == 'InrContext':
            return self._infer_inr(expr, env, expected)

        if name == 'MatchContext':
            return self._infer_match(expr, env, expected)

        if name == 'ListContext':
            return self._infer_list(expr, env, expected)

        if name == 'ConsListContext':
            return self._infer_cons(expr, env, expected)

        if name == 'HeadContext':
            return self._infer_head(expr, env)

        if name == 'TailContext':
            return self._infer_tail(expr, env)

        if name == 'IsEmptyContext':
            list_type = self._infer(expr.list_, env, None)
            if not isinstance(list_type, TypeList):
                raise TypeCheckError(
                    ERROR_NOT_A_LIST,
                    f"Expected a list type, but got {pretty_type(list_type)}"
                )
            return BOOL

        if name == 'VariantContext':
            return self._infer_variant(expr, env, expected)

        if name == 'FixContext':
            return self._infer_fix(expr, env, expected)

        if name in ('AddContext', 'SubtractContext', 'MultiplyContext', 'DivideContext'):
            self.check(expr.left, NAT, env)
            self.check(expr.right, NAT, env)
            return NAT

        if name in ('LessThanContext', 'LessThanOrEqualContext', 'GreaterThanContext',
                    'GreaterThanOrEqualContext', 'EqualContext', 'NotEqualContext'):
            self.check(expr.left, NAT, env)
            self.check(expr.right, NAT, env)
            return BOOL

        if name == 'LogicNotContext':
            self.check(expr.expr_, BOOL, env)
            return BOOL

        if name == 'LogicAndContext':
            self.check(expr.left, BOOL, env)
            self.check(expr.right, BOOL, env)
            return BOOL

        if name == 'LogicOrContext':
            self.check(expr.left, BOOL, env)
            self.check(expr.right, BOOL, env)
            return BOOL

        raise TypeCheckError(
            ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
            f"Unsupported expression type: {name}"
        )

    def _infer_abstraction(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        params = list(expr.paramDecls)

        if expected is not None and isinstance(expected, TypeFun):
            if len(params) == len(expected.param_types):
                param_types = expected.param_types
                annotated_params = []
                for pd, exp_pt in zip(params, param_types):
                    ann_type = self.parse_type(pd.paramType)
                    self._expect_type(pd, ann_type, exp_pt)
                    annotated_params.append(ann_type)

                new_env = env
                for pd, pt in zip(params, annotated_params):
                    new_env = new_env.extend(pd.name.text, pt)

                body_expected = expected.return_type
                body_type = self._infer(expr.returnExpr, new_env, body_expected)
                self._expect_type(expr.returnExpr, body_type, body_expected)
                return TypeFun(annotated_params, body_type)

        param_types = []
        new_env = env
        for pd in params:
            pt = self.parse_type(pd.paramType)
            param_types.append(pt)
            new_env = new_env.extend(pd.name.text, pt)

        if expected is not None and isinstance(expected, TypeFun):
            body_expected = expected.return_type
        else:
            body_expected = None

        body_type = self._infer(expr.returnExpr, new_env, body_expected)
        if body_expected is not None:
            self._expect_type(expr.returnExpr, body_type, body_expected)

        return TypeFun(param_types, body_type)

    def _infer_application(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        fun_type = self._infer(expr.fun, env, None)

        if not isinstance(fun_type, TypeFun):
            raise TypeCheckError(
                ERROR_NOT_A_FUNCTION,
                f"Expected a function type, but got {pretty_type(fun_type)}"
                + (f" for expression {pretty_expr(expr.fun)}" if expr.fun is not None else "")
            )

        args = list(expr.args)
        if len(args) != len(fun_type.param_types):
            raise TypeCheckError(
                ERROR_NOT_A_FUNCTION,
                f"Function expects {len(fun_type.param_types)} arguments but got {len(args)}"
            )

        for arg, param_type in zip(args, fun_type.param_types):
            actual = self._infer(arg, env, param_type)
            self._expect_type(arg, actual, param_type)

        return fun_type.return_type

    def _infer_let(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        new_env = env
        for pb in expr.patternBindings:
            rhs_type = self.infer(pb.rhs, new_env)
            new_env = self._bind_pattern(pb.pat, rhs_type, new_env)
        return self._infer(expr.body, new_env, expected)

    def _infer_tuple(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        exprs = list(expr.exprs)

        if expected is not None:
            if isinstance(expected, TypeTuple):
                if len(exprs) != len(expected.types):
                    raise TypeCheckError(
                        ERROR_UNEXPECTED_TUPLE_LENGTH,
                        f"Expected tuple of length {len(expected.types)}, got {len(exprs)}"
                    )
                types = []
                for e, et in zip(exprs, expected.types):
                    actual = self._infer(e, env, et)
                    self._expect_type(e, actual, et)
                    types.append(actual)
                return TypeTuple(types)
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_TUPLE,
                    f"Expected type {pretty_type(expected)}, but got a tuple"
                )

        types = [self.infer(e, env) for e in exprs]
        return TypeTuple(types)

    def _infer_dot_tuple(self, expr, env: TypeEnv) -> StellaType:
        tuple_type = self._infer(expr.expr_, env, None)

        index = int(expr.index.text)

        if not isinstance(tuple_type, TypeTuple):
            raise TypeCheckError(
                ERROR_NOT_A_TUPLE,
                f"Expected a tuple type, but got {pretty_type(tuple_type)}"
            )
        if index < 1 or index > len(tuple_type.types):
            raise TypeCheckError(
                ERROR_TUPLE_INDEX_OUT_OF_BOUNDS,
                f"Tuple index {index} out of bounds for tuple of length {len(tuple_type.types)}"
            )

        return tuple_type.types[index - 1]

    def _infer_record(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        bindings = list(expr.bindings)

        seen = set()
        for b in bindings:
            label = b.name.text
            if label in seen:
                raise TypeCheckError(
                    ERROR_DUPLICATE_RECORD_FIELDS,
                    f"Duplicate field '{label}' in record"
                )
            seen.add(label)

        if expected is not None and isinstance(expected, TypeRecord):
            expected_dict = dict(expected.fields)
            provided_labels = {b.name.text for b in bindings}
            expected_labels = set(expected_dict.keys())

            missing = expected_labels - provided_labels
            if missing:
                raise TypeCheckError(
                    ERROR_MISSING_RECORD_FIELDS,
                    f"Missing record fields: {', '.join(sorted(missing))}"
                )

            extra = provided_labels - expected_labels
            if extra:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_RECORD_FIELDS,
                    f"Unexpected record fields: {', '.join(sorted(extra))}"
                )

            fields = []
            for b in bindings:
                label = b.name.text
                exp_type = expected_dict[label]
                actual = self._infer(b.rhs, env, exp_type)
                self._expect_type(b.rhs, actual, exp_type)
                fields.append((label, actual))
            return TypeRecord(fields)

        fields = []
        for b in bindings:
            label = b.name.text
            t = self.infer(b.rhs, env)
            fields.append((label, t))
        return TypeRecord(fields)

    def _infer_dot_record(self, expr, env: TypeEnv) -> StellaType:
        rec_type = self._infer(expr.expr_, env, None)

        if not isinstance(rec_type, TypeRecord):
            raise TypeCheckError(
                ERROR_NOT_A_RECORD,
                f"Expected a record type, but got {pretty_type(rec_type)}"
            )

        label = expr.label.text
        field_type = rec_type.get_field(label)
        if field_type is None:
            raise TypeCheckError(
                ERROR_UNEXPECTED_FIELD_ACCESS,
                f"Record has no field '{label}'"
            )

        return field_type

    def _infer_inl(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None and isinstance(expected, TypeSum):
            actual = self._infer(expr.expr_, env, expected.left)
            self._expect_type(expr.expr_, actual, expected.left)
            return expected
        elif expected is not None:
            raise TypeCheckError(
                ERROR_UNEXPECTED_INJECTION,
                f"Expected type {pretty_type(expected)}, but got an injection (inl)"
            )
        else:
            raise TypeCheckError(
                ERROR_AMBIGUOUS_SUM_TYPE,
                "Cannot determine type of inl without expected sum type"
            )

    def _infer_inr(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None and isinstance(expected, TypeSum):
            actual = self._infer(expr.expr_, env, expected.right)
            self._expect_type(expr.expr_, actual, expected.right)
            return expected
        elif expected is not None:
            raise TypeCheckError(
                ERROR_UNEXPECTED_INJECTION,
                f"Expected type {pretty_type(expected)}, but got an injection (inr)"
            )
        else:
            raise TypeCheckError(
                ERROR_AMBIGUOUS_SUM_TYPE,
                "Cannot determine type of inr without expected sum type"
            )

    def _infer_match(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        cases = list(expr.cases)
        if not cases:
            raise TypeCheckError(
                ERROR_ILLEGAL_EMPTY_MATCHING,
                "Match expression has no cases"
            )

        matched_type = self.infer(expr.expr_, env)

        result_type: Optional[StellaType] = expected

        covered = set()

        for case in cases:
            pat = case.pattern_
            case_env = self._bind_pattern(pat, matched_type, env)
            case_type = self._infer(case.expr_, case_env, result_type)

            if result_type is None:
                result_type = case_type
            else:
                self._expect_type(case.expr_, case_type, result_type)

            covered.add(self._pattern_label(pat))

        self._check_exhaustive(matched_type, covered, expr)

        return result_type if result_type is not None else UNIT

    def _pattern_label(self, pat) -> str:
        name = pat.__class__.__name__
        if name == 'PatternInlContext':
            return 'inl'
        elif name == 'PatternInrContext':
            return 'inr'
        elif name == 'PatternTrueContext':
            return 'true'
        elif name == 'PatternFalseContext':
            return 'false'
        elif name == 'PatternVariantContext':
            return f'variant:{pat.label.text}'
        elif name == 'PatternVarContext':
            return '_'
        elif name == 'PatternUnitContext':
            return 'unit'
        elif name == 'PatternIntContext':
            return f'int:{pat.n.text}'
        elif name == 'PatternSuccContext':
            return 'succ'
        elif name == 'PatternTupleContext':
            return 'tuple'
        elif name == 'PatternRecordContext':
            return 'record'
        elif name == 'PatternListContext':
            n = len(list(pat.patterns)) if hasattr(pat, 'patterns') else 0
            return f'list:{n}'
        elif name == 'PatternConsContext':
            return 'cons'
        elif name == 'PatternAscContext':
            return self._pattern_label(pat.pattern_)
        elif name == 'ParenthesisedPatternContext':
            return self._pattern_label(pat.pattern_)
        elif name == 'patternConsContext':
            return 'cons'
        else:
            return name

    def _check_exhaustive(self, matched_type: StellaType, covered: Set[str], expr):
        if '_' in covered:
            return

        if isinstance(matched_type, TypeSum):
            required = {'inl', 'inr'}
            missing = required - covered
            if missing:
                raise TypeCheckError(
                    ERROR_NONEXHAUSTIVE_MATCH_PATTERNS,
                    f"Non-exhaustive match: missing patterns for {', '.join(sorted(missing))}"
                )

        elif isinstance(matched_type, TypeBool):
            required = {'true', 'false'}
            missing = required - covered
            if missing:
                raise TypeCheckError(
                    ERROR_NONEXHAUSTIVE_MATCH_PATTERNS,
                    f"Non-exhaustive match: missing patterns for {', '.join(sorted(missing))}"
                )

        elif isinstance(matched_type, TypeVariant):
            required = {f'variant:{label}' for label, _ in matched_type.fields}
            missing = required - covered
            if missing:
                raise TypeCheckError(
                    ERROR_NONEXHAUSTIVE_MATCH_PATTERNS,
                    f"Non-exhaustive match: missing variant labels"
                )

        elif isinstance(matched_type, TypeNat):
            has_zero = any(label.startswith('int:') for label in covered)
            has_succ = 'succ' in covered
            if not (has_zero and has_succ):
                pass

        elif isinstance(matched_type, TypeList):
            pass

    def _bind_pattern(self, pat, matched_type: StellaType, env: TypeEnv) -> TypeEnv:
        name = pat.__class__.__name__

        if name == 'PatternVarContext':
            return env.extend(pat.name.text, matched_type)

        if name == 'ParenthesisedPatternContext':
            return self._bind_pattern(pat.pattern_, matched_type, env)

        if name == 'PatternAscContext':
            asc_type = self.parse_type(pat.type_)
            self._expect_type(pat, matched_type, asc_type)
            return self._bind_pattern(pat.pattern_, asc_type, env)

        if name == 'PatternTrueContext':
            if not isinstance(matched_type, TypeBool):
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern true does not match type {pretty_type(matched_type)}"
                )
            return env

        if name == 'PatternFalseContext':
            if not isinstance(matched_type, TypeBool):
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern false does not match type {pretty_type(matched_type)}"
                )
            return env

        if name == 'PatternUnitContext':
            if not isinstance(matched_type, TypeUnit):
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern unit does not match type {pretty_type(matched_type)}"
                )
            return env

        if name == 'PatternIntContext':
            if not isinstance(matched_type, TypeNat):
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern {pat.n.text} does not match type {pretty_type(matched_type)}"
                )
            return env

        if name == 'PatternSuccContext':
            if not isinstance(matched_type, TypeNat):
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern succ(...) does not match type {pretty_type(matched_type)}"
                )
            return self._bind_pattern(pat.pattern_, NAT, env)

        if name == 'PatternInlContext':
            if isinstance(matched_type, TypeSum):
                return self._bind_pattern(pat.pattern_, matched_type.left, env)
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern inl(...) does not match type {pretty_type(matched_type)}"
                )

        if name == 'PatternInrContext':
            if isinstance(matched_type, TypeSum):
                return self._bind_pattern(pat.pattern_, matched_type.right, env)
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Pattern inr(...) does not match type {pretty_type(matched_type)}"
                )

        if name == 'PatternTupleContext':
            patterns = list(pat.patterns)
            if isinstance(matched_type, TypeTuple):
                if len(patterns) != len(matched_type.types):
                    raise TypeCheckError(
                        ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                        f"Tuple pattern has {len(patterns)} elements but type has {len(matched_type.types)}"
                    )
                new_env = env
                for p, t in zip(patterns, matched_type.types):
                    new_env = self._bind_pattern(p, t, new_env)
                return new_env
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Tuple pattern does not match type {pretty_type(matched_type)}"
                )

        if name == 'PatternRecordContext':
            patterns = list(pat.patterns)
            if isinstance(matched_type, TypeRecord):
                field_dict = dict(matched_type.fields)
                new_env = env
                for lp in patterns:
                    label = lp.label.text
                    if label not in field_dict:
                        raise TypeCheckError(
                            ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                            f"Record pattern has field '{label}' not in record type"
                        )
                    new_env = self._bind_pattern(lp.pattern_, field_dict[label], new_env)
                return new_env
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Record pattern does not match type {pretty_type(matched_type)}"
                )

        if name == 'PatternVariantContext':
            label = pat.label.text
            if isinstance(matched_type, TypeVariant):
                found, field_type = matched_type.get_field(label)
                if not found:
                    raise TypeCheckError(
                        ERROR_UNEXPECTED_VARIANT_LABEL,
                        f"Variant type has no label '{label}'"
                    )
                if pat.pattern_ is not None and field_type is not None:
                    return self._bind_pattern(pat.pattern_, field_type, env)
                elif pat.pattern_ is not None and field_type is None:
                    return self._bind_pattern(pat.pattern_, UNIT, env)
                return env
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Variant pattern does not match type {pretty_type(matched_type)}"
                )

        if name == 'PatternListContext':
            patterns = list(pat.patterns) if hasattr(pat, 'patterns') else []
            if isinstance(matched_type, TypeList):
                new_env = env
                for p in patterns:
                    new_env = self._bind_pattern(p, matched_type.element_type, new_env)
                return new_env
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"List pattern does not match type {pretty_type(matched_type)}"
                )

        if name == 'PatternConsContext':
            if isinstance(matched_type, TypeList):
                env = self._bind_pattern(pat.head, matched_type.element_type, env)
                env = self._bind_pattern(pat.tail, matched_type, env)
                return env
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Cons pattern does not match type {pretty_type(matched_type)}"
                )

        if name == 'patternConsContext':
            if isinstance(matched_type, TypeList):
                env = self._bind_pattern(pat.p1, matched_type.element_type, env)
                env = self._bind_pattern(pat.p2, matched_type, env)
                return env
            else:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                    f"Cons pattern does not match type {pretty_type(matched_type)}"
                )

        return env

    def _infer_list(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        exprs = list(expr.exprs)

        if not exprs:
            if expected is not None and isinstance(expected, TypeList):
                return expected
            else:
                raise TypeCheckError(
                    ERROR_AMBIGUOUS_LIST,
                    "Cannot determine element type of empty list without expected type"
                )

        if expected is not None and isinstance(expected, TypeList):
            elem_type = expected.element_type
            for e in exprs:
                actual = self._infer(e, env, elem_type)
                self._expect_type(e, actual, elem_type)
            return TypeList(elem_type)
        else:
            elem_type = self.infer(exprs[0], env)
            for e in exprs[1:]:
                actual = self._infer(e, env, elem_type)
                self._expect_type(e, actual, elem_type)
            return TypeList(elem_type)

    def _infer_cons(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None and isinstance(expected, TypeList):
            elem_type = expected.element_type
            head_actual = self._infer(expr.head, env, elem_type)
            self._expect_type(expr.head, head_actual, elem_type)
            tail_actual = self._infer(expr.tail, env, expected)
            self._expect_type(expr.tail, tail_actual, expected)
            return expected
        else:
            head_type = self.infer(expr.head, env)
            list_type = TypeList(head_type)
            tail_actual = self._infer(expr.tail, env, list_type)
            self._expect_type(expr.tail, tail_actual, list_type)
            return list_type

    def _infer_head(self, expr, env: TypeEnv) -> StellaType:
        list_type = self._infer(expr.list_, env, None)
        if not isinstance(list_type, TypeList):
            raise TypeCheckError(
                ERROR_NOT_A_LIST,
                f"Expected a list type, but got {pretty_type(list_type)}"
            )
        return list_type.element_type

    def _infer_tail(self, expr, env: TypeEnv) -> StellaType:
        list_type = self._infer(expr.list_, env, None)
        if not isinstance(list_type, TypeList):
            raise TypeCheckError(
                ERROR_NOT_A_LIST,
                f"Expected a list type, but got {pretty_type(list_type)}"
            )
        return list_type

    def _infer_variant(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        label = expr.label.text

        if expected is not None and isinstance(expected, TypeVariant):
            found, field_type = expected.get_field(label)
            if not found:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_VARIANT_LABEL,
                    f"Variant type has no label '{label}'"
                )
            if expr.rhs is not None:
                if field_type is not None:
                    actual = self._infer(expr.rhs, env, field_type)
                    self._expect_type(expr.rhs, actual, field_type)
                else:
                    actual = self._infer(expr.rhs, env, UNIT)
            return expected

        elif expected is not None:
            raise TypeCheckError(
                ERROR_UNEXPECTED_VARIANT,
                f"Expected type {pretty_type(expected)}, but got a variant"
            )
        else:
            raise TypeCheckError(
                ERROR_AMBIGUOUS_VARIANT_TYPE,
                f"Cannot determine type of variant '{label}' without expected type"
            )

    def _infer_fix(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None:
            fun_type = TypeFun([expected], expected)
            actual = self._infer(expr.expr_, env, fun_type)
            self._expect_type(expr.expr_, actual, fun_type)
            return expected
        else:
            inner_type = self.infer(expr.expr_, env)
            if not isinstance(inner_type, TypeFun):
                raise TypeCheckError(
                    ERROR_NOT_A_FUNCTION,
                    f"fix expects a function type, but got {pretty_type(inner_type)}"
                )
            if len(inner_type.param_types) != 1:
                raise TypeCheckError(
                    ERROR_NOT_A_FUNCTION,
                    f"fix expects a function with exactly one parameter"
                )
            if inner_type.param_types[0] != inner_type.return_type:
                raise TypeCheckError(
                    ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                    f"fix expects fn(T)->T, but got {pretty_type(inner_type)}"
                )
            return inner_type.return_type
