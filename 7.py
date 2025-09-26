#number guessing game 

import random 

print("Welcome to the number guessing game! Try to guess the number im thinking of. Its between 1 and 20. If you want to quit at any time then press q \nPick your poison: \n 1. Easy mode (15 tries) \n 2. Medium mode (10 tries) \n 3. Hard mode (5 tries)\n 4. Bet on your luck (1 try only)")
difficulty = int(input())
guesses = []
trycount = 0
number = random.randint(1,20)
if difficulty == 1:
    trycount = 15
    print("Chi chillar")
elif difficulty == 2:
    trycount = 10
    print("Okay ig")
elif difficulty == 3:
    trycount = 5
    print("sare nee saavu nuvvu savu")
elif difficulty == 4:
    trycount = 1
    print("Hell yeah") 
else:
    print("Kastham ila aithe")

winstatus = 0

if trycount != 1:
    while True:
        for i in range(trycount):
            guesses.append(int(input(f"Try {i+1}: ")))
            if guesses[i]>number:
                print("Too high")
            elif guesses[i]<number:
                print("Too low")
            elif guesses[i] == number:
                print("Ding Ding Ding you got it!!!")
                winstatus = 1
                stop = True
                break
            elif guesses[i] == "q":
                break
        if stop == True:
            break
else:
    guesses.append(int(input("One and only one shot lets go: ")))
    if guesses[0] == number:
        print("How on earth did you pull that off?")
        winstatus = 1
    else:
        print("Nice try")
    
if winstatus == 0:
    print(f"Better luck next time :( the number was {number})")
    print(f"You failed {len(guesses)} times")
    print(f"Your guesses were {guesses}")
else:
    print("Good job you actually did it!")
    print(f"You tried {len(guesses)} times")
    print(f"Your guesses were {guesses}")



            





