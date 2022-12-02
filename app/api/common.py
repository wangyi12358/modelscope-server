from fastapi import APIRouter
from app.utils.response import response
from app.utils.modelscope import domain

router = APIRouter()


@router.get("/domain")
async def get_domain():
    return response(data=domain)
