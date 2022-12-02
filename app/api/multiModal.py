from fastapi import APIRouter, Body
from app.utils.constant import BodyConst
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys
from app.utils.response import response

router = APIRouter()


# 根据图片获取文字说明 (偏电商中文)
@router.post("/image/caption")
async def image_caption(body=Body(None)):
  image = body[BodyConst.input_content]
  img_captioning = pipeline(Tasks.image_captioning, model='damo/ofa_image-caption_muge_base_zh')
  result = img_captioning(image)
  return response(data=result[OutputKeys.CAPTION])
