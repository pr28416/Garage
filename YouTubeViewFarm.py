from selenium import webdriver
from time import sleep
import threading
from random import randint

videos = [
    "https://youtu.be/2hmt-nFnKEg",
    "https://youtu.be/mYBBaVnCthc",
    "https://youtu.be/la9kLfXcmMQ",
    "https://youtu.be/mXUDoRiERxo",
    "https://youtu.be/ccgzLUifwrA",
    "https://youtu.be/i_4VIFEZbpw"
]
def runVideo(_thread_name):
    browser = webdriver.Chrome("/Users/pranavramesh/Developer/chromedriver")
    video, seconds = videos[randint(0, len(videos)-1)], randint(10, 30)
    print(f"({_thread_name}) Running '{video}' for {seconds} sec")
    browser.get(video)
    sleep(seconds)
    browser.quit()

i = 0
while i < 100000:
    runVideo(f"T{i}")
    i += 1
