from PIL import Image
import cv2, numpy as np
import funcs

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\allpc.jpg"))
target = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs\\done.jpg"))

read = funcs.reader()

points1, points2, matches, matchesMask, matchIndexes = read.findAndMatch(pcs, target, .6)
matchImg = read.genMatchImg(pcs, target, points1, points2, matches, matchesMask)

queryPos, targetPos = read.getMatchPositions(points1, points2, matches, matchesMask)

print(f"features matched: {sum(m[0] for m in matchesMask)}")

funcs.circles(matchImg, queryPos)
funcs.circles(matchImg, [(e[0] + len(pcs[0]), e[1]) for e in targetPos])

cv2.imwrite("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\matches.jpg", matchImg)

while 1:
#    cv2.imshow("pcs", cv2.resize(pcs, (430, 400)))
#    cv2.imshow("done", cv2.resize(done, (430, 400)))
    cv2.imshow("matched", cv2.resize(matchImg, (1200, 800)))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break