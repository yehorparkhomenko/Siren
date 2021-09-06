from typing import List

from src.siren.user.model.user.user import User
from src.siren.app.repository.abstract_repository import AbstractRepository
from src.siren.app.value_object.id_value_object import Id


class UserRepository(AbstractRepository):
    def __init__(self):
        super().__init__()

    def add(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()
        self.session.commit()
        return user

    def get(self, model_id: Id) -> User:
        return self.session.query(User).get(model_id)

    def list(self) -> List[User]:
        return self.session.query(User).all()

    def update(self):
        self.session.flush()
        self.session.commit()

    def delete(self, model_id: Id):
        user = self.session.query(User).get(model_id)
        self.session.delete(user)
        self.session.commit()
        return user

