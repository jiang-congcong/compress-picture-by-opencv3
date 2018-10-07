#coding = utf-8
import cv2
import os
import math

def get_doc_size(path):
    try:
        size = os.path.getsize(path)
        return get_mb_size(size)
    except Exception as err:
        print(err)

def get_mb_size(bytes):
    bytes = float(bytes)
    mb = bytes / 1024 / 1024
    return mb


def delete_file(path):
    if file_exist(path):
        os.remove(path)
    else:
        print('no such file:%s' % path)


def file_exist(path):
    return os.path.exists(path)


def resize_rate(path, resize_path, fx, fy):
    image = read_image(path)
    im_resize = cv2.resize(image, None, fx=fx, fy=fy)
    delete_file(resize_path)
    save_image(resize_path, im_resize)


def save_image(path, image):
    cv2.imwrite(path, image)


def read_image(path):
    return cv2.imread(path)


path = "D://3//313.jpg" #被压缩图片的绝对路径
resize_path = "D://3//3.jpg"  #压缩图片的存储位置，记住给压缩图片命名，3.jpg就是压缩后图片的名字
size = get_doc_size(path)
print(size) #原始的size
delete_file(resize_path)
filesize = 0.8   #压缩比例

while size > filesize:
    rate = math.ceil((size / filesize) * 10) / 10 + 0.1
    rate = math.sqrt(rate)

    rate = 1.0 / rate
    if file_exist(resize_path):
        resize_rate(resize_path, resize_path, rate, rate)
    else:
        resize_rate(path, resize_path, rate, rate)
    size = get_doc_size(resize_path)


