# ai-server使用文档

## 打包docker镜像
```shell
$ docker-compose -f ./docker-compose.yml build --force-rm ai-server
```

## 启动镜像
```shell
$ docker run -d --gpus all --name ai-server -v /nv/projects/modelscope:/app -v /root/.cache/modelscope:/mnt/workspace/.cache/modelscope  -p 8000:8000 ai-server
$ docker-compose -f ./docker-compose.yml up --force-recreate -d ai-server
```