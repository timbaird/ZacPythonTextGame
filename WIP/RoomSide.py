
class RoomSide:
  def __init__(self, desc = None, 
                     destinationId = None,
                     door = None):
    self.desc = desc
    self.destinationId= destinationId
    self.door = door

    def look(self):
        if self.desc == None:
            return "You see nothing in particular"
        else:
            return self.desc
    
    def go(self):
        if self.destinationId == None:
            return "There is nowhere to go here"
        else:
            if self.door == None:
                return destinationId
            elif:
                self.door


