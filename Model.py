from Player import *
from Torus import *
from Map import *

class Model:
    def __init__(self,tmpView,tmpCont,colSize=20,rowSize=20):
        global tilesize
        tilesize=5
        self.view=tmpView
        self.controller=tmpCont
        self.torus=Torus(colSize,rowSize)
        self.genMapping()
        self.playerX=0
        self.playerY=0

    def genMapping(self):
        self.mapping=Map(10,10)
        self.mapping.randomize(5)

    def fetch(self):
        self.view.repaint(self.mapping)

    def move(self,dir):
        if(dir==1):
            self.playerY-=tilesize
            if(self.playerY<0):
                self.playerY=self.mapping.getRows()-1
        elif(dir==2):
            self.playerX+=tilesize
            if(self.playerX>=self.mapping.getCols()):
                self.playerX=0
        elif(dir==3):
            self.playerX-=tilesize
            if(self.playerX<0):
                self.playerX=self.mapping.getCols()-1
        else:
            self.playerY+=tilesize
            if(self.playerY>=self.mapping.getRows()):
                self.playerY=0
