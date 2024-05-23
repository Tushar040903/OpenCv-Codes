import cv2 as cv

img = cv.imread('Pictures/boston.jpeg')
cv.imshow('cat', img)

# 1. converting to grayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blurr
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. edge cascade
canny = cv.Canny(blur,175,200)
cv.imshow('Canny', canny)

# 4. dilating
dilate = cv.dilate(img, (3,3) , iterations=1)
cv.imshow('dialte', dilate)

# 5. Erode
erode = cv.erode(img, (3,3), iterations=1)
cv.imshow('erode', erode)

# cropping
cropped = img[0:100,200:500]   #only here height comes first
# resize
resize = cv.resize(img,(100,100))

cv.waitKey(0)