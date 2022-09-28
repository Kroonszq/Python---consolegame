from func import playsound, printTxt, os, inputfield

def chapter2(items:list):
    farmtxt = open("text/chapter2/chap2.txt", "r", encoding="utf-8")        #load chapter txt (primary)
    inntxt = open("text/chapter2/inn.txt", "r", encoding="utf-8")           #load inn txt (optional)
    #playsound("sound/naturesound.wav", "start")                            #play song
    print("\033[35m\033[1mCHAPTER 2B - The village\033[0m")                 #display chapter
    printTxt(farmtxt)                                                       #display chapter txt

    while True:
        options = [
            "Pickup the package from the neighbors",
            "Get a drink at the local inn",
        ]
        decision = inputfield("Enter youre choice ", options, items)
        if decision.upper().strip() == "A":
            print("a")
        elif decision.upper().strip() == "B":
            printTxt(inntxt)
            options = [
                "Play a game with the man",
                "Get yourslef a drink and leave",
            ]
            decision2 = inputfield("Enter youre choice ", options, items)

            if decision2 == "A": #play game
                print("Alright, the game we will play is hangman, i will chose a word and you have to guess it")
                word = "Hunter"
                while True:
                    letter = input("Letter?: ")
                    
            else:
                print("Drink and leave")
        else:
            print("Invalid input")

chapter2([])