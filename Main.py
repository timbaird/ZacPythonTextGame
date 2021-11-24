import time
import os
from DataAccess import DataAccess
from Game import Game
from Menu import Menu


# a bit of start up fanciness for effect
os.system('clear')
print("Launching Game.")

## lengthen or shorten the start delay here
start_delay = 4

for i in range (1, start_delay):
    print(".")
    time.sleep(0.5)

#  main loop

while True:

    Menu.DisplayMainMenu()
    # VALIDATION OF MENU CHOICE INPUT HAPPENS INSIDE THE Menu.GetMainMenuChoice() METHOD SO NOT NEEDED HERE.
    mainMenuChoice = Menu.GetMainMenuChoice()
        
    if mainMenuChoice == "N": # new game
        Game.NewGame()
        time.sleep(3)

    elif mainMenuChoice == "L": #load game
        # get the list of current players
        playerList = DataAccess.GetPlayerList()

        # deal with the case where there is no existing players
        if len(playerList) == 0:
            print("There are no existing games, starting a new game")
            Game.NewGame()
        else:
            # ask the user which player they want to play
            loadPlayerChoice = Menu.GetPlayerChoice(playerList)
            #run the game for that player
            Game.Run(loadPlayerChoice)
        
    else: # exit game
        os.system('clear')
        print("Thanks for Playing\n")
        break
    
# end main loop




