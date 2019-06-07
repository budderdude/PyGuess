import random
import sys
from os import system, name
from time import sleep
# define clear function
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = system('clear')

print("""
 _____  ___  ___   ___    _     _   ____   ____    ____
|  _  | \\  \\/  /  / __\\  | |   | | |  __| / ___\\  / ___\\
| |_| |  \\    /  | | __  | |   | | | |_   \\___    \___
|   __|   |  |   | |_\\ | |  \_/  | |  _|  ___/ |  ___/ |
|__|      |__|    \\___/   \\_____/  |____| \\____/  \\____/   version 1.3

         "One Billion Digits and Counting!~"
         
© Christopher Bilodeau 2019
""")

cheat = input("Press RETURN to Start. ")
screen_clear()
difficulty = 1000000000

if cheat == "TIGUESS":
    print("I'm Sorry.")

elif cheat == "CAT":
    print("Meow~")

elif cheat == "DOG":
    print("woof.")

elif cheat == "SECRET":
    print("Congratulations! You found a secret.")

elif cheat == "Custom":
    print("SuperCheat Activated: Custom")
    difficulty = int(input("Choose 1 - [?]: "))


# Random Number Generator
for x in range(1):
  number = (random.randint(1,difficulty))


def answer():
    answer = int(input("Guess > "))
    if answer == number:
        # Random Number Generator
        for x in range(1):
            thanks = (random.randint(1,100))
        print("You Win! Congratulations!")
        
        if thanks == 1:
            print("""
            Heya, Chris here. You know, the guy who developed this
            silly little game (You can see that in the copyright notice!).
            It's super lucky that you're actually seeing this! In fact, it's 
            a 1/100 chance! Take a picture!
            
            Well anyways, I'm here to say "Thanks!". It really means
            a lot that you took the time to not only get this working,
            but also played all the way through to One Billion!
            
            For your incredible luck, I present you with a Magic Code!
            
            MAGIC CODE: "CAT"
            
            Magic Codes, are essentially just cheat codes. Access them
            on the title screen by typing the code, then hitting RETURN.
            
            Thanks Again!         
                                                               -Chris :)
            """)
            sys.exit()
        
        if thanks == 2:
            print("""
            Heya, Chris here. You know, the guy who developed this
            silly little game (You can see that in the copyright notice!).
            It's super lucky that you're actually seeing this! In fact, it's 
            a 1/100 chance! Take a picture!
            
            Well anyways, I'm here to say "Thanks!". It really means
            a lot that you took the time to not only get this working,
            but also played all the way through to One Billion!
            
            For your incredible luck, I present you with a Magic Code!
            
            MAGIC CODE: "TIGUESS"
            
            Magic Codes, are essentially just cheat codes. Access them
            on the title screen by typing the code, then hitting RETURN.
            
            Thanks Again!         
                                                               -Chris :)
            """)
            sys.exit()
        
        if thanks == 3:
            print("""
            Heya, Chris here. You know, the guy who developed this
            silly little game (You can see that in the copyright notice!).
            It's super lucky that you're actually seeing this! In fact, it's 
            a 1/100 chance! Take a picture!
            
            Well anyways, I'm here to say "Thanks!". It really means
            a lot that you took the time to not only get this working,
            but also played all the way through to One Billion!
            
            For your incredible luck, I present you with a Magic Code!
            
            MAGIC CODE: "DOG"
            
            Magic Codes, are essentially just cheat codes. Access them
            on the title screen by typing the code, then hitting RETURN.
            
            Thanks Again!         
                                                               -Chris :)
            """)
            sys.exit()
        
        if thanks == 4:
            print("""
            Heya, Chris here. You know, the guy who developed this
            silly little game (You can see that in the copyright notice!).
            It's super lucky that you're actually seeing this! In fact, it's 
            a 1/100 chance! Take a picture!
            
            Well anyways, I'm here to say "Thanks!". It really means
            a lot that you took the time to not only get this working,
            but also played all the way through to One Billion!
            
            For your incredible luck, I present you with a Magic Code!
            
            MAGIC CODE: "SECRET"
            
            Magic Codes, are essentially just cheat codes. Access them
            on the title screen by typing the code, then hitting RETURN.
            
            Thanks Again!         
                                                               -Chris :)
            """)
            sys.exit()
        
        if thanks == 5:
            print("""
            Heya, Chris here. You know, the guy who developed this
            silly little game (You can see that in the copyright notice!).
            It's super lucky that you're actually seeing this! In fact, it's 
            a 1/100 chance! Also, it's really lucky! You'll see why soon.
            Take a picture!
            
            Well anyways, I'm here to say "Thanks!". It really means
            a lot that you took the time to not only get this working,
            but also played all the way through to One Billion or Beyond!
            
            For your amazing luck, I present you with a SuperCheat!
            These "SuperCheats" are cheats that change the way the game
            plays. Warning, this may make some of my text not make sense.
            
            SuperCheat: "Custom"
            
            Access SuperCheats on the title screen by typing the code, then 
            hitting RETURN. 
            
            Thanks Again!         
                                                               -Chris :)
            """)
        else:    
            sys.exit()
    
    elif (answer < number):
        
        print("Too Low.")
    
    elif (answer > number):
        print("Too High.")
    
    else:
        print("I am Error.")

while(1):
    answer()