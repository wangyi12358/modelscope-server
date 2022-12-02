from typing import Union
from fastapi.responses import JSONResponse, Response
from fastapi import status


def response(*, code=200, data: Union[list, dict, str] = None, message="Success") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'message': message,
            'data': data,
        }
    )
