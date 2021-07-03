import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Photos/cat_large.jpg")
cv.imshow('Cat', img)
resized_img = rescaleFrame(img)
cv.imshow('Cat resized', resized_img)
cv.waitKey(0)

# capture = cv.VideoCapture('Videos/dog.mp4')
# capture = cv.VideoCapture(2)

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, 0.2)
#     cv.imshow('Video', frame)
#     cv.imshow('Video resized', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
cv.destroyAllWindows()