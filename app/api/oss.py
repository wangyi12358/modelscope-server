from fastapi import APIRouter, File, UploadFile
from app.utils.response import response
from app.utils.oss import upload

router = APIRouter()

@router.post("/upload")
async def oss_upload(file: UploadFile = File()):
  url = await upload(file)
  return response(data=url)
