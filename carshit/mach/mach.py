
import keras, matplotlib as plt
import tensorflow as tf
from PIL import Image

import numpy, cv2, random, time

def scramble(lst):
    for i in range(1, 3*len(lst)-1):
        a = random.randint(1, len(lst)-1)
        b = random.randint(1, len(lst)-1)
        lst[a], lst[b] = lst[b], lst[a]


data = []

labels = ['sky', 'offroad', 'road', 'midline', 'rightedge']


print('COLLECTION STARTED . . .')

for i in range(1, 2001):
    if random.randint(0, 1) > 0:
        img = numpy.array(cv2.imread('C:\\Users\\ekhad\\Desktop\\training data\\btrain\\road\\road' + str(i) + '.png'))
        data.append([img, 1])
    else:
        img = numpy.array(cv2.imread('C:\\Users\\ekhad\\Desktop\\training data\\btrain\\road\\rightedge' + str(i) + '.png'))
        data.append([img, 1])


for i in range(1, 2001):
    if random.randint(0, 2) == 0:
        img = numpy.array(cv2.imread('C:\\Users\\ekhad\\Desktop\\training data\\btrain\\offroad\\offroad' + str(i) + '.png'))
        data.append([img, 0])
    else:
        img = numpy.array(cv2.imread('C:\\Users\\ekhad\\Desktop\\training data\\btrain\\offroad\\sky' + str(i) + '.png'))
        data.append([img, 0])



scramble(data)
scramble(data)



frames = []
tags = []
for i in range(0, len(data)-500):
    frames.append(data[i][0])
    tags.append(data[i][1])


frames = numpy.array(frames)
tags = numpy.array(tags)

f = []
t = []
for i in range(len(data)-500, len(data)):
    f.append(data[i][0])
    t.append(data[i][1])
    
f = numpy.array(f)
t = numpy.array(t)

tf.keras.optimizers.Adam(lr=.0001)

print('TRAINING STARTED . . .')
(x_train, y_train), (x_test, y_test) = (frames, tags), (f, t)

x_train = numpy.resize(x_train, (7500, 40, 40, 3))
y_train = numpy.resize(y_train, (7500, 1))

x_train = tf.keras.utils.normalize(x_train, axis=1, order=1)
x_test = tf.keras.utils.normalize(x_test, axis=1, order=1)

x_test = numpy.resize(x_test, (500, 40, 40, 3))
y_test = numpy.resize(y_test, (500, 1))

x_test = tf.keras.utils.normalize(x_test, axis=1, order=1)
y_test = tf.keras.utils.normalize(y_test, axis=1, order=1)

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(32, kernel_size=5, activation='relu', input_shape=(40,40,3)))
model.add(tf.keras.layers.Conv2D(16, kernel_size=5, activation='relu'))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train, y_train, epochs=15)

saver = input('SAVE MODEL? :')

if saver == 'y':
    model.save('C:\\Users\\ekhad\\Desktop\\trained_model')

































































































































