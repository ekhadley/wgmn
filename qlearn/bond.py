import tensorflow as tf, time, random, dwarf, bond, numpy as np
from tensorflow import keras

class agent:
    def __init__(self, env):
        self.env = env
        self.memories = []

    def genModel(self, disc, eps, ler):
        self.disc = disc
        self.eps = eps
        self.ler = ler

        self.net = keras.models.Sequential()
        self.net.add(keras.layers.Conv2D(32, (3,3), input_shape=(self.env.size, self.env.size, 1), activation = "relu"))
        self.net.add(keras.layers.Flatten())
        self.net.add(keras.layers.Dense(64))
        self.net.add(keras.layers.Dense(4, activation="linear"))
        self.net.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])

    def chooseAction(self):
        if np.random.uniform() < self.eps:
            return self.net.predict(np.array(self.env.state))
        else:
            return random.choice([0, 1, 2, 3])
        
    def doAction(self, action):
        reward = self.env.applyAction(action)