import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #Image, video and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def chageRes(width,height):
    #live video only
    capture.set(3,width)
    capture.set(4,height)

# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read() #videos are read frame by frame

#     frame_resized = rescaleFrame(frame, scale=0.2)

#     cv.imshow('Video', frame)
#     cv.imshow('Video resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

img = cv.imread('Pictures/cat.jpg')

img_resized = rescaleFrame(img, scale=0.5)

cv.imshow('img',img)
cv.imshow('img resized', img_resized)

cv.waitKey(0)