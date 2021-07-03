import numpy as np
import cv2 as cv
import os
from random import randint

from numpy.lib.function_base import kaiser

people = [i for i in os.listdir(r'Faces/train') if i[0] != '.']

haar_cascade = cv.CascadeClassifier('haar_face.xml')
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

path = r'Faces/val'
val = [i for i in os.listdir(path) if i[0] != '.']
personPath = os.path.join(path, val[randint(0, len(val)-1)])
snapshot = [i for i in os.listdir(personPath) if i[0] != '.']
imgPath = os.path.join(personPath, snapshot[randint(0, len(snapshot)-1)])
img = cv.imread(imgPath)
cv.imshow('img', img)

# Detect face
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for x,y,w,h in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label={people[label]} with confidence of {confidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('detected face', img)

cv.waitKey(0)