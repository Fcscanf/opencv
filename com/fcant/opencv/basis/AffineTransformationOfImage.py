"""
@author:Fcant
@description：图像的仿射变换-缩放、旋转、剪切、翻转、平移
@date: 2019-02-13/0013 下午 18:51
"""

import cv2
import numpy as np


# 图像显示的函数，用于在处理前后作对比
def image_show(image_name, file_name):
    cv2.namedWindow(image_name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(image_name, file_name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 读取一张图片
img = cv2.imread('girl.jpg')
image_show("Girl", img)
# 沿着横纵轴放大1.6倍，然后平移（-150，-240），最后沿原图大小截取，等效于裁剪并放大
M_crop_elephant = np.array([
    [1.6, 0, -150],
    [0, 1.6, -240]
], dtype=np.float32)
img_elephant = cv2.warpAffine(img, M_crop_elephant, (400, 600))
image_show('Elephant', img_elephant)
# cv2.imwrite('img_elephant.jpg', img_elephant)

# x轴的剪切变换，角度15°
theta = 15 * np.pi / 180
M_shear = np.array([
    [1, np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)
img_shared = cv2.warpAffine(img, M_shear, (400, 600))
image_show('Shared', img_shared)
# cv2.imwrite('img_safari_shared.jpg', img_shared)

# 顺时针旋转，角度15°
M_rotate = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)
img_rotated = cv2.warpAffine(img, M_rotate, (400, 600))
image_show("Rotated", img_rotated)
# cv2.imwrite('img_safari_rotated.jpg', img_rotated)

# 某种变换，具体几何意义可以通过SVD分解理解
M = np.array([
    [1, 1.5, -400],
    [0.5, 2, -100]
], dtype=np.float32)
img_transformed = cv2.warpAffine(img, M, (400, 600))
image_show('Transformed', img_transformed)
# cv2.imwrite('img_safari_transformed.jpg', img_transformed)
