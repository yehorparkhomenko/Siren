from __future__ import annotations

from src.siren.app.value_object.abstract_value_object import AbstractValueObject


class IntegerValueObject(AbstractValueObject):
    value = int

    def __init__(self, value: int) -> None:
        self.value = value

    def to_string(self) -> str:
        return str(self.value)

    def get_value(self) -> int:
        return self.value

    def is_equal_to(self, value: IntegerValueObject) -> bool:
        return self.get_value() == value.get_value()
