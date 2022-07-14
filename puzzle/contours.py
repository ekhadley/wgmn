from PIL import Image
import cv2, random, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\d\\{i}.jpg") for i in range(5, 7)]


pcs = [pc(e) for e in imgs]
p = puzzle(pcs, (2, 2))
#fit, im = pcs[0].evalMatch(pcs[1], (0, 0), show=True)
#print(fit)

im = pcs[0].base
w, h, d = np.shape(im)

pts = np.array(pcs[0].corners, np.float32)
outwidth = max(dist(pts[0], pts[1]), dist(pts[2], pts[3]))
outheight = max(dist(pts[0], pts[2]), dist(pts[1], pts[3]))
print(outwidth, outheight)
d = np.array([[0, 0], [outwidth, 0], [0, outheight], [outwidth, outheight]], np.float32)

warp = cv2.getPerspectiveTransform(pts, d)
im = cv2.warpPerspective(im, warp, (im.shape[1], im.shape[0]))

cv2.imshow('corrected', im)
cv2.imshow('pc2', pcs[0].show(base=True))
#cv2.imshow('pc3', pcs[3].show(base=False))
#for i, z in enumerate(pcs):
#    cv2.imshow(f'{i}', z.show(base=True))
cv2.waitKey(0)