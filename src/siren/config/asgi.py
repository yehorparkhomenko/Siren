import uvicorn
from src.siren.entry.main import get_app


def run():
    app = get_app()
    uvicorn.run(app)
