from re import X
import cv2, tensorflow, os, keyboard as kb, time, cv2, numpy as np, random
from tensorflow import keras

foodReward = 10
bombPenalty = -10
movePenalty = -1

blankTile = 0
foodTile = 1
bombTile = 3

foodCount = 3
bombCount = 3

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
        self.x = posx
        self.y = posy
        episodeReward = 0


class env:
    def __init__(self, size, food, bomb):
        self.size=size
        self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        

        self.env = makePlane(size, blankTile)
        for i in range(0, food):
            self.env = plant(self.env, foodTile, blankTile)
        for i in range(0, bomb):
            self.env = plant(self.env, bombTile, blankTile)

    def reset(self, food, bomb):
        self.env = makePlane(size, blankTile)
        for i in range(0, food):
            self.env = plant(self.env, foodTile, blankTile)
        for i in range(0, bomb):
            self.env = plant(self.env, bombTile, blankTile)
    def get(self, x, y):
        return self.env[y][x]
    def set(self, x, y, val):
        self.env[y][x] = val

    def takeAction(self, agent, move):
        moveDirection = self.moves[move]
        
        agent.x += moveDirection[0]
        agent.y += moveDirection[1]

        dest = self.get(agent.y, agent.y)
        
        if dest == blankTile:
            return movePenalty
        if dest == foodTile:
            return foodReward + movePenalty
        if dest == bombTile:
            return bombPenalty + movePenalty

    def show(self):
        for i in self.env:
            print(i)


earth = env(15, 1, 15)
earth.show()












































































