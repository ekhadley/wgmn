import numpy, time, cv2, time
from PIL import Image

vid = cv2.VideoCapture(0)
c = 0
while 1:
    ret, frame = numpy.array(vid.read())

    path = f"C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\pcs\\{c}.jpg"

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        cv2.imwrite(path, frame)
        c += 1
        time.sleep(1)





















































