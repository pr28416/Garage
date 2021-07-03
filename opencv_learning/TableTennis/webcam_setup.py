import cv2
import cv2 as cv
import imutils
# import matplotlib.pyplot as plt
import numpy as np

# Get boundary
# img = cv.imread('tt_table.png')
# plt.imshow(img)
# plt.show()

capture = cv.VideoCapture(0)

# orange_lower_bound = (4, 95, 155)
# orange_upper_bound = (80, 191, 255)
# orange_hsv_lo = (10,100,20)
# orange_hsv_up = (40,255,255)

eighthFrame = None
iteration = 0

while True:
    ret, frame = capture.read()
    if not ret:
        print('something went wrong with trying to access webcam')
        break

    # Make frame gray
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # frame = imutils.resize(frame, width=500)
    text = "No motion"
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7,7), 0) # ksize originally (21,21)

    # if iteration % 8 == 0 or eighthFrame is None:
    if eighthFrame is None:
        eighthFrame = gray


    frameDelta = cv.absdiff(eighthFrame, gray)
    thresh = cv.threshold(frameDelta, 25, 255, cv.THRESH_BINARY)[1]

    thresh = cv.dilate(thresh, None, iterations=2)
    contours = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    for contour in contours:
        if cv.contourArea(contour) < 1000: # 500 is the minimum area size
            continue
        x,y,w,h = cv.boundingRect(contour)
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        text="Motion"

    cv.putText(frame, f"Status: {text}", (10,60), cv.FONT_HERSHEY_COMPLEX, 1.5, (0,0,255), 2)

    # cv.line(blur, (0, 910), (1280, 910), (0,255,0), 3)
    # cv.line(blur, (0, 420), (1280, 420), (0,255,0), 3)
    # cv.imshow('webcam', blur)
    # cv.imshow('mask', mask)
    cv.imshow('mask output', frameDelta)
    cv.imshow('mask output', frame)
    if cv.waitKey(1) == ord('q'): break
    iteration += 1

capture.release()
cv.destroyAllWindows()
