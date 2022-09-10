from datetime import timedelta
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = str(Path(__file__).parents[3])


class Settings(BaseSettings):
    """Settings 변수 관리 클래스

    개발 환경 분리를 위해 `pydantic` 라이브러리의 BaseSettings 모듈을 활용하였습니다.
    환경 변수에 선언된 값을 최우선으로 가져온 후, 루트 경로의 .env 파일을 읽어와 어플리케이션의
    설정 값으로 반영합니다.

    해당 설정 값은 어플리케이션이 실행될 때 최초 한 번 실행되며 `get_settings()` 메소드로
    불러올 수 있습니다.
    """

    BASE_DIR: str = BASE_DIR
    APP_ENV: str
    DEBUG: str

    SECRET_KEY: str

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    JWT_ACCESS_EXPIRED_INTERVAL: timedelta = timedelta(hours=12)
    JWT_REFRESH_EXPIRED_INTERVAL: timedelta = timedelta(days=180)

    class Config:
        env_file = ".env"
