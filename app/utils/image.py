from PIL import Image
import operator

import math


def crop(polygon: []):
  num_x = []
  num_y = []
  for index, num in enumerate(polygon):
    if index % 2 == 0:
      num_x.append(num)
    else:
      num_y.append(num)

  max_x = max(enumerate(num_x), key=operator.itemgetter(1))
  print(num_x)
  print(max_x)
  offset = azimuthangle(polygon[0], polygon[1], polygon[2], polygon[3])
  img = Image.open("./resources/ocr_detection.jpg")
  # region = img.crop()
  region = img.rotate(offset - 180, expand=1)
  region.save('./resources/test.jpg')


def azimuthangle(x1, y1, x2, y2):
  """ 已知两点坐标计算角度 -
  :param x1: 原点横坐标值
  :param y1: 原点纵坐标值
  :param x2: 目标点横坐标值
  :param y2: 目标纵坐标值
  """
  angle = 0.0
  dx = x2 - x1
  dy = y2 - y1
  if x2 == x1:
    angle = math.pi / 2.0
    if y2 == y1:
      angle = 0.0
    elif y2 < y1:
      angle = 3.0 * math.pi / 2.0
  elif x2 > x1 and y2 > y1:
    angle = math.atan(dx / dy)
  elif x2 > x1 and y2 < y1:
    angle = math.pi / 2 + math.atan(-dy / dx)
  elif x2 < x1 and y2 < y1:
    angle = math.pi + math.atan(dx / dy)
  elif x2 < x1 and y2 > y1:
    angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
  return angle * 180 / math.pi