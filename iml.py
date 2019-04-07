# coding: utf-8
import sys, os
sys.path.append(os.pardir)
# 首先导入图像处理库
from PIL import Image
from array import *
# 接下来打开图片，并且将像转化为8bit黑白像素
def get_image():
	path_to_image='../1(2).jpg'
	im = Image.open(path_to_image)
	im = im.convert('L')
# 转换图像到mnist的大小28*28
	im = im.resize((28,28))
# 获取图像长宽
	(width, height) = im.size
# 将图像数据转化位mnist
	data_image=[]
	for x in range(0,width):
    	for y in range(0,height):
        	data_image.append(255 -im.getpixel((y,x)))
     return data_image
# 将数据写到mnist文件中
'''header = array('B')
# 写入magic number
header.extend([0,0,8,3])
# 写入数据数量，以一个图片为例
header.extend([0,0,0,1])
# 写入行列像素数
header.extend([0,0,0,28])
header.extend([0,0,0,28])
# 写入数据
header.extend(data_image)
# 最后写文件

output_file = open(r'data.mnist', 'wb')
header.tofile(output_file)
output_file.close()
'''
