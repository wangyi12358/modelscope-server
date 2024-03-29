from fastapi import APIRouter, Body
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys
from app.utils.response import response
from app.utils.image import crop
from app.utils.file import save_file, get_suffix
from app.utils.oss import upload_by_file_name
import cv2
import os
import random

router = APIRouter()


class ImageRequest:
    image: str = ""


# 获取图片类目
# https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/bird.JPEG
@router.post("/image/category")
async def image_category(body=Body(None)):
    image_classification = pipeline(Tasks.image_classification,
                                    model='damo/cv_vit-base_image-classification_Dailylife-labels')
    result = image_classification(body['inputContent'])
    res = []
    scores = result.get("scores")
    labels = result.get("labels")
    for index, score in enumerate(scores):
        obj = {
            'label': labels[index],
            'score': str(score)
        }
        res.append(obj)
    return response(data=res)


# 获取图片文字
@router.post("/image/words")
async def image_words(body=Body(None)):
    image = body['inputContent']
    ocr_detection = pipeline(Tasks.ocr_detection, model='damo/cv_resnet18_ocr-detection-line-level_damo')
    result = ocr_detection(image)
    file_path = save_file("image", "words_image", image)
    # 获取的文字对象
    text = []
    for polygon in result['polygons']:
        suffix = get_suffix(image)
        save_file_path = 'image/crop.{0}'.format(suffix)
        # 裁剪图片
        crop(polygon, file_path, save_file_path)
        # 上传裁剪图片
        # file_url = await upload_by_file_name("crop.jpg")
        ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-general_damo')
        # 根据图片链接获取文字文本
        img = cv2.imread(save_file_path)
        text_result = ocr_recognition(img)
        text.append(text_result['text'])
    # 获取到四个点的xy轴
    return response(data=text)


@router.post("/image/getText")
async def image_get_text(body=Body(None)):
    image = body['inputContent']
    ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-general_damo')
    # 根据图片链接获取文字文本
    # img = cv2.imread(image)
    text_result = ocr_recognition(image)
    return response(data=text_result['text'])



# 根据人像图片获取3d图片
@router.post("/image/cartoon/3d")
async def cartoon_3d(body=Body(None)):
    image = body['inputContent']
    img_cartoon = pipeline(Tasks.image_portrait_stylization,
                           model='damo/cv_unet_person-image-cartoon-3d_compound-models')
    result = img_cartoon(image)
    cv2.imwrite('image/cartoon_3d.png', result[OutputKeys.OUTPUT_IMG])
    # 下面是上传到oss
    url = upload_by_file_name("cartoon_3d.png")
    return response(data=url)


# 获取视频商品类目
@router.post("/video/category")
async def video_category(body=Body(None)):
    video_url = body['inputContent']
    os.system('wget -O video_category.mp4 {0}'.format(video_url))
    category_pipeline = pipeline(
        Tasks.live_category, model='damo/cv_resnet50_live-category')
    result = category_pipeline('video_category.mp4')
    scores = result.get("scores")
    labels = result.get("labels")
    res = []
    for index, score in enumerate(scores):
        obj = {}
        obj['label'] = labels[index]
        obj['score'] = str(score)
        res.append(obj)
    return response(data=res)


# 获取短视频的类目
@router.post("/short/video/category")
async def short_video_category(body=Body(None)):
    video_url = body['inputContent']
    os.system('wget -O short_video_category.mp4 {0}'.format(video_url))
    category_pipeline = pipeline(
        Tasks.video_category, model='damo/cv_resnet50_video-category')
    result = category_pipeline('short_video_category.mp4')
    scores = result.get("scores")
    labels = result.get("labels")
    res = []
    for index, score in enumerate(scores):
        obj = {}
        obj['label'] = labels[index]
        obj['score'] = str(score)
        res.append(obj)
    return response(data=res)


# 人脸生成
# https://modelscope.cn/models/damo/cv_gan_face-image-generation/summary
@router.post("/generation/face")
async def generation_face(
        matting: bool = Body(embed=True, default=True)
):
    random_num = random.randint(0, 100000)
    face_generation = pipeline(Tasks.face_image_generation, model='damo/cv_gan_face-image-generation')
    result = face_generation(random_num)
    cv2.imwrite('image/face.png', result[OutputKeys.OUTPUT_IMG])
    # 下面是上传到oss
    url = upload_by_file_name("face.png")
    if matting:
        # 下面去扣掉背景图
        portrait_matting = pipeline(Tasks.portrait_matting, model='damo/cv_unet_image-matting')
        result = portrait_matting(url)
        cv2.imwrite('image/face.png', result[OutputKeys.OUTPUT_IMG])
        # 下面是把扣好的图上传到oss
        url = upload_by_file_name("face.png")
    return response(data=url)


# https://modelscope.cn/models/damo/cv_diffusion_text-to-image-synthesis/summary
# 根据文字描述生成文案
@router.post("/image/synthesis")
async def image_synthesis(
        inputContent: str = Body(embed=True)
):
    synthesis_pipeline = pipeline(Tasks.text_to_image_synthesis, model='damo/cv_diffusion_text-to-image-synthesis')
    result = synthesis_pipeline(inputContent)
    cv2.imwrite('image/image_synthesis.png', result[OutputKeys.OUTPUT_IMG])
    # 下面是上传到oss
    url = upload_by_file_name("image_synthesis.png")
    return response(data=url)


# https://modelscope.cn/models/damo/cv_unet_person-image-cartoon_compound-models/summary
# 生成卡通化
@router.post("/image/cartoon")
async def image_cartoon(
        inputContent: str = Body(embed=True)
):
    img_cartoon = pipeline(Tasks.image_portrait_stylization, model='damo/cv_unet_person-image-cartoon_compound-models')
    result = img_cartoon(inputContent)
    cv2.imwrite('image/image_cartoon.png', result[OutputKeys.OUTPUT_IMG])
    # 下面是上传到oss
    url = upload_by_file_name("image_cartoon.png")
    return response(data=url)
