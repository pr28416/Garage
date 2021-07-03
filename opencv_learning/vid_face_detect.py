import cv2 as cv

capture = cv.VideoCapture("/Users/pranavramesh/Downloads/vid_test.mov")
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()
    if not isTrue: break
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
    for x,y,w,h in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    cv.imshow('faces', frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break