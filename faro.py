import numpy, cv2, time, face_recognition as fr
from PIL import Image

vid = cv2.VideoCapture(0)

while 1:
    stime = time.time()
    ret, frame = vid.read()

    faces = fr.face_locations(frame)

    print(faces)

    if len(faces) > 0:
        cv2.rectangle(frame, (faces[0][0], faces[0][1]), (faces[0][2], faces[0][3]), (250, 10, 50), 3)

    cv2.imshow('frame', frame)

    #print(1/(time.time()-stime))
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1





















































