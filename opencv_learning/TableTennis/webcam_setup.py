import cv2 as cv
import numpy as np

capture = cv.VideoCapture(1)

while True:
    ret, frame = capture.read()
    if not ret: break
    cv.imshow('webcam', frame)
    if cv.waitKey(1) == ord('q'): break

capture.release()
cv.destroyAllWindows()