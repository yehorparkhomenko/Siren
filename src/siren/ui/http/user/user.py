from fastapi import APIRouter, HTTPException
from src.siren.user.repository.user_repository import UserRepository
from src.siren.app.value_object.id_value_object import Id
from src.siren.app.value_object.name_value_object import Name
from src.siren.app.value_object.description_value_object import Description
from src.siren.app.value_object.age_value_object import Age
from src.siren.user.model.user.user import User
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
userRepository = UserRepository()


class UserDto(BaseModel):
    name: str
    description: Optional[str] = None
    age: Optional[int] = None


@router.post("/user")
def create(userDto: UserDto):
    user = userRepository.add(
        User(
            Name(userDto.name),
            None if userDto.description is None else Description(userDto.description),
            None if userDto.age is None else Age(userDto.age)
        )
    )

    return {
        'id': user.id.value,
        'name': user.name.value,
        'description': None if user.description is None else user.description.value,
        'age': None if user.age is None else user.age.value
    }


@router.get("/user")
def index() -> list:
    users = userRepository.list()
    return list(
        map(
            lambda user:
            {
                'id': user.id.value,
                'name': user.name.value,
                'description': None if user.description is None else user.description.value,
                'age': None if user.age is None else user.age.value
            }, users
        )
    )


@router.get("/user/{id}")
def view(id: int):
    user = userRepository.get(Id(id))

    if user is None:
        raise HTTPException(status_code=404, detail="Not found")

    return {
        'id': user.id.value,
        'name': user.name.value,
        'description': None if user.description is None else user.description.value,
        'age': None if user.age is None else user.age.value
    }


@router.patch("/user/{id}")
def update(id: int, userDto: UserDto):
    user = userRepository.get(Id(id))

    if user is None:
        raise HTTPException(status_code=404, detail="Not found")

    user.name = Name(userDto.name)
    user.description = None if userDto.description is None else Description(userDto.description)
    user.age = None if userDto.age is None else Age(userDto.age)
    userRepository.update()

    return {
        'id': user.id.value,
        'name': user.name.value,
        'description': None if user.description is None else user.description.value,
        'age': None if user.age is None else user.age.value
    }


@router.delete("/user/{id}")
def delete(id):
    try:
        user = userRepository.delete(Id(id))
    except:
        raise HTTPException(status_code=404, detail="Not found")

    return {
        'id': user.id.value,
        'name': user.name.value,
        'description': None if user.description is None else user.description.value,
        'age': None if user.age is None else user.age.value
    }
