import os
import time

class Menu:
    @staticmethod
    def DisplayMainMenu():
        os.system('clear')
        print("MAIN MENU")
        print("-----------")
        print("[N]ew Game")
        print("[L]oad Game")
        print("[Q]uit")
        print("-----------")

    @staticmethod
    def GetMainMenuChoice():
        valid_choices = ["N", "L", "Q"]
        
        choice = input("Please make a choice :  ").upper()

        while choice not in valid_choices:
            os.system('clear')
            print("Invalid Choice\n")
            time.sleep(1)
            Menu.DisplayMainMenu()
            choice = input("Please make a choice :  ").upper()

        return choice

    @staticmethod
    def DisplayPlayerMenu(players):
        valid_choices = []

        os.system('clear')
        print("CHOOSE A PLAYER")
        print("-----------")
        for i in range (0, len(players)):
            valid_choices.append(str(players[i][0]))
            print("[" + str(players[i][0]) + "] - " + players[i][1])
        print("-----------")

        return valid_choices


    @staticmethod
    def GetPlayerChoice(players):

        valid_choices = Menu.DisplayPlayerMenu(players)

        choice = input("Please choose a player:  ").upper()

        while choice not in valid_choices:
            os.system('clear')
            print("Invalid Choice\n")
            time.sleep(1)
            valid_choices = Menu.DisplayPlayerMenu(players)
            choice = input("Please choose a player:  ").upper()

        return choice

    @staticmethod 
    def DisplayAvailableActionsHelpList():
        print("\nAVAILABLE ACTIONS:\n")
        print("LOOK => look around the area / room you are in")
        print("MOVE <direction> => move in nominated direction valid choices are :(north, south, east, west, up, down)")
        print("QUIT => Leave the game\n")