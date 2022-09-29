from func import printTxt
from func import playsound, printTxt, os, inputfield

def chapter4(items):
    chapter4 = open("text/chapter8/Chapter8.txt", "r", encoding="utf-8")
    print("\033[35m\033[1mCHAPTER 8 - the castle\033[0m")

    mortgageitems = 0 

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

    if "milk" in items:
        mortgageitems += 1
    if "chickens" in items:
        mortgageitems += 1
    if "grain" in items:
        mortgageitems += 1
    if "bread" in items:
        mortgageitems += 1 
    if mortgageitems == 4 and "key" in items:
        print("")
    elif mortgageitems == 2 and "golden egg" in items and "key" in items:
        print("")
    else:
        print("")