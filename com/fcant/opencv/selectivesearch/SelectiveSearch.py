"""
@author:Fcant
"""

import cv2

if __name__ == '__main__':
    cv2.setUseOptimized(True);
    cv2.setNumThreads(4);

    # read image
    im = cv2.imread("D:/Photos/Screenshots/62.jpg")
    # resize image
    newHeight = 200
    newWidth = int(im.shape[1] * 200 / im.shape[0])
    im = cv2.resize(im, (newWidth, newHeight))
    cv2.imshow("input", im)

    # 创建算法+设置输入图像
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(im)

    # 使用SS快速版本
    ss.switchToSelectiveSearchFast()

    # 执行SS
    rects = ss.process()
    print('Total Number of Region Proposals: {}'.format(len(rects)))

    # 推荐100个ROI
    numShowRects = 100
    imOut = im.copy()

    # 显示前100个区域外接矩形框
    for i, rect in enumerate(rects):
        if i < numShowRects:
            x, y, w, h = rect
            cv2.rectangle(imOut, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
        else:
            break

    # show output
    cv2.imshow("SS-Demo", imOut)
    cv2.waitKey(0)
    cv2.destroyAllWindows()