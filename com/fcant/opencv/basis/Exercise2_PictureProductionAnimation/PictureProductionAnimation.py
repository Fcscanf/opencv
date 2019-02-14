"""
@author:Fcant
@description：读取文件夹的图片以动画形式播放
@date: 2019-02-14/0014 下午 19:50
"""

import os
import cv2
from itertools import cycle


# 列出文件夹下的所有图片
filenames = os.listdir('frames')
# 通过itertools.cycle生成一个无限循环的迭代器，每次迭代都输出下一张图像对象
img_iter = cycle([cv2.imread(os.sep.join(['Frames', x])) for x in filenames])
key = 0
while key != 27:
    cv2.imshow('Fcant', next(img_iter))
    key = cv2.waitKey(2000)
