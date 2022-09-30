from func import playsound, printTxt, os, inputfield

def chapter7(items):
    banditxt = open("text/chapter7/chapter7.txt", "r", encoding="utf-8")         #load chapter txt (primary)         
    #playsound("sound/naturesound.wav", "start")                                 #play song
    print("\033[35m\033[1mCHAPTER 7 - The bandits\033[0m")                       #display chapter
    printTxt(banditxt, "import")

    # extra option 1 - golden egg
    extraOption1 = ""
    if "golden egg" in items:
        extraOption1 = "Buy the bandits off with golden egg"

    # extra option 2 - magic apple
    extraOption2 = ""
    if "apple" in items:
        extraOption2 = "Give magic apple"

    
    while True:
        awnser = inputfield("What will Norr do? ", ["Pass trough", extraOption1, extraOption2])
        # OPTION A - Pass trough
        if awnser == "A":
            print("2 mortage items get stolen")
            print(f"\033[31m\033[1mlost bread & grain\033[0m")

            items.remove("bread")
            items.remove("grain")
            break
        if extraOption1 or extraOption2:
            # OPTION B - gplden egg/magic apple
            if awnser == "B":
                if extraOption1:
                    print("Norr gives the golden egg to the badints to buy them off the bandits accept and let him trough")
                    items.remove("golden egg")
                else:
                    print("The magic apple drops from Norr his pocket and out of nowhere out of the magic apple spawns a giant tree and norr and his horse are liftid up")
                    items.remove("apple")
                break
            # OPTION C - golden magic apple
            elif awnser == "C":
                print("The magic apple drops from Norr his pocket and out of nowhere out of the magic apple spawns a giant tree and norr and his horse are liftid up")
                items.remove("apple")
                break

        print("Invalid input")

    input("Press enter to continue: ")

    return True

