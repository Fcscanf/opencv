import cv2 as cv

src = cv.imread("D:\Photos\Screenshots\62.jpg")
cv.imshow("opencv-python", src)
cv.waitKey(0)
cv.destroyAllWindows()