from PIL import Image
import cv2, numpy as np

def imscale(img, s):
    return cv2.resize(img, (round(len(img[0])*s), round(len(img)*s)))

def multiMatch(target, queries):
    r = []
    for query in queries:
        r.append(match(target, query))
    '''
    for j in range(round(len(r)/2)):
        max = 0
        min = len(r)
        for i in range(j, len(r)-j):
            if r[i][1] > r[max][1]:
                max = i
            if r[i][1] < r[min][1]:
                min = i

        print(len(r), min, max, sep = ", ")
        
        r[j], r[max] = r[max], r[j]
        r[len(r)-j], r[min] = r[min], r[len(r)-j]
    '''
    return np.array(r)

def countColor(img, channel, lower, upper):
    inrange = 0
    for e in img:
        for j in e:
            if j[channel] in range(lower, upper):
                inrange += 1
    return inrange

def avgColor(img):
    c1, c2, c3, num = 0, 0, 0, 0
    for r in img:
        for j in r:
            c1 += j[0]
            c2 += j[1]
            c3 += j[2]
            num += 1
    numPixels = len(img)*len(img[1])
    return [c1/numPixels, c2/numPixels, c3/numPixels]

def scaleImgSet(img, lower, upper, steps):
    inc = (upper-lower)/steps
    imgs = []
    for i in range(steps+1):
           imgs.append(imscale(img, lower+inc*i))
    return imgs


def bestMatch(target, queries):
    matches = multiMatch(target, queries)
    best = 0
    for i, e in enumerate(matches):
        if matches[i][1] > matches[best][1]:
            best = i
    return matches[best]


def match(target, query, retMap = False):
    map = cv2.matchTemplate(target, query, cv2.TM_CCOEFF_NORMED)
    minSim, maxSim, minSimPos, maxSimPos = cv2.minMaxLoc(map)
    return ((maxSimPos, map[maxSimPos[1]][maxSimPos[0]], query, map) if retMap else (maxSimPos, map[maxSimPos[1]][maxSimPos[0]], query))


def splitImage(img, dim):
#    sampledim = (len(img[0]), len(img))
    sampledim = np.shape(img)
    subdims = (sampledim[1]//dim[0], sampledim[0]//dim[1])

    subs = []
    for j in range(dim[0]):
        for i in range(0, dim[1]):
            subs.append(img[subdims[0]*j:subdims[0]*(j+1), subdims[1]*i:subdims[1]*(i+1),])

    return subs

def com(img):
    x, y = [], []
    for i, e in enumerate(img):
        for j, k in enumerate(e):
            if k != 0:
                x.append(j)
                y.append(i)
    try:
        return (sum(x)//len(x), sum(y)//len(y))
    except ZeroDivisionError:
        return (0, 0)


def rectangles(img, posList, dim, weight=5, color=(90, 0, 255)):
    for i, pos in enumerate(posList):
        if type(dim) == tuple:
            cv2.rectangle(img, pos, (pos[0] + dim[0], pos[1] + dim[1]), color, weight)
        if type(dim) == list:
            cv2.rectangle(img, pos, (pos[0] + dim[i][0], pos[1] + dim[i][1]), color, weight)
    return img

def rect(img, pos, dim, weight=15, color=(150, 0, 255)):
    cv2.rectangle(img, pos, (pos[0] + dim[0], pos[1] + dim[1]), color, weight)
    return img

def circles(img, pos, radius=20, color=(20, 120, 220), width=7):
    for x, y in pos:
        x, y = round(x), round(y)
        cv2.circle(img, (x, y), radius, color, width)




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

































