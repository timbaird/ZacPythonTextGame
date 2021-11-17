from Player import Player
import sys
import time
import os
from DataAccess import DataAccess
from Menu import Menu

class Game:
    
    currentPlayer = None
    currentRoom = None

    @staticmethod
    def NewGame():
        
        # load the existing player list
        currentPlayers = DataAccess.GetPlayerList()

        # set up the new name variable for the loop
        newName = ""

        #to keep a track of the highest id found in the existing player list
        maxPlayerId = 0

        # loop untul a valid name is entered
        while newName == "":
            # ask the player for a new name
            newName = input("What is your name?:  ").upper()

            # if they enter a blank name  give error message
            if newName == "":
                print("Name cannot be blank")
            else:
                # check the name they entered against existsing names to ensure it is not already used
                for p in currentPlayers:
                    # check to see if this is highest player id yet and track if it is
                    if int(p[0]) > maxPlayerId:
                        maxPlayerId = int(p[0])
                    # check the new name against the name of this player to see if the same
                    if newName.lower() == p[1].lower():
                        newName = ""
                        print("That name is either already being used, try a different one")
                        break

        # once valid name is entered
        # add a new player to the list with max player id + 1 as player id, starting in room 1
        currentPlayers.append([maxPlayerId + 1, newName, 1])

        #print(currentPlayers)
        DataAccess.SavePlayerList(currentPlayers)
        Game.Run(maxPlayerId + 1)

    @staticmethod
    def GetPlayerList():
        return DataAccess.GetPlayerList()

    @staticmethod
    def Run(playerId):
        # load the nominated player

        Game.currentPlayer = DataAccess.LoadPlayer(playerId)
        
        # some theatrics
        os.system('clear')
        print("Loading " + Game.currentPlayer.name+ "'s Game")
        ## lengthen or shorten the start delay here
        start_delay = 4
        for i in range (1, start_delay):
            print(".")
            time.sleep(0.5)
        
        os.system('clear')

        print(Game.currentPlayer.look())

        # Game Loop

        while True:
            newRoomId = None
            time.sleep(1)
            print("\nH or Help to see list of possible actions")
            print("Q or Quit to exit game\n")

            action = input("What would you like to do?  ").upper()
        
            # deal with en game
            if (action[0] == "Q" or action == "QUIT"):
                Game.currentPlayer = None
                Game.currentRoom = None
                break

            elif(action[0] == "L" or action == "LOOK"):
                os.system('clear')
                print(Game.currentPlayer.look())

            elif(action[0] == "H" or action == "HELP"):
                os.system('clear')
                Menu.DisplayAvailableActionsHelpList()

            elif(action[0] == "M" or action[0, 3] == "MOVE"):
                os.system('clear')
                actionsplit = action.split()

                if(len(actionsplit) == 1):
                    print("You need to enter a direction to move in. see Help for details")
                    continue
                else:
                    if (actionsplit[1].upper() == "NORTH"):
                        newRoomId =  Game.currentPlayer.room.North()
                    elif  (actionsplit[1] == "SOUTH"):
                        newRoomId =  Game.currentPlayer.room.South()
                    elif  (actionsplit[1].upper() == "EAST"):
                        newRoomId =  Game.currentPlayer.room.East()
                    elif  (actionsplit[1].upper() == "WEST"):
                        newRoomId =  Game.currentPlayer.room.West()
                    elif  (actionsplit[1].upper() == "UP"):
                        newRoomId =  Game.currentPlayer.room.Up()
                    elif  (actionsplit[1].upper() == "DOWN"):
                        newRoomId =  Game.currentPlayer.room.Down()                
                    else:
                        os.system('clear')
                        print("Invalid Direction")
                        continue

                #print("new room id " + newRoomId)

                try:
                    int (newRoomId)
                    newRoom = DataAccess.LoadRoom(newRoomId)
                    Game.currentPlayer.move(newRoom)
                except Exception as e:
                    #print (e)
                    print("Sorry ... There is no way to go " + actionsplit[1])
                    continue

                os.system('clear')
                print(Game.currentPlayer.look())

            else:
                print("Invalid Action\n")
                continue

