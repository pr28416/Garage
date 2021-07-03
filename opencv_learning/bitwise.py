import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)


# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# Bitwise NOT
bitwise_not_rect = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not_rect', bitwise_not_rect)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('bitwise_not_circle', bitwise_not_circle)

cv.waitKey(0)