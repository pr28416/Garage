import cv2 as cv
import numpy as np

# Original
img = cv.imread('Photos/park.jpg')
cv.imshow('Boston original', img)

# Translate
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# translated = translate(img, 100, -100)
# cv.imshow('translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    height, width = img.shape[:2]
    if rotPoint is None: rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

# rotated = img
# sides = 100
# for _ in range(sides):
    # rotated = rotate(rotated, 360*(sides-2)/(sides))
# rotated = rotate(img, 180)
# cv.imshow('rotated', rotated)

# rot2 = rotate(rotated, 90)
# cv.imshow('rot2', rot2)




# Resize
# resized = cv.resize(img, (500, 1000), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)




# Flip
# flip=cv.flip(img, -1)
# cv.imshow('flip -1', flip)
# flip=cv.flip(img, 0)
# cv.imshow('flip 0', flip)
# flip=cv.flip(img, 1)
# cv.imshow('flip 1', flip)



# Crop
# cropped = img[200:400, 300:400]
# cv.imshow('cropped', cropped)

cv.waitKey(0)