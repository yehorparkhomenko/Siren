from __future__ import annotations

from src.siren.app.value_object.abstract_value_object import AbstractValueObject


class StringValueObject(AbstractValueObject):
    value = str

    def __init__(self, value: str) -> None:
        self.value = value

    def to_string(self) -> str:
        return self.value

    def get_value(self) -> str:
        return self.value

    def is_equal_to(self, value: StringValueObject) -> bool:
        return self.get_value() == value.get_value()
