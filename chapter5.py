from func import playsound, printTxt, os, inputfield

def chapter5(items:list):
    sleepingtxt = open("text/chapter2/chap2.txt", "r", encoding="utf-8")         #load chapter txt (primary)         
    #playsound("sound/naturesound.wav", "start")                                 #play song
    print("\033[35m\033[1mCHAPTER 5 - The mountain roads\033[0m")                #display chapter
    printTxt(sleepingtxt, "import")      
    input("Press enter to continue ")
    return True     
      