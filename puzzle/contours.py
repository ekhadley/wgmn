from PIL import Image
import cv2, random, time, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"
#ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\pcs\\{i}.jpg") for i in range(25)]

checker = cv2.imread(f"{imgdir}\\turtle\\pcs\\checker.jpg")

t=time.time()
pcs = [pc(e) for e in imgs]
#puz = puzzle(pcs, (5,5))
print(f'preprocessing took {time.time()-t} seconds')

#asd = puz.bestFit((0,1))
#print(asd)
#q, rot, score = asd
#print(puz.evalPlacement(puz.pcs[21], (1, 0), 2))

for i, z in enumerate(pcs):
    cv2.imshow(f'{i}', z.show(base=True, scale=1))
    #cv2.imshow(f'w{i}', z.warped)

cv2.waitKey(0)