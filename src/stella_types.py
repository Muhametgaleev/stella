from __future__ import annotations
from typing import List, Optional, Tuple

class StellaType:

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError

class TypeBool(StellaType):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "Bool"

    def __eq__(self, other) -> bool:
        return isinstance(other, TypeBool)

    def __hash__(self) -> int:
        return hash("Bool")

class TypeNat(StellaType):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "Nat"

    def __eq__(self, other) -> bool:
        return isinstance(other, TypeNat)

    def __hash__(self) -> int:
        return hash("Nat")

class TypeUnit(StellaType):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "Unit"

    def __eq__(self, other) -> bool:
        return isinstance(other, TypeUnit)

    def __hash__(self) -> int:
        return hash("Unit")

class TypeFun(StellaType):
    def __init__(self, param_types: List[StellaType], return_type: StellaType):
        self.param_types = list(param_types)
        self.return_type = return_type

    def __repr__(self) -> str:
        params = ", ".join(repr(t) for t in self.param_types)
        return f"fn({params}) -> {repr(self.return_type)}"

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, TypeFun)
            and self.param_types == other.param_types
            and self.return_type == other.return_type
        )

    def __hash__(self) -> int:
        return hash(("Fun", tuple(self.param_types), self.return_type))

class TypeTuple(StellaType):
    def __init__(self, types: List[StellaType]):
        self.types = list(types)

    def __repr__(self) -> str:
        return "{" + ", ".join(repr(t) for t in self.types) + "}"

    def __eq__(self, other) -> bool:
        return isinstance(other, TypeTuple) and self.types == other.types

    def __hash__(self) -> int:
        return hash(("Tuple", tuple(self.types)))

class TypeRecord(StellaType):
    def __init__(self, fields: List[Tuple[str, StellaType]]):
        self.fields = list(fields)

    def __repr__(self) -> str:
        parts = ", ".join(f"{label} : {repr(t)}" for label, t in self.fields)
        return "{" + parts + "}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, TypeRecord):
            return False
        return dict(self.fields) == dict(other.fields)

    def __hash__(self) -> int:
        return hash(("Record", tuple(sorted(self.fields))))

    def get_field(self, label: str) -> Optional[StellaType]:
        for lbl, t in self.fields:
            if lbl == label:
                return t
        return None

class TypeSum(StellaType):
    def __init__(self, left: StellaType, right: StellaType):
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{repr(self.left)} + {repr(self.right)}"

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, TypeSum)
            and self.left == other.left
            and self.right == other.right
        )

    def __hash__(self) -> int:
        return hash(("Sum", self.left, self.right))

class TypeList(StellaType):
    def __init__(self, element_type: StellaType):
        self.element_type = element_type

    def __repr__(self) -> str:
        return f"[{repr(self.element_type)}]"

    def __eq__(self, other) -> bool:
        return isinstance(other, TypeList) and self.element_type == other.element_type

    def __hash__(self) -> int:
        return hash(("List", self.element_type))

class TypeVariant(StellaType):
    def __init__(self, fields: List[Tuple[str, Optional[StellaType]]]):
        self.fields = list(fields)

    def __repr__(self) -> str:
        parts = []
        for label, t in self.fields:
            if t is not None:
                parts.append(f"{label} : {repr(t)}")
            else:
                parts.append(label)
        return "<|" + ", ".join(parts) + "|>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, TypeVariant):
            return False
        return dict(self.fields) == dict(other.fields)

    def __hash__(self) -> int:
        return hash(("Variant", tuple(sorted((k, v) for k, v in self.fields))))

    def get_field(self, label: str) -> Optional[Optional[StellaType]]:
        for lbl, t in self.fields:
            if lbl == label:
                return (True, t)
        return (False, None)

BOOL = TypeBool()
NAT = TypeNat()
UNIT = TypeUnit()
