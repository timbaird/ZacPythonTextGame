class Player:
    def __init__(self, playerId, name, room):
        self.playerId = playerId
        self.name = name
        self.room = room


    def look(self):
        return "-------------------\n" + self.room.Title() + "\n-------------------\n\n" + self.room.Description() + "\n\n-------------------\n\n" + self.room.GetExits() +  "\n\n-------------------"

    def move(self, newRoom):
        self.room = newRoom
        self.look()