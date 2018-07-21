#Hangman dead model
attempts = -1

def hangdead():
        print("           ___________   ")
        print("         /            P     ")
        print("         /            I     ")
        print("         0            I     ")
        print("        /|\           I     ")
        print("         |            I     ")
        print("        / \           I     ")
        print("                      I     ")

def hangalmost():
        print("           ___________   ")
        print("          /           P     ")
        print("          /           I     ")
        print("          0           I     ")
        print("         /|\          I     ")
        print("          |           I     ")
        print("         /            I     ")
        print("                      I     ")

def hangworse():
        print("           ___________   ")
        print("          /           P     ")
        print("          /           I     ")
        print("          0           I     ")
        print("         /|\          I     ")
        print("          |           I     ")
        print("                      I     ")
        print("                      I     ")

def hangbad():
        print("           ___________   ")
        print("          /           P     ")
        print("          /           I     ")
        print("          0           I     ")
        print("         /|\          I     ")
        print("                      I     ")
        print("                      I     ")
        print("                      I     ")

def hangok():
        print("          ___________   ")
        print("         /            P     ")
        print("         /            I     ")
        print("         0            I     ")
        print("        /|            I     ")
        print("                      I     ")
        print("                      I     ")
        print("                      I     ")

def hangouch():
        print("           ___________   ")
        print("          /           P     ")
        print("          /           I     ")
        print("          0           I     ")
        print("          |           I     ")
        print("                      I     ")
        print("                      I     ")
        print("                      I     ")

def hangstart():
        print("            ___________   ")
        print("           /           P     ")
        print("           /           I     ")
        print("           0           I     ")
        print("                       I     ")
        print("                       I     ")
        print("                       I     ")
        print("                       I     ")

def hanggood():
        print("            ___________   ")
        print("           /           P     ")
        print("           /           I     ")
        print("                       I     ")
        print("                       I     ")
        print("                       I     ")
        print("                       I     ")
        print("                       I     ")

#Easy game code
def easygame():
    print("")
    print("Topic: ANIMALS")
    animals = ['Lion', 'Dog', 'Cat', 'Frog', 'Fish', 'Shark', 'Tiger']
    word = random.choice(animals)
    blanks = len(word)
    blanks = int(blanks)
    space = "     "
    attempts = 7
    answer = "-" * blanks
    if attempts == 7:
        hanggood()
    print(answer)
    print(space)
    print(space)
    right = 0
    while attempts > 0:
        print("")
        letter = input("? ")
        if letter in word:
            print("")
            print("Good!")
            print("")
            i = word.find(letter)
            answer = list(answer)
            answer[i] = letter
            answer = ''.join(answer)
            print(answer)
            right = right + 1
            if right == blanks:
                print("")
                print("You won!")
                print("")
                again = input("Play again? (y/n) ")
                if again == "y":
                    start()
                else:
                    exit()

        if letter not in word:
            print("Whoops!")
            attempts = attempts - 1
            if attempts == 6:
                hangstart()
            elif attempts == 5:
                hangouch()
            elif attempts == 4:
                hangok()
            elif attempts == 3:
                hangbad()
            elif attempts == 2:
                hangworse()
            elif attempts == 1:
                hangalmost()
            elif attempts == 0:
                hangdead()
                print("")
                print("Game over, you're dead!")
                print("")
                again = input("Play again? (y/n) ")
                if again == "y":
                    start()
                else:
                    exit()

#Medium game code
def mediumgame():
    print("")
    print("Topic: COLORS")
    colors = ['Blue', 'Red', 'Gold', 'Topaz', 'Silver', 'Bronze', 'Rusted']
    word = random.choice(colors)
    blanks = len(word)
    blanks = int(blanks)
    space = "     "
    attempts = 7
    answer = "-" * blanks
    if attempts == 7:
        hanggood()
    print(answer)
    print(space)
    print(space)
    right = 0
    while attempts > 0:
        print("")
        letter = input("? ")
        if letter in word:
            print("")
            print("Good!")
            print("")
            i = word.find(letter)
            answer = list(answer)
            answer[i] = letter
            answer = ''.join(answer)
            print(answer)
            right = right + 1
            if right == blanks:
                print("")
                print("You won!")
                print("")
                again = input("Play again? (y/n) ")
                if again == "y":
                    start()
                else:
                    exit()

        if letter not in word:
            print("Whoops!")
            attempts = attempts - 1
            if attempts == 6:
                hangstart()
            elif attempts == 5:
                hangouch()
            elif attempts == 4:
                hangok()
            elif attempts == 3:
                hangbad()
            elif attempts == 2:
                hangworse()
            elif attempts == 1:
                hangalmost()
            elif attempts == 0:
                hangdead()
                print("")
                print("Game over, you're dead!")
                print("")
                again = input("Play again? (y/n) ")
                if again == "y":
                    start()
                else:
                    exit()

#Hard game code
def hardgame():
    print("")
    print("Topic: CAPITALS")
    capitals = ['Seoul', 'Washington', 'Paris', 'Rome', 'Sucre', 'Beirut', 'Berlin']
    word = random.choice(capitals)
    blanks = len(word)
    blanks = int(blanks)
    space = "     "
    attempts = 7
    answer = "-" * blanks
    if attempts == 7:
        hanggood()
    print(answer)
    print(space)
    print(space)
    right = 0
    while attempts > 0:
        print("")
        letter = input("? ")
        if letter in word:
            print("")
            print("Good!")
            print("")
            i = word.find(letter)
            answer = list(answer)
            answer[i] = letter
            answer = ''.join(answer)
            print(answer)
            right = right + 1
            if right == blanks:
                print("")
                print("You won!")
                print("")
                again = input("Play again? (y/n) ")
                if again == "y":
                    start()
                else:
                    exit()

        if letter not in word:
            print("Whoops!")
            attempts = attempts - 1   #Attempts start as 7
            if attempts == 6:
                hangstart()
            elif attempts == 5:
                hangouch()
            elif attempts == 4:
                hangok()
            elif attempts == 3:
                hangbad()
            elif attempts == 2:
                hangworse()
            elif attempts == 1:
                hangalmost()
            elif attempts == 0:
                hangdead()
                print("")
                print("Game over, you're dead!")
                print("")
                again = input("Play again? (y/n) ")   #Play again menu
                if again == "y":
                    start()
                else:
                    exit()


#Start up screen
def start():
    gameon = 1
    import random
    print("")
    print("Welcome to Hangman!")
    print("")
    print("Easy (1)")
    print("Medium (2)")
    print("Hard (3)")
    print("")
    difficultyselected = 0
    difficulty = input("Select difficulty. ")

    if difficulty == "1":
        easygame()

    if difficulty == "2":
        mediumgame()

    if difficulty == "3":
        hardgame()



gameon = 1
import random
print("")
print("Welcome to Hangman!")
print("")
print("Easy (1)")
print("Medium (2)")
print("Hard (3)")
print("")
difficultyselected = 0
difficulty = input("Select difficulty. ")


if difficulty == "1":
    easygame()

if difficulty == "2":
    mediumgame()

if difficulty == "3":
    hardgame()
