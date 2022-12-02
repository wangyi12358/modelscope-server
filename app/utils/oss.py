from fastapi import UploadFile
import oss2

access_key_id = 'LTAI5tPDUruA4n5GtnsYiJCZ'
access_key_secret = 'APssOoePKC4utUv0eXuT2srJu9WWa1'
endpoint = 'oss-cn-chengdu.aliyuncs.com'
bucket_name = 'zbanx-banker-image'
auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)
role_arn = "acs:ram::1786718467325799:role/aliyunossrole"


def get_url_by_file_path(file_path: str):
  return 'https://' + bucket_name + '.' + endpoint + '/' + file_path


async def upload(file: UploadFile):
  file_path = 'image/' + file.filename
  content = await file.read()
  result = bucket.put_object(file_path, data=content)
  if result.status == 200:
    return get_url_by_file_path(file_path)


def upload_by_file_name(file_name: str = ""):
  file_path = 'image/' + file_name
  # result = bucket.put_object(file_path, file_path)
  with open(file_path, 'rb') as fileobj:
    # Tell方法用于返回当前位置。
    current = fileobj.tell()
    # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
    result = bucket.put_object(file_path, fileobj)
    if result.status == 200:
      return get_url_by_file_path(file_path)
  # if result.status == 200:
  #   return get_url_by_file_path(file_path)
