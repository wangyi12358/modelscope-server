from fastapi import APIRouter
from app.api import nlp, cv, oss, multiModal, common

router = APIRouter()
router.include_router(nlp.router, tags=["nlp"], prefix="/nlp")
router.include_router(cv.router, tags=["cv"], prefix="/cv")
router.include_router(oss.router, tags=["oss"], prefix="/oss")
router.include_router(multiModal.router, tags=["multiModal"], prefix="/multi/modal")
router.include_router(common.router, tags=["common"], prefix="/common")
