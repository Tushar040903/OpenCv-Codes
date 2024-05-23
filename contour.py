import cv2 as cv
import numpy as np

img = cv.imread("Pictures/shapes.png")
cv.imshow("Image",img)


imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', imgGray)
imgBlur = cv.GaussianBlur(imgGray,(3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', imgBlur)
canny = cv.Canny(imgBlur,175,200)
#cv.imshow('Canny', canny)

imgHor = np.hstack((img,img))  
cv.imshow("imageStack",imgstack)



cv.waitKey(0)