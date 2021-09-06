from typing import Optional

from sqlalchemy import Column
from src.siren.app.value_object.sqlalchemy.id_decorator import IdDecorator
from src.siren.app.value_object.sqlalchemy.name_decorator import NameDecorator
from src.siren.app.value_object.sqlalchemy.description_decorator import DescriptionDecorator
from src.siren.app.value_object.sqlalchemy.age_decorator import AgeDecorator
from src.siren.app.value_object.id_value_object import Id
from src.siren.app.value_object.name_value_object import Name
from src.siren.app.value_object.description_value_object import Description
from src.siren.app.value_object.age_value_object import Age
from src.siren.config.db import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(IdDecorator, primary_key=True, index=True)
    name = Column(NameDecorator)
    description = Column(DescriptionDecorator)
    age = Column(AgeDecorator)

    def __init__(self, name: Name, description: Optional[Description], age: Optional[Age]):
        self.name = name
        self.description = description
        self.age = age

    def __init__(self, id: Id, name: Name, description: Optional[Description], age: Optional[Age]):
        self.id = id
        self.name = name
        self.description = description
        self.age = age

    def get_id(self) -> Id:
        return self.id

    def get_name(self) -> Name:
        return self.name

    def get_description(self) -> Optional[Description]:
        return self.description

    def get_age(self) -> Optional[Age]:
        return self.age
