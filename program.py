from chapter1 import chapter1
from chapter2 import chapter2
from intro import intro
from func import os
from chapter3 import chapter3

chapter = 0
playing = True
items = ["grain", "bread", "milk", "chickens"]

while playing:
    #load in intro:
    if chapter == 0:   
        os.system("cls") #clear cls                                                                                   
        intr = intro()
        if intr:
            chapter+=1
        else:
            continue

    #load in chapter1
    if chapter == 1:     
        os.system("cls") #clear cls                    
        chap1 = chapter1(items)
        if chap1:
            chapter+=1
        else:
            continue

    #load in chapter2
    if chapter == 2:
        os.system("cls") #clear cls                         
        chap2 = chapter2(items)
        if chap2:
            chapter+=1
        else:
            continue

    #load in chapter3
    if chapter == 3:
        os.system("cls") #clear cls                         
        chap3 = chapter3(items)
        if chap3:
            chapter+=1
        else:
            continue

    
    # #load in chapter4
    # if chapter == 4:
    #     os.system("cls") #clear cls                         
    #     chap4 = chapter4(items)
    #     if chap4:
    #         chapter+=1
    #     else:
    #         continue
    # input("Hier komt chapter 3")
    
    break