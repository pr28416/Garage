import cv2 as cv

# Original
img = cv.imread('Photos/group 1.jpg')
cv.imshow('original', img)


# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# haar_face
haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'{len(faces_rect)} faces found')
for x,y,w,h in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
cv.imshow('faces', img)

cv.waitKey(0)