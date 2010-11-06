class Controller:
    def __init__(self,view):
        self.view=view

    def setModel(self,model):
        self.model=model

    def movePlayer(self,dir):
        self.model.move(dir)
