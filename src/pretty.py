from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stella_types import StellaType

def pretty_type(t: "StellaType") -> str:
    return repr(t)

def pretty_expr(ctx) -> str:
    if ctx is None:
        return "<none>"
    try:
        from antlr4 import Interval
        start = ctx.start
        stop = ctx.stop
        if start is not None and stop is not None:
            input_stream = start.getInputStream()
            if input_stream is not None:
                text = input_stream.getText(Interval(start.start, stop.stop))
                if text:
                    return text
    except Exception:
        pass

    try:
        return ctx.getText()
    except Exception:
        pass

    return "<expr>"
