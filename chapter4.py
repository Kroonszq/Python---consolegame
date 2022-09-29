from base64 import decode
import re
from func import printTxt
from func import playsound, printTxt, os, inputfield

def chapter4(items):
    chapter4 = open("text/chapter4/Chapter4.txt", "r", encoding="utf-8")
    chapter4route = open("text/chapter4/Chapter4-route.txt", "r", encoding="utf-8")
    print("\033[35m\033[1mCHAPTER 4 - the magical forest\033[0m")
    failed = False
    
    while True:

        if "map" in items:
            printTxt(chapter4route,"import")

            print("Norr saw a lightning struck tree.")

            options = [
            "left",
            "right"
            ]
            decision = inputfield("Is Norr going left or right? ", options, items)
            print(decision)

            if decision == "A":
                print("The next landmark Norr needed to watch out for was a large open field.")
                options = [
                "left",
                "right",
                "strait"
                ]
                decision = inputfield("Norr has three options this time does het go left, right or strait thru the field? ", options, items)
                print(decision)
                
                if decision == "C":
                    print("He followed the road until he saw a large skull shaped boulder.")
                    options = [
                    "left",
                    "right"
                    ]
                    decision = inputfield("Norr can  go left or right what does he choose? ", options, items)
                    print(decision)

                    if decision == "A":
                        print("He next reached a poisonous looking giant mushroom patch.")
                        options = [
                        "left",
                        "right"
                        ]
                        decision = inputfield("Norr can  go left or right what does he choose? ", options, items)
                        print(decision)
                        if decision == "right":
                            return True
                        else:
                            print("It became even darker and then the sounds started at first Norr thought it was the wind rustling through the leaves then Norr started to assure himself it was the wind rustling through the leaves and that he wasn’t lost. He started seeing eyes everywhere. And then he saw the creature. A lot of eyes, big fangs and eight legs this was the biggest spider Norr had ever seen. Norr was extremely scared but needed to do something.")
                            failed = True
                            items.remove("map")
                    else:
                        print("It became even darker and then the sounds started at first Norr thought it was the wind rustling through the leaves then Norr started to assure himself it was the wind rustling through the leaves and that he wasn’t lost. He started seeing eyes everywhere. And then he saw the creature. A lot of eyes, big fangs and eight legs this was the biggest spider Norr had ever seen. Norr was extremely scared but needed to do something.")
                        failed = True
                        items.remove("map")
                else:
                    print("It became even darker and then the sounds started at first Norr thought it was the wind rustling through the leaves then Norr started to assure himself it was the wind rustling through the leaves and that he wasn’t lost. He started seeing eyes everywhere. And then he saw the creature. A lot of eyes, big fangs and eight legs this was the biggest spider Norr had ever seen. Norr was extremely scared but needed to do something.")
                    failed = True
                    items.remove("map")
            else:
                print("It became even darker and then the sounds started at first Norr thought it was the wind rustling through the leaves then Norr started to assure himself it was the wind rustling through the leaves and that he wasn’t lost. He started seeing eyes everywhere. And then he saw the creature. A lot of eyes, big fangs and eight legs this was the biggest spider Norr had ever seen. Norr was extremely scared but needed to do something.")
                failed = True
                items.remove("map")
            
        else:
            if failed == False:
                printTxt(chapter4,"import")
            
            optionalquestion = ""
            if "golden egg" in items:
                optionalquestion = "Drop the golden egg"

            optionalquestion2 = ""
            if "food" in items:
                optionalquestion = "Drop your own food"


            options = [
            "CHAAARGE!!!",
            "Flee"
            ]
            decision = inputfield("How are you going to survive? ", options, items)
            print(decision)

            if decision == "A":
                if "knife" in items:
                    print("Norr charged the spider. With the knife he got from the old hunter in his village. He jumped and per chance the knife pierced an eye blood splattered everywhere. Norr ran to his cart and rode away never looking back.")
                    
                else:
                    print("Norr charged the spider but without a weapon didn’t stand a chance the fangs of the spider pierced his skin and he lost conscious immediately. He never saw his family again.")
                    return False
            elif decision == "B":
                print("He spurred on his horse to flee as fast as possible, but he wasn’t fast enough. ")

                options = [
                "drop mortgage items",
                optionalquestion2,
                optionalquestion
                ]
                decision = inputfield("You need to drop something? ", options, items)
                print(decision)

                if decision == "A":
                    print("It was a hard choice but he had to drop the milk to go faster. But he still wasn’t fast enough so he also had to leave the chickens to distract the spider. With the spider distracted Norr was able to flee without a problem.")
                elif decision == "B":
                    print("It was a hard choice but he had to drop his own food to distract the spider. He couldn’t afford to lose any the mortgage items. With the spider distracted Norr was able to flee without a problem.")
                elif decision == "C":
                    print("It was a hard choice but he had to drop the golden egg to go faster. While Norr lost the egg he was fast enough to escape the spider.")
            
            if "food" not in items:
                print("Norr still needed something to eat so he picked up an apple at the edge of the forest.")
                items.append("apple")
            return True