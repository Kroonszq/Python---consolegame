from func import playsound, printTxt, os, inputfield

def chapter1(items:list) -> bool:
    farmtxt = open("text/chapter1/farm.txt", "r", encoding="utf-8")         #load chapter txt
    goldenEgg = open("text/chapter1/egg.txt", "r", encoding="utf-8")        #load goldenegg txt
    #playsound("sound/naturesound.wav", "start")                            #play song
    print("\033[35m\033[1mCHAPTER 1 - the farm\033[0m")                     #display chapter
    printTxt(farmtxt, "import")                                             #display chapter txt

    # player desicion
    while True:
        options = [
            "Go straight to the village",
            "Check your chickens",
        ]
        decision1 = inputfield("Enter youre choice ", options, items)
        if decision1.upper().strip() == "A":
            print("Norr walks with the horses to the village")
        elif decision1.upper().strip() == "B":
            items.append("golden egg")
            print("\033[93m\033[1macquired golden egg\033[0m")
            printTxt(goldenEgg, "import")
            break
        else:
            print("invalid action")

    input("Press enter to continue: ")
    return True                                                                #end chapter1
