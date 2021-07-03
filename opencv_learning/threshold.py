import cv2 as cv

# Original
img = cv.imread('Photos/pingpong_preview.jpg')
cv.imshow('orig', img)


# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)



# Simple thresholding
threshold, thresh = cv.threshold(gray, 180, 255,  cv.THRESH_BINARY)
cv.imshow('simple thresholded', thresh)

# Simple thres_inv
# threshold, thresh_inv = cv.threshold(gray, 180, 255,  cv.THRESH_BINARY_INV)
# cv.imshow('simple thresholded inverse', thresh_inv)


# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 11)
cv.imshow('adaptive thresholding', adaptive_thresh)


cv.waitKey(0)