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
 ____  ___  ___ ____
|_  _|| __|/  /|_  _|
  ||  | _| \  \  ||
  ||  |___||__/  ||
""")
input("Press RETURN to Play.")
screen_clear()

print(""""
 _    _  ___  _   _  _    _
| \  / || __|| \ | || |  | |
|  \/  || _| |  \| ||  \/  |
|_|\/|_||___||_|\__| \____/

1. Option
2. Option
""")

option = int(input("> "))

if option == 1:
    screen_clear()
    print("1")
if option == 2:
    screen_clear()
    print("2")