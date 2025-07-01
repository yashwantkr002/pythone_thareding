from threading import *
import time
e=Event()
def light():
    time.sleep(3)
    e.set()
    print("green light on")
    time.sleep(5)
    print("red light on ")
    e.clear()


def people():
    e.wait()
    while e.is_set():
        print("you can go ")
        time.sleep(.5)
    print("stop")

t1=Thread(target=light)
t2=Thread(target=people)
t1.start()
t2.start()
