import cv2 as cv
import numpy as np

img = cv.imread('Pictures/cat.jpg')

imgHor = np.hstack((img,img))   # for vertical use vstack

cv.imshow('image',imgHor)

cv.waitKey(0)