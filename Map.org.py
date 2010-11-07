import random

class Map:
    def __init__(self, width, height):
        #Make an empty 2D list
        h = [0]*height
        self.map = [h for i in range(width)]
        self.width = width
        self.height = height

    #Sets random values to 1
    def randomize(self, obstacles_number):
        assert obstacles_number <= self.width*self.height, "Number of obstacles %i is greater than size of map %i." % (obstacles_number, width*height)
        #Keep track of items so that you don't randomly select the same cell twice
        items = list(range(self.width*self.height))
        
        for obstacle in range(obstacles_number):
            #Pick a random cell in the map
            random_cell = items.pop(random.randint(0, len(items)-1))
            #Find out which coordinates this item maps to
            random_cell_x = random_cell % self.width
            random_cell_y = random_cell // self.width
            self.map[random_cell_x][random_cell_y] = 1
