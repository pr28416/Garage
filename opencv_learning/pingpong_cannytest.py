"""
NOTES
- 7/3/21 9:00 AM: Successfully loaded in test video, but FPS is too low; I will use threading and load frames into a queue so I can increase FPS, since regular loading function halts other operations until it completes
"""

import cv2 as cv
from threading import Thread
import sys
from queue import Queue

class FileVideoStream:
    def __init__(self, path, queueSize=128):
        self.stream = cv.VideoCapture(path)
        self.stopped = False
        self.queue = Queue(maxsize=queueSize)
        # print(self.stream)

    def start(self):
        print('starting')
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        print('updated')
        while True:
            if self.stopped:
                print('stopped')
                return
            if not self.queue.full():
                print('queue not full, adding')
                grabbed, frame = self.stream.read()
                print('got frame:', grabbed)
            if not grabbed:
                print('nothing grabbed, stopping')
                self.stop()
                return
            print('putting frame')
            self.queue.put(frame)

    def read(self):
        return self.queue.get()

    def more(self):
        return self.queue.qsize() > 0

    def stop(self):
        print("stop function")
        self.stopped = True

capture = cv.VideoCapture("/Users/pranavramesh/Downloads/IMG_2317.mov")
# capture = cv.VideoCapture("/Users/pranavramesh/Downloads/pingpong_hd30_compressed.mov")

# capture = cv.VideoCapture("Videos/dog.mp4")
contents = []

print("loading...")
print(capture.get(cv.CAP_PROP_FPS))
while True:
    # isTrue, frame = capture.read()
    isTrue = capture.grab()
    if not isTrue: break
    _, frame = capture.retrieve()
    # print(frame)
    # biFilter = cv.bilateralFilter(frame, 10, 35, 25)
    # canny = cv.Canny(biFilter, 125, 175)
    # _, thresh = cv.threshold(frame, 180, 255, cv.THRESH_BINARY)
    # contents.append(canny)
    # adaptive_thresh = cv.adaptiveThreshold(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 11)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

# input('ready?')

# print('starting')
# for i in contents:
#     cv.imshow('frame', i)
#     cv.waitKey(1)

capture.release()
cv.destroyAllWindows()
# video = FileVideoStream("/Users/pranavramesh/Downloads/IMG_2317.mov")
# video.start()

# while video.more():
#     frame = video.read()
#     cv.putText(frame, "Queue Size: {}".format(video.queue.qsize()),
# 		(10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#     cv.imshow('frame', frame)
#     cv.waitKey(1)

# cv.destroyAllWindows()
# video.stop()