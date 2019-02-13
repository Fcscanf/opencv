"""
@author:Fcant
@description：存取图像
@date: 2019-02-13/0013 上午 11:41
"""

import cv2

#读取一张图像
color_img = cv2.imread('leaf-141494.jpg')
print(color_img.shape)
#直接读取单通道
gray_img = cv2.imread('leaf-141494.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)
#把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
cv2.imwrite('test_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('test_grayscale.jpg')
print(reload_grayscale.shape)
#cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围为1-100，默认95，越高画质越好，文件越大
cv2.imwrite('test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 95))
#cv2.IMWRITE_PNG_COMPRESSION指定PNG质量，范围为0-9，默认3，越高文件越小，画质越差
cv2.imwrite('test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 3))