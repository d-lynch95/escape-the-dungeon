# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import os

import pyfiglet
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# Inventory is a list that shows items users have collected throughout the game

global inventorylist
inventorylist = []

a = 1
b = 2
c = 3


def clearConsole():
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def inventory():
    """
    This function shows a list of items collected.
    If nothing has been collected it prints a string.
    If items have been collected the for loop prints.
    The for loop iterates through items collected.
    """
    time.sleep(c)
    if len(inventorylist) == 0:
        print("No items in the inventory")
    else:
        for item in inventorylist:
            print(item)
    time.sleep(c)


def validation():
    """
    This function prints if user inputs invalid option
    This will reprompt the user to inout a valid option
    This keeps gameplay smooth and on track
    """
    print()
    time.sleep(a)
    print("That's not a valid input")
    time.sleep(b)
    print()
    print("Please select another input option")


def imready():
    """
    This function prints when user has input Y to begin game
    The game will begin after the welcome message
    """
    time.sleep(a)
    print()
    print()
    print("See you on the other side " + name)
    print()
    time.sleep(a)
    begin()


def notready():
    """
    This prints if user is not ready to play
    The game will exit and restart
    This gives the user the option to restart the game
    """
    time.sleep(b)
    print()
    print("hmmmm")
    print("maybe this wasn't the place for you")
    time.sleep(a)
    print("another time perhaps...")
    time.sleep(c)
    start()


def fin():
    """
    This function runs everytime the game ends
    Function also runs if user presses q to exit the game
    this function thanks the user for playing.
    The function then exits the application
    """
    print()
    time.sleep(a)
    print("Thank you for playing " + name)
    print()
    time.sleep(b)
    print("See you again soon")
    print()
    time.sleep(c)
    quit()


def start():
    """
    This is the standard introduction for all players.
    Users will understand the purpose of the game and input their name.
    """
    clearConsole()
    title = pyfiglet.figlet_format("Escape The Dungeon", font="tombstone")
    print(title)
    print("Welcome to the dungeon")
    time.sleep(a)
    print("Can you escape in one piece?")
    time.sleep(a)
    print("What is your name?")
    time.sleep(a)
    print("We'll need to write something on your gravestone")
    time.sleep(a)
    print()
    global name
    name = input("Insert Username here: \n")
    print()
    print("Best of luck " + name)
    print()
    time.sleep(a)
    print("...you'll need it")
    print()
    print()
    time.sleep(a)
    print()
    print("Press 'i' to see the instructions")
    print()
    ready = input("Are you ready to begin? Y/N \n").lower().strip()

    if ready == "y":
        # This will start the game for the player using imready() function
        imready()

    elif ready == "n":
        # This will restart the game if players arent ready to play
        notready()

    elif ready == "i":
        """
         This will allow user to see the instructions to the game.
         This will help user to understand how to play
         """
        instructions()

    elif input == "c":
        # This will show the player the current items in their inventory
        inventory()

    elif input == "q":
        # This allows the player to exit the game
        fin()

    else:
        validation()
        ready = input("Are you ready to begin? Y/N \n").lower().strip()
        if ready == "y":
            imready()
        elif ready == "n":
            notready()
        elif ready == "q":
            fin()
        else:
            start()


def instructions():
    """
    This function is run to explain the gameplay to players
    The function will the automatically start the game
    """
    print()
    print("You are trapped in a foul dungeon")
    print()
    time.sleep(b)
    print("You must use logic and wit to escape")
    print()
    time.sleep(b)
    print("After each scenario you will be prompted to make a decision")
    print()
    time.sleep(b)
    print("Type the decision into the console to progress the story")
    print()
    time.sleep(c)
    print("If you type something else you will be prompted again")
    print()
    time.sleep(c)
    print("You also have an inventory during the game")
    print()
    time.sleep(c)
    print("Press 'c' to view your inventory during the game")
    print()
    time.sleep(c)
    print("If you want to exit the game at anytime press 'q'")
    print()
    print()
    time.sleep(c)
    print("Best of luck in Escape The Dungeon " + name)
    time.sleep(c)
    begin()


def begin():
    """
    This function sets the scene for the players.
    Players will then input their first decision
    """
    clearConsole()
    print("You wake up in a dark decrepid dungeon")
    time.sleep(a)
    print("Everything is shrouded in darkness")
    time.sleep(b)
    print("The dungeon is damp and slime covers the old stone walls")
    time.sleep(c)
    print("A small flame flickers across the dungeon")
    time.sleep(a)
    print("You try to move")
    time.sleep(b)
    print("Your feet have been shackled together")
    time.sleep(a)
    print("What will you do?")
    print()
    time.sleep(a)
    option1 = input("Do you 'move' or 'stay' where you are?\n").lower().strip()
    print()

    if option1 == "move":
        # take player to firstMove()
        firstMove()

    elif option1 == "stay":
        # resets the game if the player opts to stay
        time.sleep(a)
        print("Nothing happens")
        print()
        print("Your eyes start to close")
        print()
        time.sleep(b)
        print("Your body aches as you slowly drift into a slumber")
        time.sleep(c)
        begin()

    elif option1 == "c":
        # show items in the inventory and then reloop the function
        inventory()
        begin()

    elif option1 == "q":
        # allows the players to quit the fame
        fin()

    else:
        """
        This function runs if player inputs wrong option
        Function runs validation() to inform player to reinput
        Players are then reprompted with previous options
        """
        validation()
        print("What will you do?")
        print()
        time.sleep(a)
        option1 = input("Do you 'move' or 'stay'? \n").lower().strip()
        if option1 == "move":
            firstMove()
        elif option1 == "stay":
            time.sleep(a)
            print("Nothing happens")
            print()
            print("Your eyes start to close")
            print()
            time.sleep(b)
            print("Your body aches as you slowly drift into a slumber")
            time.sleep(c)
            begin()
        elif option1 == "c":
            inventory()
            begin()
        elif option1 == "q":
            fin()
        else:
            validation()
            print("What will you do? ")
            time.sleep(a)
            print()
            option1 = input("Do you 'move' or 'stay'? \n").lower().strip()
            print()


def firstMove():
    # This function allows the player to move across the room
    print("You try to move")
    print()
    time.sleep(a)
    print("Your body aches but you manage to stand")
    print()
    time.sleep(a)
    print("You shuffle across the floor towards the light")
    print()
    time.sleep(a)
    print("Your shackles clink as you make your way across the room")
    print()
    time.sleep(b)
    print("The light grows brighter")
    print()
    print()
    print("There is a torch on the wall")
    print()
    time.sleep(a)
    print("What do you do?")
    print()
    time.sleep(a)
    option2a = input("'Take' it or 'stay' where you are?  \n").lower().strip()

    if option2a == 'take':
        # take user to take function to progress the story line
        take()

    elif option2a == 'stay':
        # this function will take the player to the take function.
        print()
        print("You stand by the torch")
        print()
        time.sleep(a)
        print("The warmth of the torch is alluring")
        print()
        time.sleep(b)
        print("You reach out and take the torch")
        print()
        time.sleep(a)
        take()

    elif option2a == "c":
        # Shows items in the inventory and then reloops function
        inventory()
        firstMove()

    elif option2a == "q":
        # allows players to quit the game
        fin()

    else:
        # runs validation function and then reloops function
        validation()
        firstMove()


def take():
    """
    This function allows the user to take the torch and decide to stay or move
    This function also adds the torch to the inventory list
    """
    inventorylist.append('torch')
    print()
    time.sleep(a)
    print("You take the torch from it's sconce")
    print()
    print("You wave the torch and the room illuminates")
    print()
    time.sleep(b)
    print("The dungeon is grimy and damp")
    print("but you can only see half of it")
    time.sleep(b)
    print()
    option3 = input("Do you 'search' the dungeon or 'stay'?\n").lower().strip()
    print()

    if option3 == 'search':
        # take user to the search function
        search()

    elif option3 == 'stay':
        # this function gives players a second chance to search or wait
        print("You stay where you are")
        print()
        time.sleep(a)
        print("The torch continues to burn")
        time.sleep(a)
        print()
        wait = input("Do you 'search' the room or 'wait'?  \n").lower().strip()

        if wait == 'search':
            # take the user to the search function
            search()

        elif wait == 'wait':
            # if the player chooses this option the game will end
            print()
            time.sleep(a)
            print("You wait where you are")
            time.sleep(a)
            print()
            print()
            print("Nothing happens")
            time.sleep(b)
            print()
            print("The torch slowly burns out")
            time.sleep(b)
            print()
            print("You are thrust into darkness")
            time.sleep(b)
            print()
            print(Fore.RED + "GAME OVER")
            print()
            time.sleep(c)
            fin()

        elif wait == "c":
            # show users items in inventory and reloop function
            inventory()
            take()

        elif wait == "q":
            # allow players to quit the game
            fin()

        else:
            # inform player of wrong input and reloop function
            validation()
            take()

    elif option3 == "c":
        # show users items in inventory and reloop function
        inventory()
        take()

    elif option3 == "q":
        # allow players to quit the game
        fin()

    else:
        # inform player of wrong input and reloop function
        validation()
        take()


def search():
    """
    This function allows the player to search the room
    Players will find a set of keys on the wall
    Keys are then appended to inventory list
    """
    print("You shuffle across the room")
    print()
    time.sleep(a)
    print("The torch provides an ark of light in front of you")
    print()
    time.sleep(a)
    print("You reach the far wall and follow it around the near empty room")
    print()
    time.sleep(a)
    print("You come across a set of keys on the wall")
    inventorylist.append('keys')
    print()
    keys = input("Do you 'take' them or 'leave' them?  \n")

    if keys == 'take':
        # take users to the keyWest function to progress the storyline
        keyWest()

    elif keys == 'leave':
        # players leave keys and story stagnates. Reprompt to take key
        print()
        time.sleep(a)
        print("You leave the keys on the wall")
        print()
        print()
        print()
        time.sleep(b)
        print("Are you sure you don't want to take those keys?")
        key2 = input("Do you take the keys?   Y/N \n").lower().strip()

        if key2 == 'y':
            # take players to keyWest function to progress story
            keyWest()
        elif key2 == 'n':
            # end game as players leave keys behind twice
            print()
            print("You leave the keys where they are")
            time.sleep(a)
            print("Why would you do that?")
            time.sleep(b)
            print(Fore.RED + "GAME OVER")
            time.sleep(c)
            start()

        elif key2 == "c":
            # show inventory and reloop function
            inventory()
            search()

        elif key2 == "q":
            # end game
            fin()

    elif keys == "c":
        # show inventory and reloop function
        inventory()
        search()

    elif keys == "q":
        # end game
        fin()

    else:
        # inform player of wrong input and reloop function
        validation()
        search()


def keyWest():
    """
    This function allows players to unlock their shackles
    Players can now move freely
    Players will be given option to search or rest
    """
    print()
    print("You take the keys and crouch down")
    print()
    time.sleep(a)
    print()
    print("There are three keys on the key chain")
    print()
    time.sleep(a)
    print()
    print("You try the first key")
    time.sleep(b)
    print()
    print("nothing")
    print()
    time.sleep(a)
    print("You try the second key")
    print()
    time.sleep(b)
    print("Nothing")
    print()
    time.sleep(b)
    print()
    print("You try the final key")
    print()
    time.sleep(c)
    print()
    print("SUCCESS")
    time.sleep(b)
    print("You hear the lock click and the shackles spring off your feet")
    print()
    time.sleep(b)
    print("It feels good to be partly free")
    time.sleep(b)
    print()
    print("What will you do next?")
    time.sleep(b)
    print()
    choice = input("'Search' the room or 'rest'? \n").lower().strip()

    if choice == 'search':
        # player can search the room and are brought to findChest function
        findChest()

    elif choice == 'rest':
        # if player chooses to rest the game will end as this is a dead end
        print()
        print("You lie down on the slimy stone floor to rest")
        time.sleep(b)
        print()
        print("It's the last thing you ever do")
        print()
        print()
        time.sleep(b)
        print(Fore.RED + "GAME OVER")
        print()
        time.sleep(c)
        fin()

    elif choice == "c":
        # check inventory and then reloop function
        inventory()
        keyWest()

    elif choice == "q":
        # allows players to end the game and exit
        fin()

    else:
        # reprompt input and rerun function
        validation()
        keyWest()


def findChest():
    """
    Player finds a chest in this function
    Player has option to open the chest,
    or investigate a noise behind them.
    """
    print()
    print("With your new found freedom...")
    time.sleep(a)
    print()
    print("..and torch in hand you stride around the room")
    time.sleep(c)
    print()
    print("The dungeon is larger than you had originally suspected")
    time.sleep(c)
    print()
    print("Secluded in the back you find a large wooden chest")
    time.sleep(b)
    print()
    print("As you approach the chest you hear a noise behind you")
    print()
    time.sleep(c)
    check = input("Do you 'open' the chest or 'investigate' the noise?  \n")

    if check == 'open':
        # takes players to open chest function where they find weapons
        open_chest()

    elif check == 'investigate':
        # allows user to investigate noise but they're killed
        investigate()

    elif check == "c":
        # opens inventory and then reloops function
        inventory()
        findChest()

    elif check == "q":
        # ends game and allows player to exit
        fin()

    else:
        # reprompt input and rerun function
        validation()
        findChest()


def investigate():
    # function results in a game over as player is killed by goblin
    print()
    time.sleep(a)
    print("You turn around and make your way towards the noise")
    print()
    time.sleep(a)
    print("You make it halfway across the room")
    print()
    time.sleep(c)
    print("A black barbed arrow strikes your square in the chest")
    print()
    time.sleep(b)
    print("You fall to the ground")
    time.sleep(b)
    print()
    print("You look at the hole in your chest as blood seeps out...")
    print()
    time.sleep(b)
    print("... everything fades to black")
    time.sleep(c)
    print()
    print(Fore.RED + "GAME OVER")
    print()
    time.sleep(c)
    fin()


def open_chest():
    """
    In this function the player opens the chest.
    Player them has the option to select a weapon.
    The weapon input is a global variable.
    This allows it to be used later in the story.
    """
    print()
    time.sleep(b)
    print("You approach the old chest")
    print()
    time.sleep(b)
    print("You reach down and grab the rotten wood")
    print()
    time.sleep(b)
    print("You heave with all your might and lift the heavy lid")
    print()
    time.sleep(b)
    print("You wave the torch over the open chest")
    print()
    time.sleep(b)
    print("Steel glints in the torch light")
    print()
    time.sleep(b)
    print()
    print("Nestled in the chest you can see a sword and a spear")
    print()
    time.sleep(c)
    print("Choose your weapon")
    time.sleep(b)
    print()
    global weapon
    weapon = input("Do you take the 'sword' or the 'spear'?\n").lower().strip()

    if weapon == "sword":
        sword()

    elif weapon == "spear":
        spear()

    elif weapon == "c":
        inventory()
        open_chest()

    elif weapon == "q":
        fin()

    else:
        validation()
        open_chest()


def sword():
    """
    This function adds the sword item to players inventory.
    Player will be killed as the sword option is not
    a valid option to defeat the goblin in this story
    """
    inventorylist.append('sword')
    print()
    print("You take the " + weapon + " from the chest")
    print()
    time.sleep(b)
    print("The footsteps are close now")
    time.sleep(b)
    print("A faint light appears in the far corner of the dungeon..")
    time.sleep(b)
    print()
    print("..it grows closer")
    time.sleep(b)
    print()
    print("Suddenly a goblin steps out of a hidden corridor")
    time.sleep(b)
    print()
    print("They are holding a torch and a bow")
    time.sleep(c)
    print()
    print("What will you do? ")
    time.sleep(b)
    print()
    gobby = input("'Stay' or 'charge' at the goblin?   \n ").lower().strip()

    if gobby == "stay":
        stay_death()

    elif gobby == "charge":
        sword_death()

    elif gobby == "c":
        inventory()
        sword()

    elif gobby == "q":
        fin()

    else:
        validation()
        sword()


def sword_death():
    """
    Player attacks the goblin but is killed
    game ends using fin function
    """
    print()
    time.sleep(b)
    print()
    print("You steady yourself")
    time.sleep(b)
    print("You feel the weight of the sword in your hands")
    time.sleep(b)
    print()
    print("You charge at the goblin")
    time.sleep(b)
    print()
    print("You scream at the top of your lungs")
    time.sleep(b)
    print()
    print("You swing your sword")
    time.sleep(c)
    print()
    print("Your first swing connects")
    time.sleep(c)
    print()
    print("but the goblin is too fast for you")
    time.sleep(c)
    print()
    print("He parries quickly")
    time.sleep(b)
    print()
    print("He stabs you in the chest")
    time.sleep(c)
    print()
    print("You fall to the ground in a pool of your own blood")
    time.sleep(c)
    print()
    print(Fore.RED + "GAME OVER")
    time.sleep(c)
    fin()


def stay_death():
    """
    Player holds their ground
    Player is then slain by the goblin
    Game ends using fin function
    """
    print()
    time.sleep(b)
    print("You steady yourself and hold your ground")
    time.sleep(b)
    print()
    print("The goblin looks at you")
    time.sleep(b)
    print()
    print("He unsheathes a sword from its scabbard")
    time.sleep(b)
    print()
    print("The goblin charges across the dungeon")
    time.sleep(b)
    print()
    print("He swings his sword in one fluid motion")
    time.sleep(b)
    print()
    print("He chops your head clean off your shoulders")
    time.sleep(b)
    print()
    print("You never stood a chance..")
    time.sleep(c)
    print()
    print(Fore.RED + "GAME OVER")
    print()
    time.sleep(c)
    fin()


def spear():
    """
    This function runs if player selects spear as their weapon
    Spear is then added to inventory list.
    If player selects throw input option they win the game.
    If player selects stay input option they are killed.
    Stay function is the same for both sword and spear input
    """
    print()
    inventorylist.append("spear")
    print("You take the " + weapon + " from the chest")
    print()
    time.sleep(b)
    print("The footsteps are close now")
    time.sleep(b)
    print("A faint light appears in the far corner of the dungeon..")
    time.sleep(b)
    print()
    print("..it grows closer")
    time.sleep(b)
    print()
    print("Suddenly a goblin steps out of a hidden corridor")
    time.sleep(b)
    print()
    print("They are holding a torch and a bow")
    time.sleep(c)
    print()
    print("What will you do? ")
    time.sleep(b)
    print()
    spear_gang = input("'Stay' or 'throw' your spear ? \n").lower().strip()

    if spear_gang == "stay":
        # run stay_death function and player is killed
        stay_death()

    elif spear_gang == "throw":
        # take players to final input and ultimate victory
        impale()

    elif spear_gang == "c":
        # check inventory and then rerun the function
        inventory()
        spear()

    elif spear_gang == "q":
        # ends the game
        fin()

    else:
        # reprompt input from the user and rerun spear function
        validation()
        spear()


def impale():
    """
    This function ends the game.
    The player is victorious.
    Well done
    """
    print()
    time.sleep(b)
    print("You weigh the spear in your hand")
    time.sleep(b)
    print()
    print("You calculate the distance to the Goblin")
    time.sleep(b)
    print()
    print("You hoist the spear onto your shoulder like a javelin..")
    time.sleep(b)
    print(".. and throw it with all your might")
    time.sleep(c)
    print()
    print("You strike the goblin square in the chest")
    time.sleep(c)
    print()
    print("He is killed instantly")
    time.sleep(c)
    print()
    print("You make your way across the dungeon")
    time.sleep(b)
    print()
    print("You go to the area where the goblin appeared from")
    time.sleep(b)
    print()
    print("You find the secret passageway and begin to ascend")
    time.sleep(b)
    print()
    print("You find the exit and open the door")
    time.sleep(b)
    print()
    print("You shut as the strong sunlight burns your retina")
    time.sleep(b)
    print()
    print("The sun feels warm on your skin")
    time.sleep(b)
    print()
    print("Congratulations " + name + " you are finally free")
    print()
    time.sleep(c)


start()