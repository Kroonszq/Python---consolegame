from func import playsound, printTxt, os, inputfield, time

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
        awnser = inputfield("What will Norr do? ", ["Pass trough", "solve puzzle", extraOption1, extraOption2])
        # OPTION A - Pass trough
        if awnser == "A":
            print("2 mortage items get stolen")
            print(f"\033[31m\033[1mlost bread & grain\033[0m")

            items.remove("bread")
            items.remove("grain")
            break
        elif awnser == "B":
            print("Alright i got a puzzle for you.")
            print("Press enter to start the puzzle... ")
            valid = True
            while True:
                try:
                    # question 1
                    question1 = int(input("Whats the fith primary number? "))
                    if question1 != 11:
                        valid = False
                        break
                    #question 2
                    question2 = int(input("Whats the third primary number? "))
                    if question2 != 5:
                        valid = False
                        break
                    #question 3
                    question3 = int(input("Whats the fourth primary number? "))
                    if question3 != 7:
                        valid = False
                        break

                    break
                except ValueError:
                    print("Ha you are more dumber then i thought!!")
                    valid = False
                    break
            if valid:
                print()
                print("Well done boy, i will let you pass without harming you!.")
                #true
            else:
                print()
                print("Ha, bad day for you you failed the puzzle and i will rob you.")
                print(f"\033[31m\033[1mlost bread & grain\033[0m")
                items.remove("bread")
                items.remove("grain")
                #false
            break
        elif extraOption1 or extraOption2:
            # OPTION B - gplden egg/magic apple
            if awnser == "C":
                if extraOption1:
                    print("Norr gives the golden egg to the bandits to buy the bandits off. After inspecting the golden egg they lett Norr trough to continue")
                    if "golden egg" in items:
                        items.remove("golden egg")
                else:
                    print("The magic apple drops from Norr his pocket and out of nowhere out of the magic apple spawns a giant tree and norr and his horse are liftid up")
                    if "apple" in items:
                        items.remove("apple")
                break
            # OPTION C - golden magic apple
            elif awnser == "D" and extraOption2:
                print("The magic apple drops from Norr his pocket and out of nowhere out of the magic apple spawns a giant tree and norr and his horse are liftid up")
                if "apple" in items:
                    items.remove("apple")
                break

        print("Invalid input")

    input("Press enter to continue: ")

    return True

