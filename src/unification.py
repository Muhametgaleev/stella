from __future__ import annotations
from typing import Dict, List, Tuple, Optional

from stella_types import (
    StellaType, TypeInferVar, TypeFun, TypeTuple, TypeRecord, TypeSum,
    TypeList, TypeVariant, TypeRef, TypeForAll, TypeRec, TypeBool, TypeNat,
    TypeUnit, TypeTop, TypeBottom, TypeVar
)
from errors import TypeCheckError, ERROR_OCCURS_CHECK_INFINITE_TYPE, ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION

def apply_subst(subst: Dict[int, StellaType], t: StellaType) -> StellaType:
    if isinstance(t, TypeInferVar):
        if t.id in subst:
            resolved = apply_subst(subst, subst[t.id])
            subst[t.id] = resolved
            return resolved
        return t
    elif isinstance(t, TypeFun):
        return TypeFun(
            [apply_subst(subst, p) for p in t.param_types],
            apply_subst(subst, t.return_type)
        )
    elif isinstance(t, TypeTuple):
        return TypeTuple([apply_subst(subst, e) for e in t.types])
    elif isinstance(t, TypeRecord):
        return TypeRecord([(lbl, apply_subst(subst, ty)) for lbl, ty in t.fields])
    elif isinstance(t, TypeSum):
        return TypeSum(apply_subst(subst, t.left), apply_subst(subst, t.right))
    elif isinstance(t, TypeList):
        return TypeList(apply_subst(subst, t.element_type))
    elif isinstance(t, TypeVariant):
        new_fields = []
        for lbl, ty in t.fields:
            new_fields.append((lbl, apply_subst(subst, ty) if ty is not None else None))
        return TypeVariant(new_fields)
    elif isinstance(t, TypeRef):
        return TypeRef(apply_subst(subst, t.inner_type))
    elif isinstance(t, TypeForAll):
        return TypeForAll(t.vars, apply_subst(subst, t.body))
    elif isinstance(t, TypeRec):
        return TypeRec(t.var, apply_subst(subst, t.body))
    else:
        return t

def occurs_in(var_id: int, t: StellaType, subst: Dict[int, StellaType]) -> bool:
    t = apply_subst(subst, t)
    if isinstance(t, TypeInferVar):
        return t.id == var_id
    elif isinstance(t, TypeFun):
        return any(occurs_in(var_id, p, subst) for p in t.param_types) or \
               occurs_in(var_id, t.return_type, subst)
    elif isinstance(t, TypeTuple):
        return any(occurs_in(var_id, e, subst) for e in t.types)
    elif isinstance(t, TypeRecord):
        return any(occurs_in(var_id, ty, subst) for _, ty in t.fields)
    elif isinstance(t, TypeSum):
        return occurs_in(var_id, t.left, subst) or occurs_in(var_id, t.right, subst)
    elif isinstance(t, TypeList):
        return occurs_in(var_id, t.element_type, subst)
    elif isinstance(t, TypeVariant):
        return any(occurs_in(var_id, ty, subst) for _, ty in t.fields if ty is not None)
    elif isinstance(t, TypeRef):
        return occurs_in(var_id, t.inner_type, subst)
    elif isinstance(t, TypeForAll):
        return occurs_in(var_id, t.body, subst)
    elif isinstance(t, TypeRec):
        return occurs_in(var_id, t.body, subst)
    else:
        return False

def unify_one(t1: StellaType, t2: StellaType, subst: Dict[int, StellaType]) -> None:
    t1 = apply_subst(subst, t1)
    t2 = apply_subst(subst, t2)

    if t1 == t2:
        return

    if isinstance(t1, TypeInferVar):
        if occurs_in(t1.id, t2, subst):
            raise TypeCheckError(
                ERROR_OCCURS_CHECK_INFINITE_TYPE,
                f"Occurs check failed: ?T{t1.id} occurs in {repr(t2)}"
            )
        subst[t1.id] = t2
        return

    if isinstance(t2, TypeInferVar):
        if occurs_in(t2.id, t1, subst):
            raise TypeCheckError(
                ERROR_OCCURS_CHECK_INFINITE_TYPE,
                f"Occurs check failed: ?T{t2.id} occurs in {repr(t1)}"
            )
        subst[t2.id] = t1
        return

    if isinstance(t1, TypeFun) and isinstance(t2, TypeFun):
        if len(t1.param_types) != len(t2.param_types):
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Cannot unify {repr(t1)} with {repr(t2)}: different number of parameters"
            )
        for p1, p2 in zip(t1.param_types, t2.param_types):
            unify_one(p1, p2, subst)
        unify_one(t1.return_type, t2.return_type, subst)
        return

    if isinstance(t1, TypeTuple) and isinstance(t2, TypeTuple):
        if len(t1.types) != len(t2.types):
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Cannot unify {repr(t1)} with {repr(t2)}: different tuple sizes"
            )
        for e1, e2 in zip(t1.types, t2.types):
            unify_one(e1, e2, subst)
        return

    if isinstance(t1, TypeRecord) and isinstance(t2, TypeRecord):
        d1 = dict(t1.fields)
        d2 = dict(t2.fields)
        if set(d1.keys()) != set(d2.keys()):
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Cannot unify {repr(t1)} with {repr(t2)}: different record fields"
            )
        for lbl in d1:
            unify_one(d1[lbl], d2[lbl], subst)
        return

    if isinstance(t1, TypeSum) and isinstance(t2, TypeSum):
        unify_one(t1.left, t2.left, subst)
        unify_one(t1.right, t2.right, subst)
        return

    if isinstance(t1, TypeList) and isinstance(t2, TypeList):
        unify_one(t1.element_type, t2.element_type, subst)
        return

    if isinstance(t1, TypeVariant) and isinstance(t2, TypeVariant):
        d1 = dict(t1.fields)
        d2 = dict(t2.fields)
        if set(d1.keys()) != set(d2.keys()):
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Cannot unify {repr(t1)} with {repr(t2)}: different variant labels"
            )
        for lbl in d1:
            if d1[lbl] is not None and d2[lbl] is not None:
                unify_one(d1[lbl], d2[lbl], subst)
        return

    if isinstance(t1, TypeRef) and isinstance(t2, TypeRef):
        unify_one(t1.inner_type, t2.inner_type, subst)
        return

    if isinstance(t1, TypeForAll) and isinstance(t2, TypeForAll):
        if t1.vars != t2.vars:
            raise TypeCheckError(
                ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
                f"Cannot unify {repr(t1)} with {repr(t2)}: different type variables"
            )
        unify_one(t1.body, t2.body, subst)
        return

    raise TypeCheckError(
        ERROR_UNEXPECTED_TYPE_FOR_EXPRESSION,
        f"Cannot unify {repr(t1)} with {repr(t2)}"
    )

def unify(constraints: List[Tuple[StellaType, StellaType]], subst: Dict[int, StellaType]) -> Dict[int, StellaType]:
    result = dict(subst)
    for t1, t2 in constraints:
        unify_one(t1, t2, result)
    return result
