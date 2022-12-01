from typing import List
# from uti

# 找出值相等的项
def find(list: List[dict], key: str, value: str):
  for obj in list:
    if obj[key] == value:
      return obj
  return None

# 找到最大值
def find_max(list: List[dict], key: str):
  max_obj = list[0]
  max_num = max_obj[key]
  for obj in list:
    if obj[key] > max_num:
      max_num = obj[key]
      max_obj = obj
  return max_obj
