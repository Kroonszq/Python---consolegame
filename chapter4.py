from importlib.resources import path
from func import printTxt
from func import playsound, printTxt, os, inputfield

def chapter4(items):
    chapter4 = open("text/chapter4/Chapter4.txt", "r", encoding="utf-8")
    chapter4route = open("text/chapter4/Chapter4-route.txt", "r", encoding="utf-8")
    print("\033[35m\033[1mCHAPTER 4 - the magical forest\033[0m")
    failed = False
    
    while True:
        if "map" in items:
            if "food" in items:
                items.remove("food")
            printTxt(chapter4route,"import")
            print("Norr saw a lightning struck tree.")

            # path 1 
            path1 = None
            while True:
                decision = inputfield("Is Norr going left or right? ", ["left", "right"], items)
                if decision == "A": #GOOD
                    path1 = True
                    break
                elif decision == "B": #WRONG
                    path1 = False
                    break
                else:
                    print("invalid input")

            #path 2
            path2 = None
            if path1:
                while True:
                    decision = inputfield("Norr has three options this time does het go left, right or strait thru the field? ", ["left", "right", "straight"], items)
                    if decision == "C":
                        path2 = True
                        break
                    elif decision == "A" or decision == "B":
                        path2 = False
                        break
                    else:
                        print("invalid input")

            #path 3    
            path3 = None
            if path2:
                while True:
                    decision = inputfield("Norr can  go left or right what does he choose? ", ["left", "right"], items)
                    if decision == "A": #GOOD     
                        path3 = True 
                        break
                    elif decision == "B": #WRONG
                        path3 = False
                        break
                    else:
                        print("invalid input")

            #path 4
            path4 = None
            if path3:
                while True:
                    decision = inputfield("Norr can  go left or right what does he choose? ", ["left", "right"], items)
                    if decision == "B":
                        path4 = True
                        break
                    elif decision == "A":
                        path4 = False
                        break
                    else:
                        print("invalid input")
                
            #check result
            if path4: # CORRECT = A C A B
                print("He finnaly reached the edge of the dark creepy forest")
            else:
                failed = True
                items.remove("map")
                print("It became even darker and then the sounds started at first Norr thought it was the wind rustling through the leaves then Norr started to assure himself it was the wind rustling through the leaves and that he wasn’t lost. He started seeing eyes everywhere. And then he saw the creature. A lot of eyes, big fangs and eight legs this was the biggest spider Norr had ever seen. Norr was extremely scared but needed to do something.")
            input("PRESS ENTER TO CONTINUE ... ")

        elif "map" not in items or failed == True:
            if failed == False:
                printTxt(chapter4,"import")
            
            optionalquestion = ""
            if "golden egg" in items:
                optionalquestion = "Drop the golden egg"

            optionalquestion2 = ""
            if "food" in items:
                optionalquestion = "Drop your own food"

            
            while True:
                decision = inputfield("How are you going to survive? ", ["CHAAARGE!!!", "Flee"], items)
                print(decision)
                if decision == "A":
                    if "knife" in items:
                        print("Norr charged the spider. With the knife he got from the old hunter in his village. He jumped and per chance the knife pierced an eye blood splattered everywhere. Norr ran to his cart and rode away never looking back.")
                    else:
                        exit("Norr charged the spider but without a weapon didn’t stand a chance the fangs of the spider pierced his skin and he lost conscious immediately. He never saw his family again.")   
                
                elif decision == "B":
                    print("He spurred on his horse to flee as fast as possible, but he wasn’t fast enough. ")

                    while True:
                        decision = inputfield("You need to drop something? ", ["drop mortgage items", optionalquestion, optionalquestion2], items)
                        print(decision)

                        if decision == "A":
                            print("It was a hard choice but he had to drop the milk to go faster. But he still wasn’t fast enough so he also had to leave the chickens to distract the spider. With the spider distracted Norr was able to flee without a problem.")
                            items.remove("milk")
                            items.remove("chickens")
                            break
                        elif decision == "B":
                            print("It was a hard choice but he had to drop his own food to distract the spider. He couldn’t afford to lose any the mortgage items. With the spider distracted Norr was able to flee without a problem.")
                            items.remove("golden egg")
                            break
                        elif decision == "C":
                            print("It was a hard choice but he had to drop the golden egg to go faster. While Norr lost the egg he was fast enough to escape the spider.")
                            items.remove("golden egg")
                            break
                        else:
                            print("invalid input")
                    break
                else:
                    print("invalid input")
              
        if "food" not in items:
            print("Norr still needed something to eat so he picked up an apple at the edge of the forest.")
            items.append("apple")
            print("\033[93m\033[1macquired magic apple\033[0m")
            print()
            input("press a button to contiue...")
        return True

