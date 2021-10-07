import cv2, numpy as np
import tensorflow
from tensorflow import keras


class env():
    def __init__(self):
        self.env = []
        for i in range(0, 10):
            self.env.append([])
            for j in range(0, 10):
                self.env[i-1].append([])

    def step(self):
        pass

    def display(self):
        pass


world = env()
print(world.env)
    
















































































