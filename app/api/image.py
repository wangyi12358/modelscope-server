from fastapi import APIRouter
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from app.utils.response import response
from app.utils.image import crop
from app.utils.oss import upload_by_file_name
from app.utils.file import save_file

router = APIRouter()


# 获取图片类目
# https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/bird.JPEG
@router.get("/category")
async def image_category(image: str = ""):
  image_classification = pipeline(Tasks.image_classification,
                                  model='damo/cv_vit-base_image-classification_Dailylife-labels')
  result = image_classification(image)
  res = []
  scores = result.get("scores")
  labels = result.get("labels")
  for index, score in enumerate(scores):
    obj = {}
    obj['label'] = labels[index]
    obj['score'] = str(score)
    res.append(obj)
  return response(data=res)



data = [
  [
    220,  # x1
    14,  # y1
    780,
    14,
    780,
    64,
    220,
    64
  ],
  [
    196,
    369,
    604,
    370,
    604,
    425,
    196,
    425
  ],
  [
    21,
    730,
    425,
    731,
    425,
    787,
    21,
    786
  ],
  [
    421,
    731,
    782,
    731,
    782,
    789,
    421,
    789
  ],
  [
    0,
    121,
    109,
    0,
    147,
    35,
    26,
    159
  ],
  [
    697,
    160,
    773,
    160,
    773,
    197,
    697,
    198
  ],
  [
    547,
    205,
    623,
    205,
    623,
    244,
    547,
    244
  ],
  [
    548,
    161,
    623,
    161,
    623,
    199,
    547,
    199
  ],
  [
    698,
    206,
    772,
    206,
    772,
    244,
    698,
    244
  ]
]

# 获取图片文字
@router.get("/words")
async def image_words(image: str = ""):
  ocr_detection = pipeline(Tasks.ocr_detection, model='damo/cv_resnet18_ocr-detection-line-level_damo')
  result = ocr_detection(image)
  print(result)
  file_path = save_file("image", "words_image", image)
  # 获取的文字对象
  text = []
  for polygon in result:
    save_file_path = 'image/crop.jpg'
    # 裁剪图片
    crop(polygon, file_path, save_file_path)
    # 上传裁剪图片
    file_url = await upload_by_file_name("crop.jpg")
    ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-general_damo')
    # 根据图片链接获取文字文本
    text_result = ocr_recognition(file_url)
    print(text_result)
    text.append(text_result['text'])
  # 获取到四个点的xy轴
  return response(data=text)


@router.get("/test")
async def image_test():
  crop(data[4])
  url = await upload_by_file_name("crop.jpg")
  return url
