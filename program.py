from func import playsound, printTxt, os

introtxt = open("text/chapter1/intro.txt", "r", encoding="utf-8")
farmtxt = open("text/chapter2/farm.txt", "r", encoding="utf-8")
items = []


# - CHAPTER 1 INTRODUCTION ------------------------------------------------------------------------------------------------
playsound("sound/intromusic.wav", "start")                    #play song
print("\033[35m\033[1mCHAPTER 1 - introduction\033[0m")       #display chapter
printTxt(introtxt)                                            #display chapter txt

# player desicion
ready = input("\033[91m\033[1mARE YOU READY TO START THIS ADVENTURE? (YES / NO): \033[0m")
if ready != "YES":
    exit("Not ready? No problem come back next time")

playsound("", "stop")                                        #stop song
os.system("cls")                                             #clear cls


playing = True
while playing:
    # - CHAPTER 2 THE FARM ------------------------------------------------------------------------------------------------
    playsound("sound/naturesound.wav", "start")             #play song
    print("\033[35m\033[1mCHAPTER 1 - the farm\033[0m")     #display chapter
    printTxt(farmtxt)                                       #display chapter txt

    # player desicion
    while True:
        decision1 = input("DO YOU WANT TO CHECK YOUR CHICKENS BEFORE HEADING TO THE VILLAGE?(YES/NO): ")
        if decision1.upper() == "YES":
            items.append("golden egg")
            print("Nor checks the chickens and finds a golden egg and puts it in his bag")
            break
        elif decision1.upper() == "CHICKENS":
            break
        else:
            print("invalid action")
    print("Norr walks with the horses to the village")
    input()
   


