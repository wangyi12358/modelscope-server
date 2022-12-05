from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

router = APIRouter()

# 挂载模版文件夹
tmp = Jinja2Templates(directory='templates')

@router.get('/')
async def get_html(request: Request):
    return tmp.TemplateResponse(
        'index.html',
        {'request': request}
    )