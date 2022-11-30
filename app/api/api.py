from fastapi import APIRouter
from app.api import text, image, oss

router = APIRouter()
router.include_router(text.router, tags=["text"], prefix="/text")
router.include_router(image.router, tags=["image"], prefix="/image")
router.include_router(oss.router, tags=["oss"], prefix="/oss")
