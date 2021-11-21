from typing import List
import string


def cols_generator(amount: int) -> List[str]:
    result = []
    for iteration in range(1, amount+1):
        result.append(int_to_col(iteration))

    return result


def int_to_col(i: int) -> str:
    result = ""
    while i > 0:
        i, remainder = divmod(i - 1, 26)
        result = chr(65 + remainder) + result
    return result


def rows_generator(amount: int) -> List[str]:
    result = []
    for iteration in range(1, amount+1):
        result.append(str(iteration))
    return result
