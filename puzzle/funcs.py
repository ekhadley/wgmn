from PIL import Image
import cv2, numpy as np

class reader:
    def __init__(self):
        self.sift = cv2.SIFT_create()

        self.flann = cv2.FlannBasedMatcher(dict(algorithm = 1, trees = 5), dict(checks=50))
    
    def genMatchImg(self, query, target, queryPoints, targetPoints, matches, matchesMask):
        draw_params = dict(matchColor = (0,255,0),
                        singlePointColor = (255,0,0),
                        matchesMask = matchesMask,
                        flags = cv2.DrawMatchesFlags_DEFAULT)
        
        return cv2.drawMatchesKnn(query, queryPoints, target, targetPoints, matches, None, **draw_params)

    def find(self, img):
        return self.sift.detectAndCompute(img, None)
    
    def match(self, desc1, desc2):
        return self.flann.knnMatch(desc1, desc2, k=2)

    def findAndMatch(self, query, target, t):
        pts1, desc1 = self.find(query)
        pts2, desc2 = self.find(target)
        matches = self.match(desc1, desc2)
        matchesMask, matchIndexes = self.ratioTest(matches, t)
        return pts1, pts2, matches, matchesMask, matchIndexes

    def getMatchPositions(self, points1, points2, matches, mask):
        queryPos = []
        targetPos = []
        for i, (m, n) in enumerate(matches):
            if mask[i][0] == 1:
                queryPos.append(points1[i].pt)
                targetPos.append(points2[matches[i][0].trainIdx].pt)

        return queryPos, targetPos

    def ratioTest(self, matches, t):
        matchesMask = [[0, 0] for i in range(len(matches))]
        matchIndexes = []
        for i, (m,n) in enumerate(matches):
            if m.distance < t*n.distance:
                matchesMask[i]=[1,0]
                matchIndexes.append([i, m.trainIdx])
        return matchesMask, matchIndexes

def circles(img, pos, radius=20, color=(20, 120, 220), width=7):
    for x, y in pos:
        x, y = round(x), round(y)
        cv2.circle(img, (x, y), radius, color, width)





































