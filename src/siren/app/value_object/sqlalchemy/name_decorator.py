from sqlalchemy.types import TypeDecorator, VARCHAR

from src.siren.app.value_object.name_value_object import Name


class NameDecorator(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value_object: Name, dialect) -> str:
        if value_object is not None:
            return value_object.get_value()

    def process_result_value(self, value: str, dialect) -> Name:
        if value is not None:
            return Name(value)
