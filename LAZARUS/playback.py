import numpy, time, cv2, time
from PIL import Image

count = 9


while count > -1:
    time.sleep(0)
    count += 1

    path = 'D:\\lvid\\frame' + str(count) + ".png"

    frame = cv2.imread(path)

    print(path)
    try:
        cv2.imshow('frame', frame)
    except Exception:
        pass

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1





















































