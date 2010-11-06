class Torus:
    def __init__(self,colSize,rowSize):
        self.rows=rowSize
        self.cols=colSize
        self.rowPos=0
        self.colPos=0

    #moving up
    def up(self):
        self.rowPos-=1
        if(self.rowPos<0):
            self.rowPos=self.rows-1

    #moving down
    def down(self):
        self.rowPos+=1
        if(self.rowPos>=self.rows):
            self.rowPos=0

    #moving left
    def left(self):
        self.colPos-=1
        if(self.colPos<0):
            self.colPos=self.cols-1

    #moving right
    def right(self):
        self.colPos+=1
        if(self.colPos>=self.cols):
            self.colPos=0

    #return the number of rows, a sort of "Y-SIZE value"
    def getRows(self):
        return rows

    #return the number of cols, a sort of "X-SIZE value"
    def getCols(self):
        return cols

'''
Do we want to make cols & rows globals?  Discuss.
'''
