import logging.config

from fastapi import FastAPI

from app.api.auth.controllers import router as router_auth
from app.api.sample.controllers import router as router_sample
from app.api.user.controllers import router as router_user
from app.config.connections.database import db
from app.config.loggings.config import logging_config
from app.config.middlewares.logging_middleware import LoggingMiddleware
from app.common.exceptions.exception_handlers import exception_handlers
from app.common.response import APIResponse


def create_app():
    """FastAPI Application"""

    app = FastAPI(
        default_response_class=APIResponse,
        exception_handlers=exception_handlers,
    )

    # Logging
    logging.config.dictConfig(logging_config)

    # Connection
    db.init_app(app)

    # Middlewares
    app.add_middleware(LoggingMiddleware)

    # Routers
    app.include_router(router_auth, prefix="/auth")
    app.include_router(router_sample, prefix="/test")
    app.include_router(router_user, prefix="/user")

    return app
