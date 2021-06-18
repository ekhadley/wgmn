import serial, numpy, time, cv2, time, tensorflow as tf
from PIL import Image
import keras

model = tf.keras.models.load_model('C:\\Users\\ekhad\Desktop\\trained_model')


count = 15600

print('ANALYSIS STARTING . . .')
while 1:
    count += 1
    frame = cv2.imread('C:\\Users\\ekhad\\Desktop\\rawvid_backup\\frame' + str(count) + '.png')




    for i in range(11):
        for j in range(16):
            cut = frame[(40*i):((40*i) + 40), (40*j):((40*j) + 40)]

            image_from_array = Image.fromarray(cut, 'RGB')
            size_image = image_from_array.resize((40,40))
            p = numpy.expand_dims(size_image, 0)
            img = tf.cast(p, tf.float32)
            pred = model.predict_classes(img)
            
            print(pred)


            for m in range(40*i, 40*i+40):
                for n in range(40*j, 40*j+40):
                    if pred == 0:
                        frame[m][n][1] = 0
                        frame[m][n][0] = 255
                    else:
                        frame[m][n][1] = 255
                        frame[m][n][0] = 0

                    cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    1


    if count >= 17000:
        count = 15000



























































