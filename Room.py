class Room:
  def __init__(self, roomId, title, description, north, south, east, west, up, down):
    self.roomId = roomId
    self.title = title
    self.description = description

    if north.lower() == "none":
      self.north = None
    else:
      self.north = north

    if south.lower() == 'none':
      self.south = None
    else:
      self.south = south

    if east.lower() == "none":
      self.east = None
    else:
      self.east = east
    
    if west.lower() == 'none':
      self.west = None
    else:
      self.west = west

    if up.lower() == 'none':
      self.up = None
    else:
      self.up = up

    if down.lower() == 'none':
      self.down = None
    else:
      self.down = down
    
  
  def Description(self):
    return self.description

  def Title(self):
    return self.title

  def RoomId(self):
    return self.roomId
  
  def North(self):
    return self.north

  def South(self):
    return self.south

  def East(self):
    return self.east

  def West(self):
    return self.west

  def Up(self):
    return self.up

  def Down(self):
    return self.down
