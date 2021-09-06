from sqlalchemy.types import TypeDecorator, INTEGER
from typing import Optional

from src.siren.app.value_object.id_value_object import Id


class IdDecorator(TypeDecorator):
    impl = INTEGER

    def process_bind_param(self, value_object: Optional[Id], dialect) -> Optional[int]:
        return None if value_object is None else value_object.get_value()

    def process_result_value(self, value: Optional[int], dialect) -> Optional[Id]:
        return None if value is None else Id(value)
