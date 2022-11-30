import oss2

accessKeyId = ''
accessKeySecret = ''
endpoint = 'oss-cn-chengdu.aliyuncs.com'
bucket = 'zbanx-banker-image'


def upload(file):
  auth = oss2.Auth('yourAccessKeyId', 'yourAccessKeySecret')
  bucket = oss2.Bucket(auth, endpoint, 'examplebucket')
  file_path = '/image/' + file.filename
  result = bucket.put_object(file_path, file)
  if result.status == 200:
    file_url = bucket.sign_url("GET", file_path, 60)
    return file_url
