from re import X
import cv2, tensorflow, os, keyboard as kb, time, cv2, numpy as np, random
from tensorflow import keras

foodReward = 10
bombPenalty = -10
movePenalty = -1

def makePlane(size, tile):
    row = []
    plane = []
    for i in range(1, size):
        row.append(tile)
    for i in range(1, size):
        plane.append(row.copy())
    return plane

def plant(array, val, find):
    y = random.randint(0, len(array)-1)
    x = random.randint(0, len(array[y])-1)
    while(array[y][x] != find):
        y = random.randint(0, len(array)-1)
        x = random.randint(0, len(array[y])-1)
    array[y][x]=val
    return array

class agent():
    def __init__(self, posx, posy):
        self.x = X
        self.y = y

class env:
    def __init__(self, size, food, bomb):
        self.size=size
        self.env = makePlane(size, 0)

        for i in range(0, food):
            self.env = plant(self.env, 1, 0)
        for i in range(0, bomb):
            self.env = plant(self.env, 3, 0)

    def get(self, x, y):
        return self.env[y][x]
    def set(self, x, y, val):
        self.env[y][x] = val

    def takeAction(self, agent, move):
        

    def show(self):
        for i in self.env:
            print(i)


earth = env(10, 3, 3)
earth.show()












































































