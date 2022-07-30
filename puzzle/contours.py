from tabnanny import check
from PIL import Image
import cv2, random, time, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle"
#ref = cv2.imread(f"{imgdir}\\turtle\\reference.jpg")
imgs = [cv2.imread(f"{imgdir}\\d\\{i}.png") for i in range(4)]
checker = cv2.imread(f"{imgdir}\\d\\checker.png")

gray = cv2.cvtColor(checker, cv2.COLOR_BGR2GRAY)
obj = np.zeros((6*6,3), np.float32)
obj[:,:2] = np.mgrid[0:6,0:6].T.reshape(-1,2)
blur = cv2.GaussianBlur(checker, (3,3), 50)
ret, pts = cv2.findChessboardCorners(blur, (6,6))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
corners = cv2.cornerSubPix(gray,pts, (11,11), (-1,-1), criteria)
checker = cv2.drawChessboardCorners(checker, (6,6), pts, True)
print(ret, pts)
ret, mtx, dst, rvecs, tvecs = cv2.calibrateCamera([obj], [pts], gray.shape, None, None)
h,  w = gray.shape[:2]
newmtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dst, (w,h), 0, (w,h))
new = cv2.undistort(checker, mtx, dst, None, newmtx)

t=time.time()
p = puzzle([pc(e) for e in imgs], (6,6))
print(f'preprocessing took {time.time()-t} seconds')

score, im = p.evalMatch((p.pcs[0], p.pcs[1]), (1,3), show=True)
print(score)

cv2.imshow('c', checker)
#cv2.imshow('new', new)
for i, z in enumerate(p.pcs):
    cv2.imshow(f'{i}', z.show(base=True, scale=.6))

cv2.waitKey(0)