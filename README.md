# ai-server使用文档

## 打包docker镜像
```shell
$ docker-compose -f ./docker-compose.yaml build --force-rm ai-server
```

## 启动镜像
```shell
$ docker-compose -f ./docker-compose.yaml up --force-recreate -d ai-server
```