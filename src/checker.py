from __future__ import annotations
from typing import Optional, List, Dict, Tuple, Set

from stella_types import (
    StellaType, TypeBool, TypeNat, TypeUnit,
    TypeFun, TypeTuple, TypeRecord, TypeSum, TypeList, TypeVariant,
    TypeTop, TypeBottom, TypeRef,
    TypeVar, TypeForAll, TypeRec, TypeInferVar,
    BOOL, NAT, UNIT, TOP, BOTTOM
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
    ERROR_DUPLICATE_FUNCTION_DECLARATION,
    ERROR_EXCEPTION_TYPE_NOT_DECLARED, ERROR_AMBIGUOUS_THROW_TYPE,
    ERROR_AMBIGUOUS_REFERENCE_TYPE, ERROR_AMBIGUOUS_PANIC_TYPE,
    ERROR_NOT_A_REFERENCE, ERROR_UNEXPECTED_MEMORY_ADDRESS,
    ERROR_UNEXPECTED_REFERENCE, ERROR_UNEXPECTED_SUBTYPE,
    ERROR_OCCURS_CHECK_INFINITE_TYPE, ERROR_NOT_A_GENERIC_FUNCTION,
    ERROR_INCORRECT_NUMBER_OF_TYPE_ARGUMENTS, ERROR_UNDEFINED_TYPE_VARIABLE,
)
from unification import unify, apply_subst, unify_one
from context import TypeEnv
from pretty import pretty_type, pretty_expr

class TypeChecker:
    def __init__(self, extensions: set):
        self.extensions = extensions
        self.functions: Dict[str, StellaType] = {}
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

        self.exception_type = None
        self.structural_subtyping = '#structural-subtyping' in extensions
        self.ambiguous_as_bottom = '#ambiguous-type-as-bottom' in extensions
        self.has_sequencing = '#sequencing' in extensions
        self.has_references = '#references' in extensions
        self.has_exceptions = '#exceptions' in extensions
        self.has_type_cast = '#type-cast' in extensions
        self.has_panic = '#panic' in extensions

        self.type_reconstruction = '#type-reconstruction' in extensions
        self.universal_types = '#universal-types' in extensions
        self.has_recursive_types = '#recursive-types' in extensions
        self.has_letrec = '#letrec' in extensions

        self._next_var = 0
        self.constraints: List[Tuple[StellaType, StellaType]] = []
        self.subst: Dict[int, StellaType] = {}
        self.current_type_vars: Set[str] = set()

        self.type_aliases: Dict[str, StellaType] = {}

    def fresh_var(self) -> TypeInferVar:
        v = TypeInferVar(self._next_var)
        self._next_var += 1
        return v

    def parse_type(self, ctx, type_vars=None) -> StellaType:
        if type_vars is None:
            type_vars = set(self.current_type_vars)

        name = ctx.__class__.__name__

        if name == 'TypeBoolContext':
            return BOOL
        elif name == 'TypeNatContext':
            return NAT
        elif name == 'TypeUnitContext':
            return UNIT
        elif name == 'TypeTopContext':
            return TOP
        elif name == 'TypeBottomContext':
            return BOTTOM
        elif name == 'TypeAutoContext':
            return self.fresh_var()
        elif name == 'TypeRefContext':
            return TypeRef(self.parse_type(ctx.type_, type_vars))
        elif name == 'TypeFunContext':
            param_types = [self.parse_type(p, type_vars) for p in ctx.paramTypes]
            ret_type = self.parse_type(ctx.returnType, type_vars)
            return TypeFun(param_types, ret_type)
        elif name == 'TypeTupleContext':
            types = [self.parse_type(t, type_vars) for t in ctx.types]
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
                fields.append((label, self.parse_type(ft.type_, type_vars)))
            return TypeRecord(fields)
        elif name == 'TypeSumContext':
            return TypeSum(
                self.parse_type(ctx.left, type_vars),
                self.parse_type(ctx.right, type_vars)
            )
        elif name == 'TypeListContext':
            return TypeList(self.parse_type(ctx.type_, type_vars))
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
                    fields.append((label, self.parse_type(ft.type_, type_vars)))
                else:
                    fields.append((label, None))
            return TypeVariant(fields)
        elif name == 'TypeVarContext':
            var_name = ctx.name.text
            if var_name in type_vars:
                return TypeVar(var_name)
            if var_name in self.type_aliases:
                return self.type_aliases[var_name]
            if self.universal_types or self.has_recursive_types:
                raise TypeCheckError(
                    ERROR_UNDEFINED_TYPE_VARIABLE,
                    f"Undefined type variable: {var_name}"
                )
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Undefined type: {var_name}"
            )
        elif name == 'TypeForAllContext':
            vars_list = [t.text for t in ctx.types]
            new_type_vars = set(type_vars) | set(vars_list)
            body = self.parse_type(ctx.type_, new_type_vars)
            return TypeForAll(vars_list, body)
        elif name == 'TypeRecContext':
            var_name = ctx.var.text
            new_type_vars = set(type_vars) | {var_name}
            body = self.parse_type(ctx.type_, new_type_vars)
            return TypeRec(var_name, body)
        elif name == 'TypeParensContext':
            return self.parse_type(ctx.type_, type_vars)
        else:
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Unknown type context: {name}"
            )

    def is_subtype(self, sub: StellaType, sup: StellaType) -> bool:
        if isinstance(sub, TypeBottom):
            return True
        if isinstance(sup, TypeTop):
            return True
        if sub == sup:
            return True
        if isinstance(sub, TypeFun) and isinstance(sup, TypeFun):
            if len(sub.param_types) != len(sup.param_types):
                return False
            for sp, pp in zip(sup.param_types, sub.param_types):
                if not self.is_subtype(sp, pp):
                    return False
            return self.is_subtype(sub.return_type, sup.return_type)
        if isinstance(sub, TypeTuple) and isinstance(sup, TypeTuple):
            if len(sub.types) != len(sup.types):
                return False
            return all(self.is_subtype(s, p) for s, p in zip(sub.types, sup.types))
        if isinstance(sub, TypeRecord) and isinstance(sup, TypeRecord):
            sub_dict = dict(sub.fields)
            for label, sup_type in sup.fields:
                if label not in sub_dict:
                    return False
                if not self.is_subtype(sub_dict[label], sup_type):
                    return False
            return True
        if isinstance(sub, TypeVariant) and isinstance(sup, TypeVariant):
            sup_dict = dict(sup.fields)
            for label, sub_type in sub.fields:
                if label not in sup_dict:
                    return False
                sup_type2 = sup_dict[label]
                if sub_type is not None and sup_type2 is not None:
                    if not self.is_subtype(sub_type, sup_type2):
                        return False
            return True
        if isinstance(sub, TypeRef) and isinstance(sup, TypeRef):
            return sub.inner_type == sup.inner_type
        if isinstance(sub, TypeList) and isinstance(sup, TypeList):
            return self.is_subtype(sub.element_type, sup.element_type)
        if isinstance(sub, TypeSum) and isinstance(sup, TypeSum):
            return self.is_subtype(sub.left, sup.left) and self.is_subtype(sub.right, sup.right)
        return False

    def _expect_type(self, expr, actual: StellaType, expected: StellaType):
        if self.type_reconstruction:
            actual_resolved = apply_subst(self.subst, actual)
            expected_resolved = apply_subst(self.subst, expected)
            if isinstance(actual_resolved, TypeInferVar) or isinstance(expected_resolved, TypeInferVar):
                unify_one(actual_resolved, expected_resolved, self.subst)
                return
            actual = actual_resolved
            expected = expected_resolved

        if self.structural_subtyping:
            if not self.is_subtype(actual, expected):
                if isinstance(actual, TypeRecord) and isinstance(expected, TypeRecord):
                    actual_dict = dict(actual.fields)
                    missing = [lbl for lbl, _ in expected.fields if lbl not in actual_dict]
                    if missing:
                        raise TypeCheckError(
                            ERROR_MISSING_RECORD_FIELDS,
                            f"Missing record fields: {', '.join(sorted(missing))}"
                        )
                raise TypeCheckError(
                    ERROR_UNEXPECTED_SUBTYPE,
                    f"Expected type {pretty_type(expected)}, but got {pretty_type(actual)}"
                    + (f" for expression {pretty_expr(expr)}" if expr is not None else "")
                )
        else:
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

        for decl in program_ctx.decls:
            if decl.__class__.__name__ == 'DeclExceptionTypeContext':
                self.exception_type = self.parse_type(decl.exceptionType)

        seen_names = set()
        for decl in program_ctx.decls:
            cname = decl.__class__.__name__
            if cname in ('DeclFunContext', 'DeclFunGenericContext'):
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
            elif cname == 'DeclFunGenericContext':
                fn_type = self._get_generic_fun_type(decl)
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
            elif cname == 'DeclFunGenericContext':
                self._check_generic_fun_decl(decl, global_env)

        if self.type_reconstruction and self.constraints:
            self.subst = unify(self.constraints, self.subst)
            self.constraints = []

    def _get_fun_type(self, decl, type_vars=None) -> TypeFun:
        if type_vars is None:
            type_vars = set()
        param_types = []
        for pd in decl.paramDecls:
            param_types.append(self.parse_type(pd.paramType, type_vars))

        if decl.returnType is not None:
            ret_type = self.parse_type(decl.returnType, type_vars)
        else:
            ret_type = UNIT

        return TypeFun(param_types, ret_type)

    def _get_generic_fun_type(self, decl) -> TypeForAll:
        generics = [g.text for g in decl.generics]
        type_vars = set(generics)
        param_types = [self.parse_type(pd.paramType, type_vars) for pd in decl.paramDecls]
        ret_type = self.parse_type(decl.returnType, type_vars) if decl.returnType else UNIT
        return TypeForAll(generics, TypeFun(param_types, ret_type))

    def _check_fun_decl(self, decl, global_env: TypeEnv, type_vars=None):
        if type_vars is None:
            type_vars = set()
        self.current_fn = decl.name.text
        old_type_vars = self.current_type_vars
        self.current_type_vars = set(type_vars)

        fn_type = self.functions[decl.name.text]

        env = global_env
        for pd, param_type in zip(decl.paramDecls, fn_type.param_types):
            env = env.extend(pd.name.text, param_type)

        local_functions = {}
        for local_decl in decl.localDecls:
            local_cname = local_decl.__class__.__name__
            if local_cname == 'DeclFunContext':
                local_fn_type = self._get_fun_type(local_decl, type_vars)
                local_functions[local_decl.name.text] = local_fn_type
                env = env.extend(local_decl.name.text, local_fn_type)

        for local_decl in decl.localDecls:
            local_cname = local_decl.__class__.__name__
            if local_cname == 'DeclFunContext':
                old_fn = self.functions.get(local_decl.name.text)
                self.functions[local_decl.name.text] = local_functions[local_decl.name.text]
                self._check_fun_decl(local_decl, env, type_vars)
                if old_fn is None:
                    del self.functions[local_decl.name.text]
                else:
                    self.functions[local_decl.name.text] = old_fn

        ret_type = fn_type.return_type
        actual = self.infer_with_expected(decl.returnExpr, env, ret_type)
        self._expect_type(decl.returnExpr, actual, ret_type)

        self.current_type_vars = old_type_vars

    def _check_generic_fun_decl(self, decl, global_env: TypeEnv):
        self.current_fn = decl.name.text
        generics = [g.text for g in decl.generics]
        old_type_vars = self.current_type_vars
        self.current_type_vars = set(generics)

        fn_forall = self.functions[decl.name.text]
        fn_type = fn_forall.body

        env = global_env
        for pd, param_type in zip(decl.paramDecls, fn_type.param_types):
            env = env.extend(pd.name.text, param_type)

        for local_decl in decl.localDecls:
            if local_decl.__class__.__name__ == 'DeclFunContext':
                local_fn_type = self._get_fun_type(local_decl, set(generics))
                self.functions[local_decl.name.text] = local_fn_type
                env = env.extend(local_decl.name.text, local_fn_type)

        ret_type = fn_type.return_type
        actual = self.infer_with_expected(decl.returnExpr, env, ret_type)
        self._expect_type(decl.returnExpr, actual, ret_type)

        self.current_type_vars = old_type_vars

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
            if self.type_reconstruction:
                t = apply_subst(self.subst, t)
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

        if name == 'SequenceContext':
            self.check(expr.expr1, UNIT, env)
            return self._infer(expr.expr2, env, expected)

        if name == 'RefContext':
            return self._infer_ref(expr, env, expected)

        if name == 'DerefContext':
            return self._infer_deref(expr, env, expected)

        if name == 'AssignContext':
            return self._infer_assign(expr, env)

        if name == 'ConstMemoryContext':
            return self._infer_const_memory(expr, env, expected)

        if name == 'PanicContext':
            return self._infer_panic(expr, env, expected)

        if name == 'ThrowContext':
            return self._infer_throw(expr, env, expected)

        if name == 'TryWithContext':
            if expected is not None:
                try_type = self._infer(expr.tryExpr, env, expected)
                self._expect_type(expr.tryExpr, try_type, expected)
                fallback_type = self._infer(expr.fallbackExpr, env, expected)
                self._expect_type(expr.fallbackExpr, fallback_type, expected)
                return expected
            else:
                try_type = self.infer(expr.tryExpr, env)
                fallback_type = self._infer(expr.fallbackExpr, env, try_type)
                self._expect_type(expr.fallbackExpr, fallback_type, try_type)
                return try_type

        if name == 'TryCatchContext':
            return self._infer_try_catch(expr, env, expected)

        if name == 'TypeCastContext':
            self._infer(expr.expr_, env, None)
            return self.parse_type(expr.type_)

        if name == 'TryCastAsContext':
            return self._infer_try_cast_as(expr, env, expected)

        if name == 'TypeAbstractionContext':
            return self._infer_type_abstraction(expr, env, expected)

        if name == 'TypeApplicationContext':
            return self._infer_type_application(expr, env, expected)

        if name == 'FoldContext':
            return self._infer_fold(expr, env, expected)

        if name == 'UnfoldContext':
            return self._infer_unfold(expr, env, expected)

        if name == 'LetRecContext':
            return self._infer_letrec(expr, env, expected)

        raise TypeCheckError(
            ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
            f"Unsupported expression type: {name}"
        )

    def _infer_abstraction(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        params = list(expr.paramDecls)

        if self.type_reconstruction and expected is not None:
            expected = apply_subst(self.subst, expected)

        if expected is not None and not isinstance(expected, (TypeFun, TypeInferVar, TypeTop)):
            raise TypeCheckError(
                ERROR_UNEXPECTED_LAMBDA,
                f"Expected type {pretty_type(expected)}, but got a lambda"
            )

        if expected is not None and isinstance(expected, TypeFun):
            if len(params) == len(expected.param_types):
                param_types = expected.param_types
                annotated_params = []
                for pd, exp_pt in zip(params, param_types):
                    ann_type = self.parse_type(pd.paramType)
                    if not isinstance(ann_type, TypeInferVar) and ann_type != exp_pt:
                        raise TypeCheckError(
                            ERROR_UNEXPECTED_TYPE_FOR_PARAMETER,
                            f"Expected parameter type {pretty_type(exp_pt)}, but got {pretty_type(ann_type)}"
                        )
                    annotated_params.append(ann_type if not isinstance(ann_type, TypeInferVar) else exp_pt)

                new_env = env
                for pd, pt in zip(params, annotated_params):
                    new_env = new_env.extend(pd.name.text, pt)

                body_expected = expected.return_type
                body_type = self._infer(expr.returnExpr, new_env, body_expected)
                self._expect_type(expr.returnExpr, body_type, body_expected)
                return TypeFun(annotated_params, body_type)

        if self.type_reconstruction and expected is not None and isinstance(expected, TypeInferVar):
            param_types = []
            new_env = env
            for pd in params:
                ann_type = self.parse_type(pd.paramType)
                param_types.append(ann_type)
                new_env = new_env.extend(pd.name.text, ann_type)
            body_type = self.infer(expr.returnExpr, new_env)
            fun_type = TypeFun(param_types, body_type)
            unify_one(expected, fun_type, self.subst)
            return fun_type

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

        if self.type_reconstruction:
            fun_type = apply_subst(self.subst, fun_type)

        if self.type_reconstruction and not isinstance(fun_type, TypeFun):
            args = list(expr.args)
            param_vars = [self.fresh_var() for _ in args]
            ret_var = self.fresh_var()
            new_fun_type = TypeFun(param_vars, ret_var)
            unify_one(fun_type, new_fun_type, self.subst)
            fun_type = apply_subst(self.subst, fun_type)
        elif isinstance(fun_type, TypeInferVar):
            args = list(expr.args)
            param_vars = [self.fresh_var() for _ in args]
            ret_var = self.fresh_var()
            new_fun_type = TypeFun(param_vars, ret_var)
            unify_one(fun_type, new_fun_type, self.subst)
            fun_type = apply_subst(self.subst, fun_type)

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

        if self.type_reconstruction:
            tuple_type = apply_subst(self.subst, tuple_type)

        if isinstance(tuple_type, TypeInferVar) and self.type_reconstruction:
            size = max(index, 2) if self.has_pairs else index
            elem_vars = [self.fresh_var() for _ in range(size)]
            unify_one(tuple_type, TypeTuple(elem_vars), self.subst)
            return apply_subst(self.subst, elem_vars[index - 1])

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
        if expected is not None and not isinstance(expected, (TypeRecord, TypeInferVar, TypeTop)):
            raise TypeCheckError(
                ERROR_UNEXPECTED_RECORD,
                f"Expected type {pretty_type(expected)}, but got a record"
            )

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

            if not self.structural_subtyping:
                extra = provided_labels - expected_labels
                if extra:
                    raise TypeCheckError(
                        ERROR_UNEXPECTED_RECORD_FIELDS,
                        f"Unexpected record fields: {', '.join(sorted(extra))}"
                    )

            fields = []
            for b in bindings:
                label = b.name.text
                if label in expected_dict:
                    exp_type = expected_dict[label]
                    actual = self._infer(b.rhs, env, exp_type)
                    self._expect_type(b.rhs, actual, exp_type)
                    fields.append((label, actual))
                else:
                    actual = self.infer(b.rhs, env)
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
        if self.type_reconstruction and expected is not None:
            expected = apply_subst(self.subst, expected)

        if expected is not None and isinstance(expected, TypeSum):
            actual = self._infer(expr.expr_, env, expected.left)
            self._expect_type(expr.expr_, actual, expected.left)
            return expected
        elif expected is not None and isinstance(expected, TypeInferVar) and self.type_reconstruction:
            inner = self.infer(expr.expr_, env)
            right_var = self.fresh_var()
            sum_type = TypeSum(inner, right_var)
            unify_one(expected, sum_type, self.subst)
            return apply_subst(self.subst, sum_type)
        elif expected is not None and not isinstance(expected, TypeTop):
            raise TypeCheckError(
                ERROR_UNEXPECTED_INJECTION,
                f"Expected type {pretty_type(expected)}, but got an injection (inl)"
            )
        else:
            if self.ambiguous_as_bottom:
                inner = self.infer(expr.expr_, env)
                return TypeSum(inner, BOTTOM)
            elif self.type_reconstruction:
                inner = self.infer(expr.expr_, env)
                right_var = self.fresh_var()
                return TypeSum(inner, right_var)
            else:
                raise TypeCheckError(
                    ERROR_AMBIGUOUS_SUM_TYPE,
                    "Cannot determine type of inl without expected sum type"
                )

    def _infer_inr(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if self.type_reconstruction and expected is not None:
            expected = apply_subst(self.subst, expected)

        if expected is not None and isinstance(expected, TypeSum):
            actual = self._infer(expr.expr_, env, expected.right)
            self._expect_type(expr.expr_, actual, expected.right)
            return expected
        elif expected is not None and isinstance(expected, TypeInferVar) and self.type_reconstruction:
            inner = self.infer(expr.expr_, env)
            left_var = self.fresh_var()
            sum_type = TypeSum(left_var, inner)
            unify_one(expected, sum_type, self.subst)
            return apply_subst(self.subst, sum_type)
        elif expected is not None and not isinstance(expected, TypeTop):
            raise TypeCheckError(
                ERROR_UNEXPECTED_INJECTION,
                f"Expected type {pretty_type(expected)}, but got an injection (inr)"
            )
        else:
            if self.ambiguous_as_bottom:
                inner = self.infer(expr.expr_, env)
                return TypeSum(BOTTOM, inner)
            elif self.type_reconstruction:
                inner = self.infer(expr.expr_, env)
                left_var = self.fresh_var()
                return TypeSum(left_var, inner)
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

        resolved_matched = apply_subst(self.subst, matched_type) if self.type_reconstruction else matched_type
        self._check_exhaustive(resolved_matched, covered, expr)

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
            if self.type_reconstruction and isinstance(matched_type, TypeInferVar):
                sum_left = self.fresh_var()
                sum_right = self.fresh_var()
                unify_one(matched_type, TypeSum(sum_left, sum_right), self.subst)
                resolved = apply_subst(self.subst, matched_type)
                return self._bind_pattern(pat.pattern_, resolved.left, env)
            if isinstance(matched_type, TypeSum):
                return self._bind_pattern(pat.pattern_, matched_type.left, env)
            raise TypeCheckError(
                ERROR_UNEXPECTED_PATTERN_FOR_TYPE,
                f"Pattern inl(...) does not match type {pretty_type(matched_type)}"
            )

        if name == 'PatternInrContext':
            if self.type_reconstruction and isinstance(matched_type, TypeInferVar):
                sum_left = self.fresh_var()
                sum_right = self.fresh_var()
                unify_one(matched_type, TypeSum(sum_left, sum_right), self.subst)
                resolved = apply_subst(self.subst, matched_type)
                return self._bind_pattern(pat.pattern_, resolved.right, env)
            if isinstance(matched_type, TypeSum):
                return self._bind_pattern(pat.pattern_, matched_type.right, env)
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
        if expected is not None and not isinstance(expected, (TypeList, TypeInferVar, TypeTop)):
            raise TypeCheckError(
                ERROR_UNEXPECTED_LIST,
                f"Expected type {pretty_type(expected)}, but got a list"
            )

        exprs = list(expr.exprs)

        if not exprs:
            if expected is not None and isinstance(expected, TypeList):
                return expected
            elif self.ambiguous_as_bottom:
                return TypeList(BOTTOM)
            elif self.type_reconstruction:
                return TypeList(self.fresh_var())
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

        elif expected is not None and not isinstance(expected, TypeTop):
            raise TypeCheckError(
                ERROR_UNEXPECTED_VARIANT,
                f"Expected type {pretty_type(expected)}, but got a variant"
            )
        else:
            if self.ambiguous_as_bottom:
                if expr.rhs is not None:
                    inner = self.infer(expr.rhs, env)
                else:
                    inner = None
                return TypeVariant([(label, inner)])
            else:
                raise TypeCheckError(
                    ERROR_AMBIGUOUS_VARIANT_TYPE,
                    f"Cannot determine type of variant '{label}' without expected type"
                )

    def _infer_fix(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if self.type_reconstruction and expected is None:
            ret_var = self.fresh_var()
            fun_type = TypeFun([ret_var], ret_var)
            actual = self._infer(expr.expr_, env, fun_type)
            self._expect_type(expr.expr_, actual, fun_type)
            return apply_subst(self.subst, ret_var)

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

    def _infer_ref(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None and isinstance(expected, TypeRef):
            actual = self._infer(expr.expr_, env, expected.inner_type)
            self._expect_type(expr.expr_, actual, expected.inner_type)
            return expected
        elif expected is not None and not isinstance(expected, TypeTop):
            raise TypeCheckError(
                ERROR_UNEXPECTED_REFERENCE,
                f"Expected type {pretty_type(expected)}, but got a reference"
            )
        else:
            inner = self.infer(expr.expr_, env)
            return TypeRef(inner)

    def _infer_deref(self, expr, env: TypeEnv, expected: Optional[StellaType] = None) -> StellaType:
        inner_expected = TypeRef(expected) if expected is not None else None
        ref_type = self._infer(expr.expr_, env, inner_expected)
        if self.type_reconstruction:
            from unification import apply_subst
            ref_type = apply_subst(self.subst, ref_type)
        if not isinstance(ref_type, TypeRef):
            raise TypeCheckError(
                ERROR_NOT_A_REFERENCE,
                f"Expected a reference type, but got {pretty_type(ref_type)}"
            )
        return ref_type.inner_type

    def _infer_assign(self, expr, env: TypeEnv) -> StellaType:
        lhs_type = self.infer(expr.lhs, env)
        if not isinstance(lhs_type, TypeRef):
            raise TypeCheckError(
                ERROR_NOT_A_REFERENCE,
                f"Left-hand side of assignment must be a reference, but got {pretty_type(lhs_type)}"
            )
        self.check(expr.rhs, lhs_type.inner_type, env)
        return UNIT

    def _infer_const_memory(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None and isinstance(expected, TypeRef):
            return expected
        elif expected is not None and not isinstance(expected, TypeTop):
            raise TypeCheckError(
                ERROR_UNEXPECTED_MEMORY_ADDRESS,
                f"Unexpected memory address for type {pretty_type(expected)}"
            )
        elif self.ambiguous_as_bottom:
            return TypeRef(BOTTOM)
        else:
            raise TypeCheckError(
                ERROR_AMBIGUOUS_REFERENCE_TYPE,
                "Cannot determine type of memory address without expected reference type"
            )

    def _infer_panic(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if expected is not None:
            return expected
        elif self.ambiguous_as_bottom:
            return BOTTOM
        else:
            raise TypeCheckError(
                ERROR_AMBIGUOUS_PANIC_TYPE,
                "Cannot determine type of panic! without expected type"
            )

    def _infer_throw(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if self.exception_type is None:
            raise TypeCheckError(
                ERROR_EXCEPTION_TYPE_NOT_DECLARED,
                "Exception type not declared"
            )
        self.check(expr.expr_, self.exception_type, env)
        if expected is not None:
            return expected
        elif self.ambiguous_as_bottom:
            return BOTTOM
        else:
            raise TypeCheckError(
                ERROR_AMBIGUOUS_THROW_TYPE,
                "Cannot determine type of throw without expected type"
            )

    def _infer_try_catch(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        if self.exception_type is None:
            raise TypeCheckError(
                ERROR_EXCEPTION_TYPE_NOT_DECLARED,
                "Exception type not declared"
            )
        if expected is not None:
            try_type = self._infer(expr.tryExpr, env, expected)
            self._expect_type(expr.tryExpr, try_type, expected)
            result_type = expected
        else:
            try_type = self.infer(expr.tryExpr, env)
            result_type = try_type
        handler_env = self._bind_pattern(expr.pat, self.exception_type, env)
        handler_type = self._infer(expr.fallbackExpr, handler_env, result_type)
        self._expect_type(expr.fallbackExpr, handler_type, result_type)
        return result_type

    def _infer_try_cast_as(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        self._infer(expr.tryExpr, env, None)
        cast_type = self.parse_type(expr.type_)
        pat_env = self._bind_pattern(expr.pattern_, cast_type, env)
        if expected is not None:
            branch_type = expected
        else:
            branch_type = self._infer(expr.expr_, pat_env, None)
        self.check(expr.expr_, branch_type, pat_env)
        self.check(expr.fallbackExpr, branch_type, env)
        return branch_type

    def _infer_type_abstraction(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        generics = [g.text for g in expr.generics]
        old_type_vars = self.current_type_vars
        self.current_type_vars = set(generics)

        body_expected = None
        if expected is not None and isinstance(expected, TypeForAll):
            if expected.vars == generics:
                body_expected = expected.body

        body_type = self._infer(expr.expr_, env, body_expected)
        self.current_type_vars = old_type_vars
        return TypeForAll(generics, body_type)

    def _infer_type_application(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        fun_type = self._infer(expr.fun, env, None)

        if self.type_reconstruction:
            fun_type = apply_subst(self.subst, fun_type)

        if not isinstance(fun_type, TypeForAll):
            raise TypeCheckError(
                ERROR_NOT_A_GENERIC_FUNCTION,
                f"Expected a generic (forall) function, but got {pretty_type(fun_type)}"
                + (f" for expression {pretty_expr(expr.fun)}" if expr.fun is not None else "")
            )

        type_args = [self.parse_type(t) for t in expr.types]

        if len(type_args) != len(fun_type.vars):
            raise TypeCheckError(
                ERROR_INCORRECT_NUMBER_OF_TYPE_ARGUMENTS,
                f"Generic function expects {len(fun_type.vars)} type arguments, "
                f"but got {len(type_args)}"
            )

        result = self.subst_type_vars(fun_type.body, dict(zip(fun_type.vars, type_args)))
        return result

    def _infer_fold(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        rec_type = self.parse_type(expr.type_)
        if not isinstance(rec_type, TypeRec):
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"fold expects a recursive type annotation, but got {pretty_type(rec_type)}"
            )
        unfolded = self.unfold_rec(rec_type)
        actual = self._infer(expr.expr_, env, unfolded)
        self._expect_type(expr.expr_, actual, unfolded)
        return rec_type

    def _infer_unfold(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        rec_type = self.parse_type(expr.type_)
        if not isinstance(rec_type, TypeRec):
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"unfold expects a recursive type annotation, but got {pretty_type(rec_type)}"
            )
        actual = self._infer(expr.expr_, env, rec_type)
        self._expect_type(expr.expr_, actual, rec_type)
        return self.unfold_rec(rec_type)

    def _infer_letrec(self, expr, env: TypeEnv, expected: Optional[StellaType]) -> StellaType:
        new_env = env
        binding_types = []
        for pb in expr.patternBindings:
            if self.type_reconstruction:
                bvar = self.fresh_var()
                binding_types.append(bvar)
                new_env = self._bind_pattern(pb.pat, bvar, new_env)
            else:
                rhs_type = self.infer(pb.rhs, new_env)
                binding_types.append(rhs_type)
                new_env = self._bind_pattern(pb.pat, rhs_type, new_env)

        if self.type_reconstruction:
            for pb, btype in zip(expr.patternBindings, binding_types):
                actual = self._infer(pb.rhs, new_env, btype)
                self._expect_type(pb.rhs, actual, btype)

        return self._infer(expr.body, new_env, expected)

    def unfold_rec(self, rec_type: TypeRec) -> StellaType:
        return self.subst_type_var(rec_type.body, rec_type.var, rec_type)

    def subst_type_var(self, t: StellaType, var_name: str, replacement: StellaType) -> StellaType:
        return self.subst_type_vars(t, {var_name: replacement})

    def subst_type_vars(self, t: StellaType, mapping: Dict[str, StellaType]) -> StellaType:
        if isinstance(t, TypeVar):
            return mapping.get(t.name, t)
        elif isinstance(t, TypeFun):
            return TypeFun(
                [self.subst_type_vars(p, mapping) for p in t.param_types],
                self.subst_type_vars(t.return_type, mapping)
            )
        elif isinstance(t, TypeTuple):
            return TypeTuple([self.subst_type_vars(e, mapping) for e in t.types])
        elif isinstance(t, TypeRecord):
            return TypeRecord([(lbl, self.subst_type_vars(ty, mapping)) for lbl, ty in t.fields])
        elif isinstance(t, TypeSum):
            return TypeSum(
                self.subst_type_vars(t.left, mapping),
                self.subst_type_vars(t.right, mapping)
            )
        elif isinstance(t, TypeList):
            return TypeList(self.subst_type_vars(t.element_type, mapping))
        elif isinstance(t, TypeVariant):
            return TypeVariant([
                (lbl, self.subst_type_vars(ty, mapping) if ty is not None else None)
                for lbl, ty in t.fields
            ])
        elif isinstance(t, TypeRef):
            return TypeRef(self.subst_type_vars(t.inner_type, mapping))
        elif isinstance(t, TypeForAll):
            inner_mapping = {k: v for k, v in mapping.items() if k not in t.vars}
            if not inner_mapping:
                return t
            return TypeForAll(t.vars, self.subst_type_vars(t.body, inner_mapping))
        elif isinstance(t, TypeRec):
            inner_mapping = {k: v for k, v in mapping.items() if k != t.var}
            if not inner_mapping:
                return t
            return TypeRec(t.var, self.subst_type_vars(t.body, inner_mapping))
        else:
            return t
