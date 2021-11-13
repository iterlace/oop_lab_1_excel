from typing import List, Tuple, Dict, Any, Optional
import json

from .table import Table


class Serializer:

    @classmethod
    def load(cls, filename: str, cols: List[str], rows: List[str]) -> Table:
        with open(filename, "r") as f:
            serialized = json.loads(f.read())
        table = Table(cols, rows)
        for cell, formula in serialized.items():
            h, w = table.cell_index(cell)
            table.set(h, w, formula)
        return table

    @classmethod
    def save(cls, table: Table, filename: str) -> None:
        serialized: Dict[str, str] = {}
        for row_name, col in zip(table.rows, table.formula_matrix):
            for col_name, value in zip(table.cols, col):
                if not value:
                    continue
                cell = col_name+row_name
                serialized[cell] = value

        with open(filename, "w+") as f:
            f.write(json.dumps(serialized))
