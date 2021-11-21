import json
import logging
from typing import Dict, List

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
            for row_name, col in zip(table.rows, table.formula_matrix):
                for col_name, value in zip(table.cols, col):
                    if not value:
                        continue
                    cell = col_name + row_name
                    serialized[cell] = value

            with open(filename, "w+") as f:
                f.write(json.dumps(serialized))
        except Exception as e:
            logger.exception(f"Error saving table to {filename}")
            raise SerializationError("Unknown error")
