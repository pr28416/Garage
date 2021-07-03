import cv2 as cv
import numpy as np

# Original
img = cv.imread('Photos/cats.jpg')
cv.imshow('original', img)


# Blank
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)


# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)


# Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)


# Edge canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)


# Threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)


# Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)


# Key-quit
cv.waitKey(0)