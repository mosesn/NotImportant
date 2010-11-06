from View import *
from Player import *
from Torus import *
from Map import *
from Model import *
from Controller import *

view=View()
controller=Controller(view)
view.setController(controller)
model=Model(view,controller)
view.setModel(model)
controller.setModel(model)


view.run()


#player=Player("Quentin",10,4,2)

