import cv2 as cv
import sys

def convertToGrayscale(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('grayscale', gray)
    cv.waitKey(0)

def blur(img, giveback=False):
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
    if giveback: return blur
    cv.imshow('blur', blur)
    cv.waitKey(0)

def edge(img, giveback=False):
    canny = cv.Canny(img, 175, 175)
    if giveback: return canny
    cv.imshow('canny', canny)
    cv.waitKey(0)

def dilate(img):
    canny = cv.Canny(img, 175, 175)
    dilated = cv.dilate(canny, (7,7), iterations=3)
    cv.imshow('dilated', dilated)
    cv.waitKey(0)

def erode(img):
    canny = cv.Canny(img, 175, 175)
    dilated = cv.dilate(canny, (7,7), iterations=3)
    eroded = cv.erode(dilated, (7,7), iterations=3)
    cv.imshow('canny', canny)
    cv.imshow('dilated', dilated)
    cv.imshow('eroded', eroded)
    cv.waitKey(0)

def resize(img):
    cv.imshow('original', img)
    resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
    cv.imshow('resized', resized)
    cv.waitKey(0)

def crop(img):
    cv.imshow('original', img)
    cropped = img[50:200, 200:400]
    cv.imshow('cropped', cropped)
    cv.waitKey(0)

img = cv.imread(f'Photos/{sys.argv[1]}')
# convertToGrayscale()
# blur(img)
crop(img)