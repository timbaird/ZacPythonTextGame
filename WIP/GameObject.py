class GameObject:
    def __init__(self, objectId, description = None):
        self.objectId = objectId
        self.description = description

    def Load(self):
        raise NotImplementedError(self.__class__.__name__ + '.Not Yet Implemented')
        
    def Save(self):
        raise NotImplementedError(self.__class__.__name__ + '.Not Yet Implemented')
