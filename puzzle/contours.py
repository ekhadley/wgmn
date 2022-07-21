from PIL import Image
import cv2, random, time, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

#ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\pcs\\{i}.jpg") for i in range(25)]

t=time.time()
pcs = [pc(e) for e in imgs]
p = puzzle(pcs, (5,5))
print(f'preprocessing took {time.time()-t} seconds')

t = time.time()

p.bestPlacement()

print(f'solving took: {time.time()-t} seconds')

for i, z in enumerate(pcs):
    cv2.imshow(f'{i}', z.show(base=True, scale=.5))

cv2.waitKey(0)