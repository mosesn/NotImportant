from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def onUpArrowKey(event):
    print('Got up arrow key press')

def onLeftArrowKey(event):
    print('Got left arrow key press')

def onRightArrowKey(event):
    print('Got right arrow key press')

def onDownArrowKey(event):
    print('Got down arrow key press')

widget = Label(root, text='')
widget.pack(expand=YES, fill=BOTH)
widget.bind('<Up>',onUpArrowKey)
widget.bind('<Down>',onDownArrowKey)
widget.bind('<Right>',onRightArrowKey)
widget.bind('<Left>',onLeftArrowKey)

widget.focus()

root.mainloop()
