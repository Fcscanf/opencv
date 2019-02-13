"""
@author:Fcant
@description：图片的缩放、裁剪、补边操作
@date: 2019-02-13/0013 下午 12:03
"""

import cv2


# 图像显示的函数，用于在处理前后作对比
def image_show(image_name, file_name):
    cv2.namedWindow(image_name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(image_name, file_name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 读取一张图片
img = cv2.imread('leaf-141494.jpg')
#image_show("first image", img)

# 缩放成200*200的方形图像
img_300_200 = cv2.resize(img, (300, 200))
#image_show("300_200_img", img_300_200)
# 不直接指定缩放后的大小，通过fx和fy指定缩放比例，0.5则长宽为原来的一半
# 等效于img_200_300 = cv2.resize(img, (300, 200),注意指定大小的格式是（宽度，高度）
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最临近插值

img_200_300 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
#image_show("200_300_img", img_200_300)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300*300的图像
img_300_300 = cv2.copyMakeBorder(img, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
#image_show("300_300_img", img_300_300)

# 对照片中进行部分裁剪
patch_tree = img[20:150, -180:-50]
#image_show("patch_tree", patch_tree)

"""
对处理的图像进行存储
cv2.imwrite('patch_tree', patch_tree)
cv2.imwrite('img_200_300.jpg', img_200_300)
cv2.imwrite('img_300_200.jpg', img_300_200)
cv2.imwrite('img_300_300.jpg', img_300_300)
"""

"""
@author:Fcant
@description：色调、明暗、直方图、Gamma曲线
@date: 2019-02-13/0013 下午 12:41
"""

#通过cv2.cvtColor把图像从BGR转换到HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#H空间中，绿色比黄色值高一点，所以给每个像素+15,黄色的树叶就会变绿
turn_green_hsv = img_hsv.copy()
turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0]+15) % 180
turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
#image_show("turn_green_img", turn_green_img)
#cv2.imwrite("turn_green.jpg", turn_green_img)

# 减少饱和度会让图像损失鲜艳变得更灰
colorless_hsv = img_hsv.copy()
colorless_hsv[:, :, 1] = 0.5 * colorless_hsv[:, :, 1]
colorless_img = cv2.cvtColor(colorless_hsv, cv2.COLOR_HSV2BGR)
#image_show("colorless_img", colorless_img)
#cv2.imwrite("colorless.jpg", colorless_img)

# 减少明度为原来的一半
darker_hsv = img_hsv.copy()
darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]
darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
#image_show("darker_img", darker_img)
#cv2.imwrite("darker.img", darker_img)