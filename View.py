from tkinter import *

class View:

    def __init__(self):
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

#        root = Tk()
#        canvas = Canvas(root, width=500, height=500)
#        canvas.pack()

    def showPosEvent(self,event):
        print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

    def onUpArrowKey(self,event):
        print('Got up arrow key press')

    def onLeftArrowKey(self,event):
        print('Got left arrow key press')

    def onRightArrowKey(self,event):
        print('Got right arrow key press')

    def onDownArrowKey(self,event):
        print('Got down arrow key press')

    def run(self):
        self.root.mainloop()

'''
Next, implement repaint
'''
