from typing import Any, List

from .exceptions import FunctionArgsInvalid, FunctionNotFound


class FunctionExecutor:
    @staticmethod
    def execute(name: str, args: List[Any]):
        from table.functions.funcs import functions

        func = functions.get(name, None)
        if not func:
            raise FunctionNotFound()

        try:
            result = func(*args)
        except TypeError as e:
            raise FunctionArgsInvalid()
        else:
            return result
