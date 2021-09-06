from sqlalchemy.types import TypeDecorator, VARCHAR

from src.siren.app.value_object.description_value_object import Description


class DescriptionDecorator(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value_object: Description, dialect) -> str:
        if value_object is not None:
            return value_object.get_value()

    def process_result_value(self, value: str, dialect) -> Description:
        if value is not None:
            return Description(value)
