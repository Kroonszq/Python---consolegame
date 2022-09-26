from func import playsound, print_text, os

# - INTRODUCTION ------------------------------------------------------------------------------------------------
playsound("sound/intromusic.wav", "start")
print_text("This story begins with a family of 3 that runs a small farm next to the \"mountain of treasures\".\n\
The family contains of a mother, a father and a aboy. Every on of them got there own tasks on the farm.\n\
The mother works with the cows and makes sure there is enough milk produced.\n\
The father cuts down the grain in the fields and bakes bread.\n\
And the boy takes care of the chicken.\n\
\n\
The family reserves 2 stashes of products they gain from the farm.\n \n\
The first stash is for the local people. Every Saturday they go to the nearby village and sell there farm products on the market.\n\
The second stash is for the king. Every first Monday of the month the family has to deliver 2kgs of grain, 10 liter milk, 12 bread & 2 chickens to the king. to pay off their mortgage.\n\
\n\
Only this time the father is sick and the boy (you) is forced to deliver the package to the king alone.\n\
Trough the mountains of treasures you will you experience things you have never seen before.\n\
Are you worthy to deliver the package!?")

ready = input("\033[91m\033[1mARE YOU READY TO START THIS ADVENTURE? (YES / NO): \033[0m")
if ready != "YES":
    exit("Not ready? No problem come back next time")
playsound("", "stop")
os.system("cls")

items = []
playing = True
while playing:
    # PART 1 - FARM ------------------------------------------------------------------------------------------------
    playsound("sound/naturesound.wav", "start")
    print("\033[35m\033[1mCHAPTER 1 - the farm\033[0m")
    print_text("It’s the day before the first Monday of the month in the evening.\n\
    The father is laying down in bed and shouts to his son if he can come the son comes running down to him.\n\
    The dad explains his son he cant go tomorrow and that he is to sick. Cant we ask someone else to do it for us asks his son.\n\
    No says the father is to late for that now you have to go. Me ? says the boy indignantly. But dad I have never done it before.\n\
    I know son says the father but there is no other option right now.")
    print_text("After long consultation and many questions with his father, the boy goes to bed.\n\
    he is nervous he doesn't know if he can do it but there is no other option.\n\
    \n\
    The next day he hears his mother getting the horses ready with the carts with the products for the king.\n\
    The boy gets up and changes and walks out towards the door.\n\
    but just before he goes out the door, his father calls out to him.\n\
    the boy looks around and the father says \"Look out for yourself and I love you \033[1mNorr\033[0m\" Norr nods and walks out he kisses his mother and is ready to go")

    while True:
        decision1 = input("GO TO THE VILLAGE OR CHECK THE CHICKEN BEFORE YOU GO(VILLAGE/CHICKENS): ")
        if decision1.upper() == "VILLAGE":
            break
        elif decision1.upper() == "CHICKENS":
            items.append("golden egg")
            print("Nor checks the chickens and finds a golden egg and puts it in his bag")
            break
        else:
            print("invalid action")
    print("Norr walks with the horses to the village")
   


