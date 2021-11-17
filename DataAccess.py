import csv
from Player import Player
from Room import Room

class DataAccess:
    @staticmethod
    def GetPlayerList():
        players = []
        with open('DataPlayers.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                players.append([row[0], row[1]])
        return players

    @staticmethod
    def LoadPlayer(playerId):
        player = None

        with open('DataPlayers.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            for row in reader:
                if int(playerId) == int(row[0]):
                    #load that players room
                    room = DataAccess.LoadRoom(row[2])
                    #instantiate the player
                    player = Player(row[0],row[1],room)

                    break

            if(player == None):
                raise Exception('Invalid Player ID passing into DataAccess..LoadPlayer()')  
                
        return player
    
    @staticmethod
    def LoadRoom(roomId):
        
        #print("LoadRoom(roomId)  Room ID " + roomId)
        room = None

        with open('DataRooms.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            room = None

            for row in reader:
                #print(row[0], row[1], row[3], row[4])
                if int(roomId) == int(row[0]):
                    room = Room(row[0],row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8])
                    break

            if room == None:
                raise Exception('Invalid Room ID passing into DataAccess.LoadRoom()') 

        return room

    @staticmethod
    def SavePlayerList(PlayerList):

        with open('DataPlayers.csv', 'w',) as csvfile:
            writer = csv.writer(csvfile)
        
            for p in PlayerList:
                writer.writerow([p.playerId, p.name, p.room])