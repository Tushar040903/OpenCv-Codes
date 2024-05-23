import cv2 as cv

img = cv.imread('Pictures/cat.jpg') #to read image from the path

cv.imshow('cat',img) #to show image

cv.waitKey(0)

# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read() #videos are read frame by frame

#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


# cap  = cv.VideoCapture(0)
# cap.set(3,340)
# cap.set(4,480)

# while True:
#     isTrue, frame = cap.read() #videos are read frame by frame

#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break