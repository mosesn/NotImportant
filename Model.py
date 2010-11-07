from Player import *
from Torus import *
from Map import *

class Model:
    def __init__(self,tmpView,tmpCont,colSize=20,rowSize=20):
        global tilesize
        tilesize=tmpView.getTileSize()
        self.view=tmpView
        self.controller=tmpCont
        self.torus=Torus(colSize,rowSize)
        self.genMapping()
        self.playerX=0
        self.playerY=0

    #generates a new map for the model
    def genMapping(self):
        self.mapping=self.torus.getMapping()

    #tells the view that something has changed internally
    #maybe should be renamed?
    def fetch(self):
        self.view.repaint(self.mapping)

    def move(self,dir):
        #up
        if(dir==1):
            self.playerY-=1
            if(self.playerY<0):
                self.torus.up()
                self.genMapping()
                self.playerY=self.mapping.getRows()-1
        #left
        elif(dir==2):
            self.playerX-=1
            if(self.playerX<0):
                self.torus.left()
                self.genMapping()
                self.playerX=self.mapping.getCols()-1
        #right
        elif(dir==3):
            self.playerX+=1
            if(self.playerX>=self.mapping.getCols()):
                self.torus.right()
                self.genMapping()
                self.playerX=0
        #down
        else:
            self.playerY+=1
            if(self.playerY>=self.mapping.getRows()):
                self.torus.down()
                self.genMapping()
                self.playerY=0
        self.fetch()
