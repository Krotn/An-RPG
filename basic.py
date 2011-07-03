class GameEntity:
    def __init__(name = ""):
        self.name = name

class GameItem(GameEntity):
    def __init__(name,stackable = True):
        super(GameItem,self).__init__(name = name)
        self.stackable = stackable