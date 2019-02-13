"""
@author:Fcant
@description：拍摄延时视频
@date: 2019-02-13/0013 下午 21:05
"""

import cv2
import time

# 捕获图像的时间间隔
interval = 60
# 捕获图像的总帧数
num_frames = 500
# 输出文件的帧率
out_fps = 24

# VideoCapture(0)表示打开默认的相机
cap = cv2.VideoCapture(0)
# 获取捕获的分辨率
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 设置要保存的视频的编码，分辨率和帧数
video = cv2.VideoWriter(
    "time_lapse.avi",
    cv2.VideoWriter_fourcc('M','P','4','2'),
    out_fps,
    size
)

# 对一些低画质的摄像头，前面的帧可能不稳定，略过
for i in range(42):
    cap.read()

# 开始捕获，通过read函数捕取捕获的帧
try:
    for i in range(num_frames):
        _, frame = cap.read()
        video.write(frame)
        # 如果希望每一帧也存成文件，比如制作GIF，则取消下面的注释
        filename = '{:0>6d}.png'.format(i)
        cv2.imwrite(filename, frame)
        print('Frame {} is captured.'.format(i))
        time.sleep(interval)
except KeyboardInterrupt:
    # 提前停止捕获
    print('Stopped! {}/{} frames captured!'.format(i, num_frames) )

# 释放资源并写入视频文件
video.release()
cap.release()
