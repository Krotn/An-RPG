class GameEntity:
    def __init__(name = ""):
        self.name = name

class GameItem(GameEntity):
    def __init__(name):
        super(GameItem,self).__init__(name = name)