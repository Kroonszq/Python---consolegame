from chapter1 import chapter1
from intro import intro

chapter = 0
playing = True
items = []

while playing:
    if chapter == 0:                                        #load in intro
        intr = intro()
        if intr:
            chapter+=1
        else:
            continue

    if chapter == 1:                                        #load in chapter1
        chap1 = chapter1(items)

    input("YESSSS")