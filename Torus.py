from Map import *

class Torus:
    def __init__(self,colSize,rowSize):
        self.rows=rowSize
        self.cols=colSize
        self.rowPos=0
        self.colPos=0
        self.zones=[[]]
        self.genMapping()

    #moving up
    def up(self):
        self.rowPos-=1
        if(self.rowPos<0):
            self.rowPos=self.rows-1
        self.genMapping()

    #moving down
    def down(self):
        self.rowPos+=1
        if(self.rowPos>=self.rows):
            self.rowPos=0
        self.genMapping()

    #moving left
    def left(self):
        self.colPos-=1
        if(self.colPos<0):
            self.colPos=self.cols-1
        self.genMapping()

    #moving right
    def right(self):
        self.colPos+=1
        if(self.colPos>=self.cols):
            self.colPos=0
        self.genMapping()

    #return the number of rows, a sort of "Y-SIZE value"
    def getRows(self):
        return self.rows

    #return the number of cols, a sort of "X-SIZE value"
    def getCols(self):
        return self.cols

    def getMapping(self):
        return self.zones[self.colPos][self.rowPos]

    #generates a new map for the torus
    def genMapping(self):
        print(self.colPos,",",self.rowPos)
        if(self.colPos>=len(self.zones)):
            while(self.colPos>=len(self.zones)+1):
                self.zones.append(None)    
            self.zones.append([])
        elif(self.zones[self.colPos]==None):
            self.zones[self.colPos]=[]

        if(self.rowPos>=len(self.zones[self.colPos])):
            while(self.rowPos>len(self.zones[self.colPos])):
                self.zones[self.colPos].append(None)
            self.zones[self.colPos].append(Map(10,10))
            self.zones[self.colPos][self.rowPos].randomize(5)
        elif(self.zones[self.colPos][self.rowPos]==None):
            self.zones[self.colPos][self.rowPos]=Map(10,10)
            self.zones[self.colPos][self.rowPos].randomize(5)


'''
Do we want to make cols & rows globals?  Discuss.
'''
