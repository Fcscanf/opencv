import cv2;

print("--------- Test OpenCV ---------");
src = cv2.imread("D:\Photos\proxy\90d58f0c09a9cbbd18e98dcf2aea0ec9.jpg");
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE);
cv2.imshow("input image", src);
cv2.waitKey(0);
cv2.destroyAllWindows();
print("--------- End Test ---------");