from pygame import mixer
import time
import sys
import os
mixer.init()
texttype = input("Instant text or typing text(instant/typing): ")
def print_text(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05) if texttype == "typing" else None # sleeps for 5 seconds
    print("\n")

def playsound(path, action):
    if action == "stop":
        mixer.music.fadeout(2500) # milisecond
    else:
        mixer.music.load(path)
        mixer.music.play(-1) # loop ifinity
        mixer.music.set_volume(0.1)