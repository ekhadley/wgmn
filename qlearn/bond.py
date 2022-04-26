import tensorflow as tf, random, numpy as np, datetime
from tensorflow import keras
from tensorflow.keras import tensorboard

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

class agent:
    def __init__(self, env, updateRate):
        self.env = env
        self.memories = []
        self.memlen = 100000
        self.memreq = 1000
        self.updateRate = updateRate
        self.sinceUpdate = 0
        self.numtargets = self.env.food + self.env.bomb
        self.batchSize = 500

    def genModels(self, discount, epsilon, learnRate):
        self.disc = discount
        self.eps = epsilon
        self.ler = learnRate

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
        states, moves, rewards, nextStates = [], [], [], []


        for m in batch:
            states.append(m[0])
            moves.append(m[1])
            rewards.append(m[2])
            nextStates.append(m[3])

        states = np.array(states)
        nextStates = np.array(nextStates)

        Qpredictions = self.net.predict(states.reshape(self.batchSize, self.numtargets, 3, 1))
        futureQPredictions = self.net.predict(nextStates.reshape(self.batchSize, self.numtargets, 3, 1))
        
        for i, (obs, move, reward, nextObs) in enumerate(batch):
            if self.env.step < self.env.epLen:
                maxFutureQ = np.max(futureQPredictions)
                newQ = reward + maxFutureQ*self.eps
            if self.env.step >= self.env.epLen:
                newQ = reward

            Qpredictions[i][move] = newQ

        if self.env.step ==  self.env.epLen:
            if self.sinceUpdate == self.updateRate:
                self.sinceUpdate = 0
                self.updateTarget()
            else:
                self.sinceUpdate += 1

        self.net.fit(np.array(states).reshape(self.batchSize, self.numtargets, 3, 1), np.array(Qpredictions), 
                     batch_size = self.batchSize, verbose=1, callbacks = [tensorboard_callback])

    def genAction(self):
        npObs = np.array(self.env.getObs())[:]*.1

        if np.random.uniform() < self.eps:
            return np.argmax(self.targetNet.predict(npObs.reshape(-1, self.numtargets, 3, 1))), 'exploit'
        else:
            return random.choice([0, 1, 2, 3]), 'explore'

    def updateTarget(self):
        self.targetNet.set_weights(self.net.get_weights())

    def remember(self, memory):
        self.memories.append(memory)
        if len(self.memories) > self.memlen:
            self.memories.pop(0)

    def sampleAction(self, action):
        obs = self.env.getObs()
        reward, newEnv = self.env.simAction(action)
        return [obs, action, reward, newEnv]
