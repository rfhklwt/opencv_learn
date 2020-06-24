import cv2 as cv
src = cv.imread("D:/Our Home/Python/OpenCV/rabbits.jpg")
#cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)
# 避免内存泄漏
cv.destroyAllWindows()

