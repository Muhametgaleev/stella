from __future__ import annotations
from typing import Optional, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from stella_types import StellaType

class TypeEnv:

    def __init__(self, bindings: Optional[Dict[str, "StellaType"]] = None):
        self._bindings: Dict[str, "StellaType"] = dict(bindings) if bindings else {}

    def extend(self, name: str, typ: "StellaType") -> "TypeEnv":
        new_bindings = dict(self._bindings)
        new_bindings[name] = typ
        return TypeEnv(new_bindings)

    def extend_many(self, bindings: Dict[str, "StellaType"]) -> "TypeEnv":
        new_bindings = dict(self._bindings)
        new_bindings.update(bindings)
        return TypeEnv(new_bindings)

    def lookup(self, name: str) -> Optional["StellaType"]:
        return self._bindings.get(name, None)

    def __repr__(self) -> str:
        return f"TypeEnv({self._bindings!r})"
