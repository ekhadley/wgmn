import random, numpy as np, datetime
from tensorflow import keras
from tensorflow.keras.callbacks import TensorBoard

#log_dir = "qlearn/qlearnlogs" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = "qlearn/qlearnlogs"
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

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
        self.net.add(keras.layers.Conv2D(64, (1,1), input_shape=(self.numtargets, 3, 1), activation = "relu"))
#        self.net.add(keras.layers.Conv2D(64, (3,3), input_shape=(self.size, self.size, 3, 1), activation = "relu"))
        self.net.add(keras.layers.Flatten())
        self.net.add(keras.layers.Dense(128))
        self.net.add(keras.layers.Dropout(.2))
        self.net.add(keras.layers.Dense(4, activation="linear"))
        
        self.targetNet = keras.models.clone_model(self.net)
        self.net.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])
        self.targetNet.compile(loss="mse", optimizer = keras.optimizers.Adam(lr=self.ler), metrics = ['accuracy'])

    def train(self):
        if len(self.memories) < self.memreq:
            return
        batch = random.sample(self.memories, self.batchSize)
        states, nextStates, moves, rewards = [], [], [], []
        for m in batch:
            states.append(m[0])
            nextStates.append(m[3])

        states = np.array(states)
        nextStates = np.array(nextStates)

        Qpredictions = self.net.predict(states.reshape(self.batchSize, self.numtargets, 3, 1))
        futureQPredictions = self.targetNet.predict(nextStates.reshape(self.batchSize, self.numtargets, 3, 1))

        print(Qpredictions[:])
        for i, (obs, action, reward, nextObs) in enumerate(batch):
            if self.env.step < self.env.epLen:
                Qpredictions[i][action] = reward + futureQPredictions[i][action]*self.eps
            else:
                Qpredictions[i][action] = reward
        print(Qpredictions[:])

        if self.env.step ==  self.env.epLen:
            if self.sinceUpdate == self.updateRate:
                self.sinceUpdate = 0
                self.updateTarget()
            else:
                self.sinceUpdate += 1

        #print(Qpredictions[:])
        self.net.fit(np.array(states).reshape(self.batchSize, self.numtargets, 3, 1), np.array(Qpredictions),
                    batch_size = self.batchSize, verbose=1, callbacks = None)

    def predict(self, obs):
        npObs = np.array(obs)[:]*.1
        return self.targetNet.predict(npObs.reshape(-1, self.numtargets, 3, 1))

    def genAction(self, show=False):
        npObs = np.array(self.env.getObs())[:]*.1

        if np.random.uniform() < self.eps:
            prediction = self.targetNet.predict(npObs.reshape(-1, self.numtargets, 3, 1))
            if show:
                print(prediction)
            return np.argmax(prediction), 'exploit'
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
