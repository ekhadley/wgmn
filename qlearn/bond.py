import tensorflow as tf, time, random, dwarf, bond, numpy as np
from tensorflow import keras

class agent:
    def __init__(self, env, disc, eps, lr):
        self.disc = disc
        self.eps = eps
        self.lr = lr

        self.env = env

        self.initialWeights = np.random.uniform()
        self.net = keras.models.Sequential()
        self.net.add(keras.layers.Conv2D(32, input_shape=(self.env.size, self.env.size, 1), activation = "relu"))