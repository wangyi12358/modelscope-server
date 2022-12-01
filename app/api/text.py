from fastapi import APIRouter, Body, Depends, HTTPException
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from app.utils.response import response

router = APIRouter()

ECOM = {
  "AUX": "宽泛的名词",
  "AUX&PRODUCT": "宽泛的名词&产品",
  "BRAND": "品牌",
  "COLOR": "颜色",
  "CONJ": "连词",
  "CROWD": "对象",
  "IP": "IP",
  "LOCATION": "地点",
  "MAIN_BRAND": "主品牌",
  "MATERIAL": "材质",
  "MEASUREMENT": "度量值",
  "MEASUREMENT&PRODUCT": "度量值&产品",
  "MODEL": "型号",
  "OBJECT_PRODUCT": "产品修饰词",
  "OCCASION": "适用场景",
  "PATTERN": "图案",
  "PREP": "介词",
  "PRODUCT": "产品词",
  "SHAPE": "形状",
  "SHOP": "店铺",
  "STOP": "停用词",
  "STYLE": "风格",
  "TIME": "时间",
}


@router.get("/segmentation")
async def text_segmentation(text: str = ""):
  p = pipeline(task=Tasks.document_segmentation, model='damo/nlp_bert_document-segmentation_english-base')
  result = p(documents=text)
  return result


## 获取文本实体类型
@router.get("/entity")
async def entity(text: str = ""):
  ner_pipeline = pipeline(task=Tasks.named_entity_recognition,
                          model='damo/nlp_raner_named-entity-recognition_english-large-ecom')
  result = ner_pipeline(text)
  res = []
  print(result)
  for item in result['output']:
    item["label"] = ECOM[item["type"]]
    res.append(item)
  return response(data=res)
