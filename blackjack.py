import random, time, math, cv2, numpy as np
from PIL import Image
from gym import Env
from gym.spaces import Discrete, Box

class env(Env):
    def __init__(self):
        self.pos = [random.randint(0, 100), random.randint(0, 100)]
        self.observationSpace = 1
        self.actionSpace = [random.randint(-1, 1), random.randint(-1, 1)]
        self.time = 0

    def step(self, action):
        self.pos[0] += self.actionSpace[0]
        self.pos[1] += self.actionSpace[1]

        reward = 100-math.sqrt(self.pos[0]**2 + self.pos[1]**2)

        self.pos[0] += random.uniform(-1, 1)    
        self.pos[1] += random.uniform(-1, 1)    

        self.time += 1
        if self.time == 1000:
            self.reset()

        return self.pos, 

    def reset(self):
        self.time = 0
        self.pos = [random.randint(0, 100), random.randint(0, 100)]


episodes = 100
e = env()

for i in range(episodes):






































