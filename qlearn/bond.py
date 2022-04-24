import tensorflow as tf, time, random, dwarf, bond, numpy as np
from tensorflow import keras

class agent:
    def __init__(self, env):
        self.env = env
        self.memories = []
        self.memlen = 100000
        self.memreq = 100
        self.numtargets = self.env.food + self.env.bomb
        self.batchSize = 64

    def genModels(self, discount, epsilon, learnRate,updateRate):
        self.disc = discount
        self.eps = epsilon
        self.ler = learnRate
        self.updateRate = updateRate

        self.net = keras.models.Sequential()
        self.net.add(keras.layers.Conv2D(64, (3,3), input_shape=(self.numtargets, 3, 1), activation = "relu"))
        self.net.add(keras.layers.Flatten())
        self.net.add(keras.layers.Dense(64))
        self.net.add(keras.layers.Dropout(.2))
        self.net.add(keras.layers.Dense(4, activation="linear"))
        
        self.targetNet = keras.models.clone_model(self.net)
        self.net.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])
        self.targetNet.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])

    def train(self):
        if len(self.memories) < self.memreq:
            return
        batch = random.sample(self.memories, self.batchSize)
        obs, moves, rewards, nextObs = np.array(batch[:,0]), batch[:,1], batch[:,2], np.array(batch[:,3])
        Qpredictions = self.model.predict(obs.reshape(self.batchSize, self.numtargets, 3, 1))
        futureQPredictions = self.model.predict(nextObs.reshape(self.batchSize, self.numtargets, 3, 1))
        

    def genAction(self):
        npObs = np.array(self.env.getObs())
        for e in npObs:
            e[1] *= .1
            e[2] *= .1
        if np.random.uniform() < self.eps:
            return np.argmax(self.net.predict(npObs.reshape(-1, self.numtargets, 3, 1))), 'exploit'
        else:
            return random.choice([0, 1, 2, 3]), 'explore'

    def updateModel(self):
        pass

    def remember(self, memory):
        self.memories.append(memory)
        if len(self.memories) > self.memlen:
            self.memories.pop(0)

    def sampleAction(self, action):
        obs = self.env.getObs()
        reward, newEnv = self.env.simAction(action)
        return [obs, action, reward, newEnv]
