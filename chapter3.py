from func import printTxt
from func import playsound, printTxt, os, inputfield
import time

def chapter3(items):
    chapter3 = open("text/chapter3/chapter3.txt", "r", encoding="utf-8")
    print("\033[35m\033[1mCHAPTER 3 - the wazy wizard\033[0m")
    printTxt(chapter3,"import")


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

    if decision == "A" or decision == "B":
        if decision == "A":
            print("Norr decided  to give the beggar his own food. “Here  ”, said Norr,” it isn’t much but it is al I have at the moment.” The beggar reached for the food with shaking hands. At that moment Norr could see the eyes of the man, they were sparkling with intelligence. Moments later the man threw the rags of him, and revealed long expensive looking robes and a long grey beard. “Thank you for sharing your food so graciously young man,” said the wizard, ”I’d like to return the favour, so young man tell me what is it you are after? ”. Norr was confused for a minute, but eventually he found the clarity of mind to tell the wizard the situation and that he didn’t think he’d make it in time. “if that’s all then I know of a safe route through the dangerous magical forest” said the wizard and handed him a map and disappeared.")
            items.append("map")
            print("\033[93m\033[1macquired map\033[0m")
            
        elif decision == "B":
            print("Norr decided  to give the beggar his golden egg. “Here  ”, said Norr,” maybe you can sell this in the next town and buy some food.” The beggar reached for the egg with shaking hands. At that moment Norr could see the eyes of the man, they were sparkling with intelligence. Moments later the man threw the rags of him, and revealed long expensive looking robes and a long grey beard. “Thank you for sharing your wealth so graciously young man,” said the wizard, ”I’d like to return the favour, so young man tell me what is it you are after? ”. Norr was confused for a minute, but eventually he found the clarity of mind to tell the wizard the situation and that he didn’t think he’d make it in time. “if that’s all then I know of a safe route through the dangerous magical forest” said the wizard and handed him a map and disappeared.")
            items.append("map")
            print("\033[93m\033[1macquired map\033[0m")

        print("the map contains a set of instructions")
        print("By the lightning struck tree go left")
        print("When you come across a large open field go strait over it")
        print("At the skull boulder turn left")
        print("when you see the mushroom forest turn right")
        print()
        input("press enter to continue...")
        return True
    elif decision == "C":
        print("Norr felt sorry for the beggar but didn’t think he could miss anything. When he rode past, the beggar asked if Norr was going to the castle. Norr said he was but didn’t think he’d make it in time. The beggar said he could take a shortcut through the magical forest. Norr rode away and yelled thanks before the beggar could finish his sentence.")
        return  True

