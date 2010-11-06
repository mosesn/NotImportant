'''
Deprecated, replaced by Program.py, replaced by View.py
MN
Stolen from somewhere online
'''

from Tkinter import *

def showPosEvent(event):
    print( 'Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def onUpArrowKey(event):
    print('Got up arrow key press')

def onLeftArrowKey(event):
    print('Got left arrow key press')

def onRightArrowKey(event):
    print('Got right arrow key press')

def onDownArrowKey(event):
    print('Got down arrow key press')

tkroot = Tk()
labelfont = ('courier', 20, 'bold')
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)
widget.bind('<Up>',onUpArrowKey)
widget.bind('<Down>',onDownArrowKey)
widget.bind('<Right>',onRightArrowKey)
widget.bind('<Left>',onLeftArrowKey)
widget.focus()
tkroot.title('Click Me')
tkroot.mainloop()
