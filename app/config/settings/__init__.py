import os
from functools import lru_cache

from .local import LocalSettings
from .development import DevSettings
from .production import ProdSettings


__all__ = ["get_settings"]


_settings = {
    "local": LocalSettings,
    "development": DevSettings,
    "production": ProdSettings,
}


@lru_cache()
def get_settings():
    env = os.environ.get("APP_ENV", "local")
    print(f"APP_ENV:\t {env}")
    settings = _settings[env]
    return settings()
