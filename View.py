from tkinter import *

class View:

    def __init__(self):
        global tilesize
        tilesize=50
        self.root=Tk()
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.widget = Label(self.root, text='')
        self.widget.pack(expand=YES, fill=BOTH)
        self.widget.bind('<Up>',self.onUpArrowKey)
        self.widget.bind('<Down>',self.onDownArrowKey)
        self.widget.bind('<Right>',self.onRightArrowKey)
        self.widget.bind('<Left>',self.onLeftArrowKey)
        self.widget.focus()
        self.hasController=False
        self.hasModel=False
        self.hasGenPlayered=False
        self.hasInitMapping=False

    def setController(self,controller):
        self.controller=controller
        self.hasController=True

    def setModel(self,model):
        self.model=model
        self.hasModel=True
        self.getUpdates()

    def showPosEvent(self,event):
        print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

    def onUpArrowKey(self,event):
        if(self.hasController):
            self.controller.movePlayer(1)
        print("up")

    def onLeftArrowKey(self,event):
        if(self.hasController):
            self.controller.movePlayer(2)
        print("left")

    def onRightArrowKey(self,event):
        if(self.hasController):
            self.controller.movePlayer(3)
        print("right")

    def onDownArrowKey(self,event):
        if(self.hasController):
            self.controller.movePlayer(4)
        print("down")

    def run(self):
        self.root.mainloop()

    def getUpdates(self):
        if(self.hasModel):
            self.model.fetch()

    def repaint(self,mapping):
        print("repainting!")
        self.hasMapping=True
        self.mapping=mapping
        self.paintMapping()

    def paintMapping(self):
        if(self.hasModel):
            if(self.hasInitMapping):
                for i in range(self.mapping.getCols()):
                    for j in range(self.mapping.getRows()):
                        if(self.mapping.fetch(i,j)==1):
                            self.canvas.itemconfigure(self.tiles[i][j],fill="green")
                        else:
                            self.canvas.itemconfigure(self.tiles[i][j],fill="grey")
            else:
                self.hasInitMapping=True
                self.tiles=[[]]
                for i in range(self.mapping.getCols()):
                    self.tiles.append([])
                    for j in range(self.mapping.getRows()):
                        if(self.mapping.fetch(i,j)==1):
                            self.tiles[i].append(self.canvas.create_rectangle((i*tilesize,j*tilesize,(i+1)*tilesize,(j+1)*tilesize),fill="green"))
                        else:
                            self.tiles[i].append(self.canvas.create_rectangle((i*tilesize,j*tilesize,(i+1)*tilesize,(j+1)*tilesize),fill="grey"))
                self.hasInitMapping=True
            if(self.hasGenPlayered):
                x=self.model.playerX
                y=self.model.playerY
                self.canvas.coords(self.player,x*tilesize,y*tilesize,x*tilesize+tilesize,y*tilesize+tilesize)
            else:
                x=self.model.playerX
                y=self.model.playerY
                self.genPlayer(x,y)
                self.hasGenPlayered=True

    def genPlayer(self,x0=0,y0=0):
        print("generating player")
        if(not self.hasGenPlayered):
            self.player=self.canvas.create_rectangle((x0,y0,x0+tilesize,y0+tilesize),fill="blue")

    def getTileSize(self):
        return tilesize
