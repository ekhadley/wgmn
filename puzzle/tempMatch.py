from PIL import Image
import cv2, numpy as np
from functions import *

pc = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\pc4cr.jpg", cv2.IMREAD_GRAYSCALE))
ref = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\reference.jpg", cv2.IMREAD_GRAYSCALE))

#pc = imscale(pc, 1/4)

pcs = [pc]
dims = [np.shape(pc)]
for i in range(1, 21):
    x = imscale(pc, i/20)
    for j in range(0, 4):
        x = np.rot90(x)
        pcs.append(x)
        dims.append(np.shape(x))

m = multiMatch(ref, pcs, bestOnly=True)
print(m)

ref = rectangles(cv2.cvtColor(ref, cv2.COLOR_GRAY2BGR), [m[0]], np.shape(pc))

while 1:
    for i, p in enumerate(pcs):
        cv2.imshow(f"pc{i}", imscale(p, 1.2))

#    cv2.imshow("map", imscale(map, .2))
    cv2.imshow("target", imscale(ref, .35))
#    cv2.imshow("matched", imscale(res, .1))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break


















































































