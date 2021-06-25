from selenium import webdriver
from time import sleep
import threading
from random import randint

# browsers = [webdriver.Chrome("/Users/pranavramesh/Developer/chromedriver") for _ in range(10)]
# browser = webdriver.Chrome("/Users/pranavramesh/Developer/chromedriver")
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
# for i in range(1000):
    runVideo(f"T{i}")
    i += 1
# threads = [threading.Thread(target=runVideo, args=(f"T{i}", None)) for i in range(5)]
# for thd in threads:
#     thd.start()
# for thd in threads:
#     thd.join()
# counts = [0] * 10
# while set(counts) != {10}:
#
"""
def print_squares(thread_name, numbers):
    for number in numbers:
        print(thread_name, number ** 2)

        # Produce some delay to see the output
        sleep(1)


# Creating 3 threads that execute the same
# function with different parameters
thread1 = threading.Thread(target=print_squares,
                           args=("thread1", [1, 2, 3, 4, 5]))

thread2 = threading.Thread(target=print_squares,
                           args=("thread2", [6, 7, 8, 9, 10]))

thread3 = threading.Thread(target=print_squares,
                           args=("thread3", [11, 12, 13, 14, 15]))

# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Join the threads before
# moving further
thread1.join()
thread2.join()
thread3.join()
"""