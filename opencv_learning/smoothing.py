import cv2 as cv

# Original
img = cv.imread('Photos/cats.jpg')
cv.imshow('original', img)


blurLvl = 7

# Averaging
avgBlur = cv.blur(img, (blurLvl,blurLvl))
cv.imshow('average', avgBlur)


# Gaussian
gBlur = cv.GaussianBlur(img, (blurLvl,blurLvl), 0)
cv.imshow('gaussian', gBlur)


# Median
medBlur = cv.medianBlur(img, blurLvl)
cv.imshow('median', medBlur)


# Bilateral
biBlur = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', biBlur)


cv.waitKey(0)