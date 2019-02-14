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

    # 如果获取的键值小于256则作为ASCII码输出对应的字符，负责直接输出值
    # msg = '{} is pressed'.format(chr(key) if key < 256 else key)
    # print(key) # Windows下输出chr() arg not in range(0x110000)


# 定义鼠标事件回调函数
def on_mouse(event, x, y, flags, param):
    # 鼠标左键按下，抬起，双击
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left button down at ({}, {})'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('Left button up at ({}, {})'.format(x, y))
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('Left button double clicked at ({}, {})'.format(x, y))

    # 鼠标右键按下，抬起，双击
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('Right button down at ({}, {})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        print('Right button up at ({}, {})'.format(x, y))
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print('Right button double clicked at ({}, {})'.format(x, y))

    # 鼠标中/滚轮键（如果有）按下，抬起，双击
    elif event == cv2.EVENT_MBUTTONDOWN:
        print('Middle button down at ({}, {})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONUP:
        print('Middle button up at ({}, {})'.format(x, y))
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print('Middle button double clicked at ({}, {})'.format(x, y))

    # 鼠标移动
    elif event == cv2.EVENT_MOUSEMOVE:
        print('Mouse moving at ({}, {})'.format(x, y))

# 为指定的窗口绑定自定义的回调函数
cv2.namedWindow('Honeymoon Island')
cv2.setMouseCallback('Honeymoon Island', on_mouse)