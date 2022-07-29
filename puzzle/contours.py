from PIL import Image
import cv2, random, time, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle"
#ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\d\\{i}.jpg") for i in range(4)]

checker = cv2.imread(f"{imgdir}\\d\\4.jpg", cv2.IMREAD_COLOR)
inrange = cv2.inRange(checker, (40,10,15),(80,37,46))
row,col = np.where(cv2.inRange(checker, (40,10,15),(80,37,46))==[255])
pts = np.stack((col,row),axis=1).astype(np.float32)
obj = np.stack(((col-130)//52,(row-70)//55,[0]*len(col)),axis=1).astype(np.float32)
print(obj)
gray = cv2.cvtColor(checker, cv2.COLOR_BGR2GRAY)
ret, mtx, dst, rvecs, tvecs = cv2.calibrateCamera([obj], [pts], gray.shape, None, None)
h,  w = gray.shape[:2]
newmtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dst, (w,h), 0, (w,h))
new = cv2.undistort(checker, mtx, dst, None, newmtx)

t=time.time()
p = puzzle([pc(e) for e in imgs], (5,5))
print(f'preprocessing took {time.time()-t} seconds')

score, im = p.evalMatch((p.pcs[0], p.pcs[1]), (3,0), show=True, thickness=7)
print(score)

#checker = circles(checker, pts, radius=5,width=1,color=(255,10,150))
#cv2.imshow('checker', checker)
#cv2.imshow('newchecker', new)
cv2.imshow('m', imscale(im, .15))
for i, z in enumerate(p.pcs):
    cv2.imshow(f'{i}', z.show(base=True, scale=.15, thickness=15, radius=35))
    cv2.imshow(f'w{i}', imscale(z.warped, .15))

cv2.waitKey(0)