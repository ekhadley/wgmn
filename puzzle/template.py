from re import A
from PIL import Image
import cv2, numpy as np
from funcs import reader, puzzle, circles

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\pc1.jpg", cv2.IMREAD_GRAYSCALE))
target = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\reference.jpg", cv2.IMREAD_GRAYSCALE))

res = cv2.matchTemplate(target, pcs, cv2.TM_CCOEFF)
pos = np.unravel_index(np.argmax(res), np.shape(res))

print(pos)
cv2.rectangle(target, (pos[0], pos[1]),(pos[0]+len(pcs[0]), pos[1]+len(pcs)), (50, 0, 255), (15))

while 1:
    cv2.imshow("pcs", cv2.resize(pcs, (430, 400)))
    cv2.imshow("grid", cv2.resize(target, (1200, 1000)))
#    cv2.imshow("matched", cv2.resize(match, (1600, 800)))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


















































































