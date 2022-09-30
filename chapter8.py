from func import printTxt
from func import playsound, printTxt, os, inputfield

def chapter4(items):
    print("\033[35m\033[1mCHAPTER 8 - the castle\033[0m")
    print("After many trials Norr finally reached the castle. Joy overflowed in his body. The only thing left to do was use the key and give the mortgage items and then he could go home. ")


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
        print("Everything went really smooth he used the key to get inside the castle. Then gave the mortgage items to the people in the castle and delivered the package. Now he could go home. THE END.")

    elif mortgageitems == 2 and  "key" in items:
        print("When Norr entered the castle he saw that he only had two of the four mortgage items in his cart.")
        if "golden egg" in items:
            print("When the people inside the castle confronted him about this Norr panicked. He didn’t have anything else to give them. Or did he! Norr still had the golden egg and with that he was able to make up for the two missing items. And Norr could go home. THE END")
        else:
            print("When the people inside the castle confronted him about this Norr panicked. He didn’t have anything else to give them. They gave Norr a choice he had to work in the castle to make up the difference or give the cart and the horse to them. YOU FAILED")

    elif mortgageitems == 0 and "key" in items:
        print("When Norr entered the castle he saw that he only had none mortgage items left in his cart. When the people inside the castle confronted him about this Norr panicked. He didn’t have anything else to give them. The castle people felt ridiculed and decided to severely punish Norr and his parents got a lot of trouble for this and needed to pay the mortgage items and a huge fine. YOU FAILED")

    else:
        print("Norr couldn’t even enter the castle because he didn’t have a key. No matter how he yelled they didn’t let him in. Norr and his parents got a lot of trouble for this and needed to pay the mortgage items and a huge fine. YOU FAILED")