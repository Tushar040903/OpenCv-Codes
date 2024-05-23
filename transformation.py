import cv2 as cv
import numpy as np

img = cv.imread('Pictures/park.jpg')
cv.imshow('image', img)

# translation
def translation(img, x, y):                                   # -x --> left
    transMat = np.float32([[1,0,x],[0,1,y]])                  # -y --> up
    dimension = (img.shape[1],img.shape[0])                   #  x --> right 
    return cv.warpAffine(img, transMat, dimension)            #  y --> down
 
translated = translation(img,100,100)
cv.imshow("translated",translated)

cv.waitKey(0)