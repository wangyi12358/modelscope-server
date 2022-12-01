from fastapi import APIRouter, File, UploadFile
from app.utils.response import response
from app.utils.oss import upload
from app.utils.alioss import get_token

router = APIRouter()

@router.post("/upload")
async def oss_upload(file: UploadFile = File()):
  url = await upload(file)
  return response(data=url)

@router.get("/sign")
async def oss_sign():
  token = get_token()
  return response(data=token)
