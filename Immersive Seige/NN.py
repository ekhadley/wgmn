import keras,cv2, numpy, tensorflow as tf
from PIL import Image
import matplotlib as plt

print("BLEEP_BLOOP")
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train, y_train, epochs=1)
model.save

'''
img = cv2.imread('G:\\rocky\\mnist.jpg')
img = cv2.resize(img, (28, 28))
img.reshape(-1, 28, 28, 1)
cv2.imshow('img', img)
cv2.destroyAllWindows()
'''

result = model.predict([x_test[13]])
print(result)