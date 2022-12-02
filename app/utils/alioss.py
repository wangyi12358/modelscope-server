import socket
import base64
import time
import datetime
import json
import hmac
from hashlib import sha1 as sha
from app.utils.oss import access_key_id, access_key_secret, bucket_name, endpoint
from app.utils.constant import OssConst

# 填写Host地址，格式为https://bucketname.endpoint。
host = 'https://{0}.{1}'.format(bucket_name, endpoint)
# 设置上传回调URL，即回调服务器地址，用于处理应用服务器与OSS之间的通信。OSS会在文件上传完成后，把文件上传信息通过此回调URL发送给应用服务器。
callback_url = "https://192.168.0.0:8888"
# 设置上传到OSS文件的前缀，可置空此项。置空后，文件将上传至Bucket的根目录下。
upload_dir = OssConst.oss_prefix
expire_time = 30


def get_iso_8601(expire):
  gmt = datetime.datetime.utcfromtimestamp(expire).isoformat()
  gmt += 'Z'
  return gmt


def get_token():
  now = int(time.time())
  expire_syncpoint = now + expire_time
  expire = get_iso_8601(expire_syncpoint)

  policy_dict = {}
  policy_dict['expiration'] = expire
  condition_array = []
  array_item = []
  array_item.append('starts-with')
  array_item.append('$key')
  array_item.append(upload_dir)
  condition_array.append(array_item)
  policy_dict['conditions'] = condition_array
  policy = json.dumps(policy_dict).strip()
  policy_encode = base64.b64encode(policy.encode())
  h = hmac.new(access_key_secret.encode(), policy_encode, sha)
  sign_result = base64.encodestring(h.digest()).strip()

  callback_dict = {}
  callback_dict['callbackUrl'] = callback_url
  callback_dict['callbackBody'] = 'filename=${object}&size=${size}&mimeType=${mimeType}' \
                                  '&height=${imageInfo.height}&width=${imageInfo.width}'
  callback_dict['callbackBodyType'] = 'application/x-www-form-urlencoded'
  callback_param = json.dumps(callback_dict).strip()
  base64_callback_body = base64.b64encode(callback_param.encode())

  token_dict = {}
  token_dict['OSSAccessKeyId'] = access_key_id
  token_dict['host'] = host
  token_dict['policy'] = policy_encode.decode()
  token_dict['Signature'] = sign_result.decode()
  token_dict['expire'] = expire_syncpoint
  token_dict['dir'] = upload_dir
  token_dict['callback'] = base64_callback_body.decode()
  return token_dict


def get_local_ip():
  """
  获取本机IPV4地址。
  :return: 成功获取，则返回本机IP地址。获取失败，则返回为空。
  """
  try:
    csocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    csocket.connect(('198.51.100.0', 80))
    (addr, port) = csocket.getsockname()
    csocket.close()
    return addr
  except socket.error:
    return ""
