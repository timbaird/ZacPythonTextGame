class Player:
    def __init__(self, playerId, name, room):
        self.playerId = playerId
        self.name = name
        self.room = room


    def look(self):
        return self.room.Title() + "\n\n" + self.room.Description()    

    def move(self, newRoom):
        self.room = newRoom
        self.look()