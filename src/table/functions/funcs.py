from table.types import Number


def _max(left: Number, right: Number) -> Number:
    return max(left, right)


def _min(left: Number, right: Number) -> Number:
    return min(left, right)


functions = {
    "max": _max,
    "min": _min,
}
