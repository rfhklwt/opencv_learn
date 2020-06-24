'''
1. 色彩空间转换函数 - cvtColor
COLOR_BGR2GRAY = 6 彩色到灰度
COLOR_GRAY2BGR = 8 灰度到彩色
COLOR_BGR2HSV = 40 BGR到HSV
COLOR_HSV2BGR = 54 HSV到BGR

2. 图像保存 - imwrite
第一个参数是图像保存路径
第二个参数是图像内存对象
'''
import cv2 as cv
src = cv.imread("D:/Our Home/Python/OpenCV/rabbits.jpg")
#cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.imwrite("D:/Our Home/Python/OpenCV/rabbits_gray.jpg", gray)
cv.waitKey(0)
cv.destroyAllWindows()m,,

