import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Cat', img)

# blank[200:300, 300:400] = 0,255,0
# cv.imshow('green', blank)

# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
# cv.circle(blank, (250, 250), 100, (255,0,0), thickness=3)
# cv.line(blank, (0,0), (250,250), (255,0,0), thickness=3)
cv.putText(blank, "hello world", (0, blank.shape[0]//2), fontFace=cv.FONT_HERSHEY_COMPLEX_SMALL, fontScale=2.0, color=(0,255,255), thickness=2)
cv.imshow('canvas', blank)

cv.waitKey(0)