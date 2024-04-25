#add a method that write multiple lines of text
#add a method that used mylife.txt for text
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
BACKGROUND_BLACK = '\033[40m'
RESET = '\033[0m'
from pyfiglet import Figlet
font = Figlet(font='drpepper')
print(YELLOW + font.renderText("Hello User") + RESET)

proceed = True
while proceed:
    line = input(BRIGHT_CYAN + BACKGROUND_BLACK + "\nEnter line: \n" + RESET)
    break_line = line+("\n")
#add a method for looping text
    with open("mylife.txt", "a") as my_life_output:
        my_life_output.write(break_line)
#add an input for lines
        while proceed:
#add a method that ask the user y or n
            repeat = input(GREEN + BACKGROUND_BLACK +"\nAre there any more lines yes/no? \n" + RESET)
            if repeat.lower() == "yes":
                break
            elif repeat.lower() == "no":
                proceed = False
            else:
                print(RED + BACKGROUND_BLACK + "\nInvalid, type yes/no only bro! \n" + RESET)
                continue