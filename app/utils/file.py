import requests


# 获取文件后缀名
def get_suffix(url: str):
  heft = url.split('?')[0]
  array = heft.split('.')
  return array[-1]


# 保存文件到本地
def save_file(path: str, file_name: str, url: str):
  res = requests.get(url)
  res.raise_for_status()
  file_path = path + "/" + file_name + '.' + get_suffix(url)
  with open(file_path, 'wb') as f:
    f.write(res.content)
    f.close()
  return file_path
