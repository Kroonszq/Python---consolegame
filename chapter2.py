from ast import While
from func import playsound, printTxt, os, inputfield
import random

def chapter2(items:list):
    villagetxt = open("text/chapter2/chap2.txt", "r", encoding="utf-8")         #load chapter txt (primary)
    inntxt = open("text/chapter2/inn.txt", "r", encoding="utf-8")               #load inn txt (optional)
    neighbortxt = open("text/chapter2/neighbor.txt", "r", encoding="utf-8")     #load neighbor txt (primary)
    #playsound("sound/naturesound.wav", "start")                                #play song
    print("\033[35m\033[1mCHAPTER 2 - The village\033[0m")                      #display chapter
    printTxt(villagetxt, "import")                                              #display chapter txt

    completedInn = False                                                       
    while True:   


        options = ["Pickup the package from the neighbors"]
        if not completedInn:
            options.append("Get a drink at the local inn")

        decision = inputfield("Enter youre choice ", options, items)
        os.system('cls')  


        # OPTION - Pickup the package from the neighbors
        if decision.upper().strip() == "A": 
            items.append("package")                                        
            printTxt(neighbortxt, "import")                                    
            printTxt("\033[93m\033[1macquired package\033[0m")                
            input("Press enter to continue")                                   
            return True


        # OPTION - "Get a drink at the local inn
        elif decision.upper().strip() == "B":
            printTxt(inntxt, "import")
            options = [
                "Play a game with the man",
                "Get yourslef a drink and leave",
            ]
            decision2 = inputfield("Enter youre choice ", options, items)
            os.system('cls')       


            # OPTION - Play a game with the man
            if decision2 == "A":                                                
                printTxt("Alright, the game we will play is hangman, i will chose a word and you have to guess it")
                while True:
                    result = hangmanPuzzle()                                            
                    # RESULT - LOST
                    if not result:                                              
                        print("Unfortunately you lost") 
                        again = inputfield("Care to try again?", ["yes", "no"], items)
                        # OPTION - NO
                        if again == "B":                                        
                            printTxt("Ha! you lost sad for you")
                            break 
                    # RESULT - WIN
                    else:                                                      
                        print(f"{result}")
                        items.append("knife")
                        printTxt("\033[93m\033[1macquired knife\033[0m")
                        printTxt("You did wel boy, the men handed over his knife")
                        break
                printTxt("Norr drinks the last little bit of water. Thank the man for the game and leave the inn heading towards the ")
                input("Press enter to continue")

                
            # OPTION - Get yourslef a drink and leave
            else:
                print("Drink and leave")
            completedInn = True


        else:
            print("Invalid input")


def hangmanPuzzle():
    words = ["hunter", "arrow", "beast", "knife"]
    word = random.choice(words)
    wordGuess = ["_" for x in range(0, len(word))]

    faults = 0
    while faults < 10:
        print(*wordGuess)
        letter = input("Enter a letter ")
        index, guessstr = 0, ""

        if not isinstance(letter, str) or len(letter) != 1:
            print("input error")
            faults+=1
            continue

        if letter in word:
            for x in word:
                if x == letter:
                    wordGuess[index] = letter
                index+=1
        else:
            faults+=1
        for swa in wordGuess:
            guessstr+=swa
        if guessstr == word:
            os.system('cls') 
            return f"You have won the words was {word}"
    os.system('cls') 
    return False