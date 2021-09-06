from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def index_action():
    return {"Hello": "World"}