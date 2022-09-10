from .base import Settings


class LocalSettings(Settings):
    DEBUG: bool = True

    class Config:
        env_file = (".env.local", ".env")
