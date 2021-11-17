import time
import os
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
    mainMenuChoice = Menu.GetMainMenuChoice()
        
    if mainMenuChoice == "N": # new game
        Game.NewGame()
        time.sleep(3)

    elif mainMenuChoice == "L": #load game
        # get the list of current players
        playerList = Game.GetPlayerList()
        # ask the user which player they want to play
        loadPlayerChoice = Menu.GetPlayerChoice(playerList)
        #run the game for that player
        Game.Run(loadPlayerChoice)
        
    else: # exit game
        os.system('clear')
        print("Thanks for Playing\n")
        break
    
# end main loop




