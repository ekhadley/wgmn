import cv2, tensorflow, os, keyboard as kb, time, cv2, numpy as np
from tensorflow import keras


class env():
    def __init__(self):
        self.grid = []
        for i in range(0, 10):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.pos = [4, 8]
        self.grid[self.pos[1]][self.pos[0]] = 1
        self.actionspace = ['x', 'n', 'e', 's', 'w']
        self.action = None
        self.done = 0
        self.age = 0
        self.score = 0

    def choose(self):
        self.action = 0
        if kb.on_release_key('w'):
            self.action = 1            
        if kb.on_release_key('a'):
            self.action = 4            
        if kb.on_release_key('s'):
            self.action = 3            
        if kb.on_release_key('d'):
            self.action = 2
        print(self.action)
        return self.actionspace[self.action]

    def reset(self):
        pass

    def step(self, action):
        if action == 'N':
            self.grid[self.pos[1]][self.pos[0]] = 0
            self.pos[1] += 1
        if action == 'E':
            self.grid[self.pos[1]][self.pos[0]] = 0
            self.pos[0] += 1
        if action == 'S':
            self.grid[self.pos[1]][self.pos[0]] = 0
            self.pos[1] -= 1
        if action == 'W':
            self.grid[self.pos[1]][self.pos[0]] = 0
            self.pos[0] -= 1

    def display(self):
        img = np.array(self.grid)
        print(img)
        #cv2.imshow('img', img)


world = env()

while 1:
    world.reset()
    while not world.done:
        world.choose()
        world.step(world.choose())
        world.display()













































































