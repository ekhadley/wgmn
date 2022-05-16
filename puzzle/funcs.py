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

        return (queryPos, targetPos)

    def ratioTest(self, matches, t):
        matchesMask = [[0, 0] for i in range(len(matches))]
        matchIndexes = []
        for i, (m,n) in enumerate(matches):
            if m.distance < t*n.distance:
                matchesMask[i]=[1,0]
                matchIndexes.append([i, m.trainIdx])
        return (matchesMask, matchIndexes)

class puzzle:
    def __init__(self, img, width, height):
        self.img = img
        self.imWidth = len(self.img[0])
        self.imHeight = len(self.img)
        self.width = width
        self.height = height

        self.pcWidth = round(self.imWidth/width)
        self.pcHeight = round(self.imHeight/height)

    def getCoordOf(self, x, y):
        return (round(x/self.width), round(y/self.height))

    def gridImg(self, width=15):
        grid = np.copy(self.img)
        for i in range(1, round(self.imWidth/self.pcWidth)):
            cv2.line(grid, (i*self.pcWidth, self.imHeight),  (i*self.pcWidth, 0), (0, 0, 0), width)
        for i in range(1, round(self.imHeight/self.pcHeight)):
            cv2.line(grid, (self.imWidth, i*self.pcHeight),  (0, i*self.pcHeight), (0, 0, 0), width)

        return grid

def circles(img, pos, radius=20, color=(20, 120, 220), width=7):
    for x, y in pos:
        x, y = round(x), round(y)
        cv2.circle(img, (x, y), radius, color, width)





































