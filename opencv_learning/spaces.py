import cv2 as cv
# import matplotlib.pyplot as plt

# Original
img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
# plt.show()

# # Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)


# HSV (hue-saturation-value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)


# # LAV
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)


# # RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)


# HSV to grayscale
hsv_gray = cv.cvtColor(cv.cvtColor(hsv, cv.COLOR_HSV2BGR), cv.COLOR_BGR2GRAY)
cv.imshow('hsv --> gray', hsv_gray)

# Key-quit
cv.waitKey(0)