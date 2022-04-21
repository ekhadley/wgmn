from concurrent.futures import process
import tensorflow as tf, time, random, dwarf, bond, numpy as np
from tensorflow import keras

class agent:
    def __init__(self, env):
        self.env = env
        self.memories = []

    def genModels(self, disc, eps, ler):
        self.disc = disc
        self.eps = eps
        self.ler = ler

        self.net = keras.models.Sequential()
        self.net.add(keras.layers.Conv2D(32, (3,3), input_shape=(self.env.size, self.env.size, 1), activation = "relu"))
        self.net.add(keras.layers.Flatten())
        self.net.add(keras.layers.Dense(64))
        self.net.add(keras.layers.Dropout(.2))
        self.net.add(keras.layers.Dense(4, activation="linear"))
        
        self.targetNet = keras.models.clone_model(self.net)
        self.net.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])
        self.targetNet.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])

    def genAction(self):
        npEnv = np.array([r[:] for r in self.env.env])
        processedEnv = npEnv*1/9
        if np.random.uniform() < self.eps:
            return np.argmax(self.net.predict(processedEnv.reshape(-1, self.env.size, self.env.size, 1))), 'exploit'
        else:
            return random.choice([0, 1, 2, 3]), 'explore'

    def remember(self, memory):
        self.memories.append(memory)

    def sampleAction(self, action):
        state = [r[:] for r in self.env.env]
        reward, newEnv = self.env.simAction(action)
        return [state, action, reward, newEnv]