# To Do: 1. Create a level select.
#        2. Fix the "Guess after Win" bug.
#        3. Add new secret codes.

import random

print("""
 _____  ___  ___   ___    _     _   ____   ____    ____
|  _  | \\  \\/  /  / __\\  | |   | | |  __| / ___\\  / ___\\
| |_| |  \\    /  | | __  | |   | | | |_   \\___    \___
|   __|   |  |   | |_\\ | |  \_/  | |  _|  ___/ |  ___/ |
|__|      |__|    \\___/   \\_____/  |____| \\____/  \\____/

         "One Billion Digits and Counting!~"
         
© Christopher Bilodeau 2019
""")

cheat = input("Press RETURN to Start. ")

if cheat == "TIGUESS":
    print("I'm Sorry.")

elif cheat == "CAT":
    print("Meow~")

elif cheat == "DOG":
    print("woof.")

elif cheat == "SECRET":
    print("Congratulations! You found a secret.")

difficulty = 1000000000

for x in range(1):
  number = (random.randint(1,difficulty))
  print(number)
running = True

def answer():
    answer = int(input("Guess > "))
    if answer == number:
        print("You Win! Congratulations!")
        running = False
    
    elif (answer < number):
        print("Too Low.")

    
    elif (answer > number):
        print("Too High.")

    
    else:
        print("I am Error.")

while(running == True):
    answer()

