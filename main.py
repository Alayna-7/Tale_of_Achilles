import time
from colorama import Fore, Style, init

init()

# ALL COLOURS FOR CHARACTERS
colours = {
    "Achilles": Fore.YELLOW,
    "Patroclus": Fore.RED,
    "Odysseus": Fore.CYAN,
    "Thetis": Fore.BLUE,
    "Peleus": Fore.GREEN,
    "Agamemnon": Fore.MAGENTA,
    "Priam": Fore.GREEN,
}


print("----------------------------------------------\n")
print(Style.BRIGHT + "Tale of Achilles\n"+Style.RESET_ALL)
print("----------------------------------------------\n")

time.sleep(1)
print(Style.DIM + "Press enter to progress the game."+Style.RESET_ALL)

file = open("script.txt", "r")

line = file.readline()

while line:
    input()
    
    parts = line.strip().split()

    if parts:
        character = parts[0]
        dialogue = " ".join(parts[1:])

    if character == "Choice":
        end = False
        line = file.readline()
        print(Fore.WHITE + Style.BRIGHT + line.rstrip() +"\n")
        line = file.readline()
        print(line.rstrip() + Style.NORMAL+"\n\n")

        #Player choice
        choice = input("Please make a choice (1 or 2): ")

        while choice != "1" and choice != "2":
            choice = input("Make a choice (1 or 2): ")

        while not end:
            line = file.readline()
            parts = line.strip().split()
            choiceNum = parts[0]
            character = parts[1]
            dialogue = " ".join(parts[2:])

            if choiceNum == choice:
                input()
                colour = colours.get(character, Fore.WHITE)
                if character == "Athena":
                    print(Fore.BLUE + Style.BRIGHT + dialogue + Style.RESET_ALL)
                else:
                    print(colour + dialogue)

            if choiceNum == "END":
                end = True

    if character == "SCENE":
        print(Fore.WHITE + "\n\n----------------------------------------------")

    else:
        colour = colours.get(character, Fore.WHITE)

        print(colour + dialogue)
    
    line = file.readline()

file.close()

print("\n\n----------------------------------------------\n")
print(Style.BRIGHT + "Tale of Achilles\n"+Style.RESET_ALL)
print("Thank you for playing!\n")
print("By Alayna I.\n")
print("----------------------------------------------\n")