"""
@author:Fcant
@description：图像显示
@date: 2019-02-04/0004 下午 17:24
"""

import matplotlib.pyplot as plt

plt.figure('A Beautiful model')
beautiful_model = plt.imread('62.jpg')
plt.show(beautiful_model)
#Z是前面生成的随机图案，img0就是Z，img1是Z做了个简单的变换
img0 = Z
img1 = 3*Z+4
#cmap指定为'gray'用来显示灰度
fig = plt.figure('Auto Normalized Visualization')
ax0 = fig.add_subplot(121)
ax0.imshow(img0, cmap='gray')
ax1 = fig.add_subplot(122)
ax1.imshow(img1, cmap='gray')
plt.show()