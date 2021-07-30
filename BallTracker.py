import cv2
import numpy as np

# Returns the approximate coordinates of the ball
def trackBall(img):
    blur = cv2.GaussianBlur(img, (21,21), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # green_lo, green_up = np.array([20, 80, 20], 'uint8'), np.array([64, 255, 255], 'uint8')
    green_lo, green_up = np.array([0, 64, 160], 'uint8'), np.array([102, 111, 255], 'uint8')
    mask = cv2.inRange(hsv, green_lo, green_up)
    combined = cv2.bitwise_and(img,img,mask=mask)
    # return combined
    circles = cv2.HoughCircles(cv2.cvtColor(combined, cv2.COLOR_BGR2GRAY), cv2.HOUGH_GRADIENT, dp=1.2, minDist=100)#,
                     #circles=None, param1=None, param2=None, minRadius=None, maxRadius=None) # http://www.bmva.org/bmvc/1989/avc-89-029.pdf
    # contour = max()
    circles = np.round(circles[0, :]).astype('int')
    if circles is None: return img
    h,k,r = max(circles, key=lambda x: x[2])
    # for h,k,r in circles:
    cv2.circle(img, (h,k), r, (255,195,0), 4)
    cv2.circle(img, (h,k), r//4, (0,0,255), 2)
    return img

if __name__ == '__main__':
    capture = cv2.VideoCapture(2)
    print('Stream started')
    while True:
        passed, frame = capture.read()
        if not passed: break


        cv2.imshow('frame', frame)
        cv2.imshow('track ball', trackBall(frame))

        if cv2.waitKey(1) == ord('q'): break
    print('Stream ended')
