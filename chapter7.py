from func import playsound, printTxt, os, inputfield

def chapter7(items):
    banditxt = open("text/chapter7/chapter7.txt", "r", encoding="utf-8")         #load chapter txt (primary)         
    #playsound("sound/naturesound.wav", "start")                                 #play song
    print("\033[35m\033[1mCHAPTER 6 - The bandits\033[0m")                #display chapter
    printTxt(banditxt, "import")

    extraOption = ""
    if "golden egg" in items:
        extraOption = "But the bandits off with golden egg"

    awnser = inputfield("What will Norr do? ", ["Pass trough", "give 2 mortage items", extraOption], []) 

    # OPTION A - Pass trough
    if awnser == "A":
        print("2 mortage items get stolen")
    elif awnser == "B":
        print("2 mortage items get stolen")
    elif awnser == "C":
        print()






chapter7(["golden egg"])