from func import playsound, printTxt, os, inputfield

def chapter1(items):
    farmtxt = open("text/chapter1/farm.txt", "r", encoding="utf-8")         #load chapter txt
    #playsound("sound/naturesound.wav", "start")                            #play song
    print("\033[35m\033[1mCHAPTER 1 - the farm\033[0m")                     #display chapter
    printTxt(farmtxt)                                                       #display chapter txt

    # player desicion
    while True:
        options = [
            "Go straight to the village",
            "Check your chickens",
        ]
        decision1 = inputfield("Enter youre choice ", options, items)
        if decision1.upper().strip() == "A":
            break
        elif decision1.upper() == "B":
            items.append("golden egg")
            print("Nor checks the chickens and finds a golden egg and puts it in his bag")
            break
        else:
            print("invalid action")
    print("Norr walks with the horses to the village")
    input()
