from typing import NewType, Tuple, Union

Formula = str
CalculationError = NewType("CalculationError", None)
CalculatedValue = Union[float, int, bool, None, CalculationError]

CellRef = Tuple[str, str]
CellIdx = Tuple[int, int]
Number = Union[int, float]
