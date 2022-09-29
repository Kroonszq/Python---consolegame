from pygame import mixer
import time
import sys
import os
mixer.init()
texttype = input("Instant text or typing text(instant/typing): ")


def printTxt(text:str, type:str = "") -> None:
    """
    Prints text in typing/instant way
    """
    if type == "import":  #import == .txt
        for x in text.read():
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.01) if texttype == "typing" else None # sleeps for 5 seconds
    else:  # regular string
        for x in text:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.01) if texttype == "typing" else None # sleeps for 5 seconds
    print("\n")

def playsound(path:str, action:str) -> None:
    """
    Play or Stop music
    """
    if action == "stop":
        mixer.music.fadeout(2500) # milisecond
    else:
        mixer.music.load(path)
        mixer.music.play(-1) # loop ifinity
        mixer.music.set_volume(0.1)

def inputfield(txt:str, choises:list, inv:list) -> None:
    """
    Create an input field based on the choises you give
    """
    while True:
        print("What are you gonna do? ")
        opt = ord("A")
        for x in choises:
            if len(x) > 0:
                print(f"{chr(opt)} - {x}")
                opt+=1
        playerInput = input(f"\033[91m\033[1m{txt}\033[0m")
        if playerInput == "inventory":
            print("\033[93m\033[1m",inv,"\033[0m")
        else:
            return playerInput

