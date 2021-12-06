import json
import logging
from typing import Dict, List

from .utils import col_to_int, cols_generator, rows_generator
from .table import Table

logger = logging.getLogger(__name__)


class SerializationError(Exception):
    def __init__(self, msg: str):
        self.message = msg
        super(SerializationError, self).__init__(self.message)


class DeserializationError(Exception):
    def __init__(self, msg: str):
        self.message = msg
        super(DeserializationError, self).__init__(self.message)


class Serializer:
    @classmethod
    def load(cls, filename: str, cols: List[str], rows: List[str]) -> Table:
        try:
            with open(filename, "r") as f:
                serialized = json.loads(f.read())

            # Determine table dimensions
            col_max = 1
            row_max = 1
            for cell, _ in serialized.items():
                col, row = Table.parse_cell_ref(cell)
                row = int(row)
                col_idx = col_to_int(col)

                row_max = max(row_max, row)
                col_max = max(col_max, col_idx)

            # Build a table
            cols = cols_generator(col_max+1)
            rows = rows_generator(row_max+1)
            table = Table(cols, rows)
            for cell, formula in serialized.items():
                try:
                    col, row = table.cell_index(cell)
                except ValueError:
                    continue
                    # raise DeserializationError(
                    #     f'Cell "{cell}" isn\'t present in the table! It either '
                    #     f"has invalid format or goes out of table bounds."
                    # )
                table.set(col, row, formula)
            return table
        except Exception as e:
            logger.exception(f"Error loading table from {filename}")
            raise DeserializationError("Unknown error")

    @classmethod
    def save(cls, table: Table, filename: str) -> None:
        try:
            serialized: Dict[str, str] = {}
            for col_name, row in zip(table.cols, table.formula_matrix):
                for row_name, value in zip(table.rows, row):
                    if not value:
                        continue
                    cell = col_name + row_name
                    serialized[cell] = value

            with open(filename, "w+") as f:
                f.write(json.dumps(serialized))
        except Exception as e:
            logger.exception(f"Error saving table to {filename}")
            raise SerializationError("Unknown error")
