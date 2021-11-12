from typing import Union, List, Tuple, Optional, Any, Final, NewType, TypeVar

Formula = str
CalculationError = NewType("CalculationError", None)
CalculatedValue = Union[float, int, bool, None, CalculationError]

CellRef = Tuple[str, str]
CellIdx = Tuple[int, int]
Number = Union[int, float]
