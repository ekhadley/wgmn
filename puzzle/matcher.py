from PIL import Image
import cv2, numpy as np

pcs = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\pc3.jpg"))
done = np.array(cv2.imread("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\done.jpg"))

sift = cv2.SIFT_create()
points1, desc1 = sift.detectAndCompute(pcs, None)
points2, desc2 = sift.detectAndCompute(done, None)

flann = cv2.FlannBasedMatcher(dict(algorithm = 1, trees = 5), dict(checks=50))
matches = flann.knnMatch(desc1,desc2,k=2)

matchesMask = [[0, 0] for i in range(len(matches))]
matchIndex = []
for i, (m,n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        matchesMask[i]=[1,0]
        matchIndex.append(i)

print(f"features matched: {sum(m[0] for m in matchesMask)}")

queryMatchPos = [points1[i].pt for i in matchIndex]
targetMatchPos = [points2[i].pt for i in matchIndex]

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = cv2.DrawMatchesFlags_DEFAULT)

matchImg = cv2.drawMatchesKnn(pcs, points1, done, points2, matches, None, **draw_params)

for x, y in queryMatchPos:
    x, y = round(x), round(y)
    cv2.circle(matchImg, (x, y), 20, (20, 120, 220), 7)

for x, y in targetMatchPos:
    x, y = round(x) + len(pcs[0]), round(y)
    cv2.circle(matchImg, (x, y), 20, (20, 120, 220), 7)

cv2.imwrite("C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\matches.jpg", matchImg)

while 1:
#    cv2.imshow("pcs", cv2.resize(pcs, (430, 400)))
#    cv2.imshow("done", cv2.resize(done, (430, 400)))
    cv2.imshow("matched", cv2.resize(matchImg, (1200, 800)))

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break