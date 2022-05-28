from PIL import Image
import cv2, numpy as np
from functions import *

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\pc1cr.jpg"))
target = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\candy\\reference.jpg"))

solved = puzzle(target, 50, 40)
grid = solved.gridImg(width=15)

read = reader()
points1, points2, matches, matchesMask, matchIndexes = read.findAndMatch(pcs, target, .9)
matchImg = read.genMatchImg(pcs, target, points1, points2, matches, matchesMask)

queryPos, targetPos = read.getMatchPositions(points1, points2, matches, matchesMask)

circles(matchImg, queryPos)
circles(matchImg, [(e[0] + len(pcs[0]), e[1]) for e in targetPos])

#cv2.imwrite("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\matches.jpg", matchImg)
#print(f"features matched: {sum(m[0] for m in matchesMask)}")
while 1:
    cv2.imshow("matched", imscale(matchImg, .2))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break