from PIL import Image
import cv2, random, time, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"
#ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\turtle\\d\\{i}.jpg") for i in range(4)]

checker = cv2.imread(f"{imgdir}\\turtle\\d\\4.jpg", cv2.IMREAD_COLOR)

'''
row,col = np.where(cv2.inRange(checker, (45,12,21),(75,32,41))==[255])
pts = np.stack((col,row),axis=1).astype(np.float32)
obj = np.stack(((col-130)//52,(row-70)//55,[0]*len(col)),axis=1).astype(np.float32)
gray = cv2.cvtColor(checker, cv2.COLOR_BGR2GRAY)
ret, mtx, dst, rvecs, tvecs = cv2.calibrateCamera([obj], [pts], gray.shape, None, None)
h,  w = gray.shape[:2]
newmtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dst, (w,h), 0, (w,h))
new = cv2.undistort(checker, mtx, dst, None, newmtx)
'''

t=time.time()
pcs = [pc(e) for e in imgs]
puz = puzzle(pcs, (5,5))
print(f'preprocessing took {time.time()-t} seconds')

score, im = puz.evalMatch((pcs[0], pcs[1]), (2,2), show=True)
print(score)

cv2.imshow('match', im)
cv2.imshow('checker', checker)
#cv2.imshow('newchecker', new)
for i, z in enumerate(pcs):
    cv2.imshow(f'{i}', z.show(base=True, scale=.65))

cv2.waitKey(0)