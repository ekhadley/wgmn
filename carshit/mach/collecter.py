import time, cv2, time, numpy
from PIL import Image

vid = cv2.VideoCapture(1)


while 1:
    ret, frame = vid.read()   
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        while cv2.waitKey(1) & 0xFF == ord('q'):
            1
'''
while 1:
    count += 1
    path = 'C:\\Users\\ekhad\\Desktop\\vid\\frame' + str(count) + '.png'

    img = cv2.imread(path)
    
    cv2.imwrite(path, img)     
    
    cv2.imshow('frame', img)

    print(count)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1
    if count > 5058:
        count = 0

'''
























































