import cv2, piece, numpy as np
from funcs import *

path = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"
pc = cv2.imread(f"{path}\\turtle\\pc2cr.jpg", cv2.IMREAD_GRAYSCALE)
ref = cv2.imread(f"{path}\\turtle\\reference.jpg", cv2.IMREAD_GRAYSCALE)

pc = cv2.GaussianBlur(pc, (11,11), 50)
ref = cv2.GaussianBlur(ref, (11,11), 50)

pc = imscale(pc, .6)

scaled = scaleImgSet(pc, .5, .7, 25)
pcs, dims = [], []
for i in scaled:
    for j in range(4):
        i = np.rot90(i)
        pcs.append(i)
        dims.append(np.shape(i))

matches = multiMatch(ref, pcs)
print(matches[:,0:2])
#ref = rectangles(cv2.cvtColor(ref, cv2.COLOR_GRAY2BGR), [matches[0]], np.shape(matches[2]))
ref = rectangles(cv2.cvtColor(ref, cv2.COLOR_GRAY2BGR), matches[:,0], dims)


#for i, p in enumerate(pcs):
#    cv2.imshow(f"pc{i}", imscale(p, 1.2))
#    cv2.imshow("map", imscale(map, .2))
cv2.imshow("ref", imscale(ref, .15))
cv2.imshow("pc", imscale(pc, 1))
#for i,e in enumerate(matches[:,2]):
#    cv2.imshow(f'{i}', e)
cv2.waitKey(0)


















































































