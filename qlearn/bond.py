import tensorflow as tf, time, random, dwarf, bond, numpy as np

class agent:
    def __init__(self, disc, eps, lr):
        self.disc = disc
        self.eps = eps
        self.lr = lr
        self.net = tf.Sequential()
