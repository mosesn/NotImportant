class Torus:
    def __init__(self,rowSize,colSize):
        self.rows=rowSize
        self.cols=colSize
        self.rowPos=0
        self.colPos=0

    def up(self):
        self.rowPos-=1
        if(self.rowPos<0):
            self.rowPos=self.rows-1

    def down(self):
        self.rowPos+=1
        if(self.rowPos>=self.rows):
            self.rowPos=0

    def left(self):
        self.colPos-=1
        if(self.colPos<0):
            self.colPos=self.cols-1

    def right(self):
        self.colPos+=1
        if(self.colPos>=self.cols):
            self.colPos=0
'''
Do we want to make cols & rows globals?  Discuss.
'''
