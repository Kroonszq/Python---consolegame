from func import playsound, printTxt, os, inputfield

def intro():
    introtxt = open("text/intro/intro.txt", "r", encoding="utf-8")
    #playsound("sound/intromusic.wav", "start")                             #play song
    print("\033[35m\033[1mCHAPTER 1 - introduction\033[0m")                 #display chapter
    printTxt(introtxt)                                                      #display chapter txt

    # player desicion
    ready = input("\033[91m\033[1mARE YOU READY TO START THIS ADVENTURE? (YES / NO): \033[0m")
    
    playsound("", "stop")                                         #stop song
    os.system("cls")                                              #clear cls

    if ready != "YES":
        print("Not ready? No problem come back next time")
        return False
    else:
        return True

