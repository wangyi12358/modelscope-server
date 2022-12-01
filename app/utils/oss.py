from fastapi import UploadFile
import oss2

accessKeyId = 'LTAI5tPDUruA4n5GtnsYiJCZ'
accessKeySecret = 'APssOoePKC4utUv0eXuT2srJu9WWa1'
endpoint = 'oss-cn-chengdu.aliyuncs.com'
bucket_name = 'zbanx-banker-image'
auth = oss2.Auth(accessKeyId, accessKeySecret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

def get_url_by_file_path(file_path: str):
  return 'https://' + bucket_name + '.' + endpoint + '/' + file_path

async def upload(file: UploadFile):
  file_path = 'image/' + file.filename
  content = await file.read()
  result = bucket.put_object(file_path, data=content)
  if result.status == 200:
    return get_url_by_file_path(file_path)

async def upload_by_file_name(file_name: str = ""):
  file_path = 'image/' + file_name
  result = bucket.put_object(file_path, file_path)
  if result.status == 200:
    return get_url_by_file_path(file_path)
