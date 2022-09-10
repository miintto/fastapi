from enum import Enum
from typing import Any

from fastapi.responses import JSONResponse

from app.common.response.formats import send_format


class APIResponse(JSONResponse):
    def __init__(self, code: Enum, data: Any = None, **kwargs) -> None:
        super().__init__(
            content=send_format(code.value[0], code.value[1], data), 
            status_code=code.value[2], 
            **kwargs
        )
