from fastapi import APIRouter, Body, Depends, HTTPException
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from app.utils.response import response
from app.utils.list import find_max, find
from app.utils.constant import BodyConst
from modelscope.outputs import OutputKeys
from typing import List
import math


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


# @router.get("/segmentation")
# async def text_segmentation(text: str = ""):
#   p = pipeline(task=Tasks.document_segmentation, model='damo/nlp_bert_document-segmentation_english-base')
#   result = p(documents=text)
#   return result


## 获取文本实体类型
@router.post("/entity")
async def entity(body=Body(None)):
  ner_pipeline = pipeline(task=Tasks.named_entity_recognition,
                          model='damo/nlp_raner_named-entity-recognition_english-large-ecom')
  result = ner_pipeline(body['inputContent'])
  res = []
  for item in result['output']:
    item["label"] = ECOM[item["type"]]
    res.append(item)
  return response(data=res)


# faq 相似度阈值
threshold = 0.1

@router.post("/faq")
async def faq(
  supports: List[object],
  inputContent: List[str]
):
  faq_pipeline = pipeline(Tasks.faq_question_answering, 'damo/nlp_structbert_faq-question-answering_chinese-base')
  outputs = faq_pipeline({
    "query_set": inputContent,
    "support_set": supports
  })
  res = []
  for answers in outputs['output']:
    print(answers)
    max_answer = answers[0]
    support = find(supports, "label", max_answer["label"])
    if support != None and max_answer['score'] > threshold:
      res.append(support['answer'])
    else:
      res.append("您说的什么？我听不懂")

  return response(data=res)


# 商品文案描述生成介绍
# https://modelscope.cn/models/damo/nlp_palm2.0_text-generation_commodity_chinese-base/summary
@router.post("/generate/product/desc")
async def generateProductDesc(body=Body(None)):
  text = body[BodyConst.input_content]
  text_generation_zh = pipeline(Tasks.text_generation, model='damo/nlp_palm2.0_text-generation_commodity_chinese-base')
  result_zh = text_generation_zh(text)
  return response(data=result_zh['text'])


# SPACE 端到端任务型对话生成模型介绍
# https://modelscope.cn/models/damo/nlp_space_dialog-modeling/summary
# todo 文档不全暂时不进行
@router.post("/dialog")
async def dialog(body=Body(None)):
  inputContent: List[str] = body[BodyConst.input_content]
  my_pipeline = pipeline("task-oriented-conversation", model='damo/nlp_space_dialog-modeling')
  result = {}
  for item in inputContent:
    result = my_pipeline({
      'user_input': item,
      'history': result
    })
  return response(data=result[OutputKeys.OUTPUT])
# 百科关系抽取模型介绍
# https://modelscope.cn/models/damo/nlp_bert_relation-extraction_chinese-base/summary

# 多语言中文摘要模型介绍
# https://modelscope.cn/models/ZhipuAI/Multilingual-GLM-Summarization-zh/summary

# 中英文翻译
# https://modelscope.cn/models/damo/nlp_csanmt_translation_en2zh/summary
@router.post("/translation")
async def translation():
  return response(data="ok")

# 情感分析
# https://modelscope.cn/models/damo/nlp_bert_sentiment-analysis_english-base/summary