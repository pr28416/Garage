import cv2 as cv
import numpy as np

# Original
img = cv.imread('Photos/park.jpg')
cv.imshow('original', img)

b,g,r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blue channel', blue)
cv.imshow('green channel', green)
cv.imshow('red channel', red)
# cv.imshow('attempted merge', cv.merge([cv.split(blue)[0], cv.split(green)[1], cv.split(red)[2]]))

cv.waitKey(0)