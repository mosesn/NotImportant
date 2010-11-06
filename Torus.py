class Torus:
    def __init__(self,rowSize,colSize):
        rows=rowSize
        cols=colSize
        rowPos=0
        colPos=0

    def up(self):
        rowPos--
        if(rowPos<0):
            rowPos=rows-1

    def down(self):
        rowPos++
        if(rowPos>=rows):
            rowPos=0

    def left(self):
        colPos--
        if(colPos<0):
            colPos=cols-1

    def right(self):
        colPos++
        if(colPos>=cols):
            colPos=0

