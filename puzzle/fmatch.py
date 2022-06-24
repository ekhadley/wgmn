from PIL import Image
import cv2, numpy as np
from funcs import *
from featreader import *

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\pc2cr.jpg"))
target = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\turtle\\reference.jpg"))


read = reader()
points1, points2, matches, matchesMask, matchIndexes = read.findAndMatch(pcs, target, 1)
matchImg = read.genMatchImg(pcs, target, points1, points2, matches, matchesMask)

queryPos, targetPos = read.getMatchPositions(points1, points2, matches, matchesMask)

circles(matchImg, queryPos)
circles(matchImg, [(e[0] + len(pcs[0]), e[1]) for e in targetPos])

#cv2.imwrite("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\matches.jpg", matchImg)
#print(f"features matched: {sum(m[0] for m in matchesMask)}")
cv2.imshow("matched", imscale(matchImg, .2))
cv2.waitKey(0)