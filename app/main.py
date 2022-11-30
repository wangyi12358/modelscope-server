from fastapi import FastAPI
from app.api.api import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


def get_application() -> FastAPI:
  origins = [
    "http://local.zbanx.com",
    "https://local.tbanx.com",
    "http://localhost:8000/",
    "http://127.0.0.1:8000/"
  ]
  application = FastAPI()

  application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins,  # 允许访问的源
    # allow_origins=origins,  # 允许访问的源
    # allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
  )
  application.include_router(router, prefix="/api")

  return application


app = get_application()

if __name__ == '__main__':
  # 服务端端口是 8080！
  uvicorn.run(app="app.main:app", reload=True, host="192.168.1.107", port=8000)
