import random


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
        print(f"You have won the words was {word}")
        break

