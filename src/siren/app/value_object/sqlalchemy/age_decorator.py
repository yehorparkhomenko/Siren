from sqlalchemy.types import TypeDecorator, VARCHAR

from src.siren.app.value_object.age_value_object import Age


class AgeDecorator(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value_object: Age, dialect) -> int:
        if value_object is not None:
            return value_object.get_value()

    def process_result_value(self, value: int, dialect) -> Age:
        if value is not None:
            return Age(value)
