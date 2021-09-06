FROM python:3.9

WORKDIR /Siren
COPY . .
RUN pip install poetry
RUN poetry install
CMD poetry run uvicorn
