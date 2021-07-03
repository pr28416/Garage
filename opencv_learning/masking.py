import cv2 as cv
import numpy as np

# Original
img = cv.imread('Photos/cats 2.jpg')
cv.imshow('orig', img)

# Create mask
blank = np.zeros(img.shape[:2], dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('mask', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('masked', masked)

cv.waitKey(0)