from typing import NewType, Tuple, Union

Formula = str
CalculationError = NewType("CalculationError", None)
CalculatedValue = Union[float, int, bool, None, CalculationError]

# CellRef must be either a string like "E12"
#   or a tuple (col: int, row: int)
CellRef = Union[str, Tuple[str, str]]
CellIdx = Tuple[int, int]
Number = Union[int, float]
