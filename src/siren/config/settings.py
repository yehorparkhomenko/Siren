from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Siren"
    MYSQL_USER: str = "user"
    MYSQL_PASS: str = "password"
    MYSQL_HOST: str = "192.168.88.231"
    #MYSQL_PORT: str = "33060"
    MYSQL_PORT: str = "3306"
    MYSQL_DB: str = "siren"


settings = Settings()
