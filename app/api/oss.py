from fastapi import APIRouter, File
from app.utils.response import response

router = APIRouter()

router.post("/upload")
async def upload(file: bytes = File()):
  return response(data=len(file))