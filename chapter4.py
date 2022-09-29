from func import printTxt
from func import playsound, printTxt, os, inputfield

def chapter4(items):
    chapter4 = open("text/chapter3/chapter4.txt", "r", encoding="utf-8")
    chapter4route = open("text/chapter3/chapter4-route.txt", "r", encoding="utf-8")
    print("\033[35m\033[1mCHAPTER 4 - the magical forest\033[0m")
    

    if "map" in items:
        printTxt(chapter4route,"import")

        options = [
        "Give your own food",
        optionalquestion,
        "Give nothing"
        ]
        decision = inputfield("What is Norr going to do? ", options, items)
        print(decision)

        
    else:
        printTxt(chapter4,"import")
        
        optionalquestion = ""
        if "golden egg" in items:
            optionalquestion = "Give the golden egg"


        options = [
        "Give your own food",
        optionalquestion,
        "Give nothing"
        ]
        decision = inputfield("What is Norr going to do? ", options, items)
        print(decision)
