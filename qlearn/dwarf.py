import cv2, numpy as np
import tensorflow
from tensorflow import keras




class env():
    def __init__(self):
        self.grid = []
        for i in range(0, 10):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        

    def step(self):
        pass

    def display(self):
       s = ''
       for i in range(len(self.grid)):
           print('\n')
           for j in range(len(self.grid[i])):
                s += str(self.grid[i][j])
                print(s)


world = env()

world.display()
















































































