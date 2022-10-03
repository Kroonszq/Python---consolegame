from func import playsound, printTxt, os, inputfield

def chapter6(items:list):
    sleepingtxt = open("text/chapter6/chapter6.txt", "r", encoding="utf-8")         #load chapter txt (primary)         
    #playsound("sound/naturesound.wav", "start")                                 #play song
    print("\033[35m\033[1mCHAPTER 6 - The temple\033[0m")                #display chapter
    printTxt(sleepingtxt, "import")   
     
    print("I have 3 riddles for you!")
    print()
    # ridle 1
    while True:
        options = [  
            "Dragon",
            "Griffyn",
            "Firefly"
        ]
        awnser = inputfield("It breathes fire and can fly high. If you train him and befriend this mighty beast, it can show you around. What is it?" , options, [])
        if awnser == "A":   #correct
            print("\033[92mCorrect\033[0m")
            break
        print("Ha thats wrong! try again")

    # ridle 2
    while True:
        options = [
            "A potion",
            "A magical curse.",
            "Death",
        ]
        awnser = inputfield("This is no ordinary thing. People fear it more than death, and a witch coven protects it all the time. What is it?", options, [])
        if awnser == "B":   #correct
            print("\033[92mCorrect\033[0m")
            break
        print("Ha thats wrong! try again")

    # ridle 3
    while True:
        options = [
            "A Castle",
            "A prison",
            "A tower"
        ]
        awnser = inputfield("It has mighty tall walls, all the riches, and also a dark prison to capture all the evil. What is it?", options, [])
        if awnser == "A":   #correct
            print("\033[92mCorrect\033[0m")
            break
        print("Ha thats wrong! try again")

    printTxt("Mhhhm, after all you are worthy to pass i didnt expect that. Here take this you might need this.")
    print("\033[93m\033[1macquired key\033[0m")

    items.append("key")
    input("Press enter to continue ")
    return True     
      
