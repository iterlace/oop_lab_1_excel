from typing import List


def cols_generator(amount: int) -> List[str]:
    result = []
    for iteration in range(1, amount + 1):
        result.append(int_to_col(iteration))

    return result


def int_to_col(i: int) -> str:
    result = ""
    while i > 0:
        i, remainder = divmod(i - 1, 26)
        result = chr(65 + remainder) + result
    return result


def col_to_int(c: str) -> int:
    for i in range(0, 1000):
        i_col = int_to_col(i)
        if c == i_col:
            return i
    raise ValueError(f"\"{c}\" is an invalid column!")


def rows_generator(amount: int) -> List[str]:
    result = []
    for iteration in range(1, amount + 1):
        result.append(str(iteration))
    return result
