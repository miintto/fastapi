from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from app.common.response import APIResponse
from app.common.response.codes import Http2XX
from app.config.connections.database import db
from app.config.settings import get_settings
from app.config.settings.base import Settings
from .services import create_parent, get_parent
from .schemas import ParentCreate

router = APIRouter()


@router.get("")
async def sample(settings: Settings = Depends(get_settings)) -> APIResponse:
    data = {
        "BASE_DIR": settings.BASE_DIR,
        "APP_ENV": settings.APP_ENV,
        "DEBUG": settings.DEBUG
    }
    return APIResponse(Http2XX.SUCCESS, data)


@router.post("")
async def create_parent(
    body: ParentCreate, session: Session = Depends(db.session)
) -> APIResponse:
    return APIResponse(Http2XX.CREATED, create_parent(body, session))


@router.get("/{idx}")
def get_parent_by_id(
    idx: int, session: Session = Depends(db.session)
) -> APIResponse:
    return APIResponse(Http2XX.SUCCESS, get_parent(idx, session))

