from fastapi import APIRouter, Body
from app.utils.constant import BodyConst
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys
from app.utils.response import response
from scipy.io.wavfile import write
from modelscope.models import Model
from app.utils.oss import upload_by_file_name

router = APIRouter()


# UniASR语音识别-中文英文混-通用-16k-离线
# https://modelscope.cn/models/damo/speech_UniASR_asr_2pass-cn-en-moe-16k-vocab8358-tensorflow1-offline/summary
@router.post("/auto_speech_recognition/uniasr")
async def auto_speech_recognition(inputContent: str = Body(embed=True)):
    text = inputContent
    inference_16k_pipline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='damo/speech_UniASR_asr_2pass-cn-en-moe-16k-vocab8358-tensorflow1-offline')
    rec_result = inference_16k_pipline(audio_in=text)
    return response(data=rec_result['text'])


# 语音合成-英式英文-通用领域
# https://modelscope.cn/models/damo/speech_sambert-hifigan_tts_en-gb_16k/summary
@router.post("/text_to_speech/speech_sambert_en")
async def text_to_speech(inputContent: str = Body(embed=True)):
    text = inputContent
    model_id = 'damo/speech_sambert-hifigan_tts_en-gb_16k'
    sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model=model_id)
    output = sambert_hifigan_tts(input=text)
    pcm = output[OutputKeys.OUTPUT_PCM]
    write('image/output.wav', 16000, pcm)
    url = upload_by_file_name("output.wav")
    return response(data=url)


# 语音合成-中文-多情感领域
# https://modelscope.cn/models/damo/speech_sambert-hifigan_tts_zh-cn_16k/summary
@router.post("/text_to_speech/speech_sambert_cn")
async def text_to_speech(inputContent: str = Body(embed=True)):
    text = inputContent
    model_id = 'damo/speech_sambert-hifigan_tts_zh-cn_16k'
    sambert_hifigan_tts = pipeline(task=Tasks.text_to_speech, model=model_id)
    output = sambert_hifigan_tts(input=text)
    pcm = output[OutputKeys.OUTPUT_PCM]
    write('image/output.wav', 16000, pcm)
    url = upload_by_file_name("output.wav")
    return response(data=url)
