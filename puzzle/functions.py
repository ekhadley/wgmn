import cv2, numpy as np

class pc:
    def __init__(self, im):
        self.im = im
        self.edge = self.findContours()
        self.corners = self.findCorners()
        self.sides = self.segment()
        self.straightSides = self.isStraight()
        self.attached = []
        [print(len(e)) for e in self.sides]

    def evalFit(self, o):
        fits = []
        mine = [[[e[0,0]-side[0,0,0], e[0,1]-side[0,0,1]] for e in side] for side in self.sides]
        other = [[[e[0,0]-side[0,0,0], e[0,1]-side[0,0,1]] for e in side] for side in o.sides]
        for i, a in enumerate(mine):
            for j, b in enumerate(other):
                if self.straightSides[i] or o.straightSides[j]:
                    fits.append(1000)
                elif dist(a[0], a[-1]) - dist(b[0], b[-1]) >= 10:
                    fits.append(1000)
                else:
                    diff = [dist(a[q], b[q]) for q in range(min(len(a), len(b)))]
                    fits.append(sum(diff)/len(diff))
        return fits

    def segment(self):
        closest = [0, 0, 0, 0]
        for i, p in enumerate(self.edge):
            for j, c in enumerate(self.corners):
                if dist(c, p) < dist(c, self.edge[closest[j]]):
                    closest[j] = i
        closest = sorted(closest)
        return [self.edge[closest[0]:closest[1]], self.edge[closest[1]:closest[2]],
                      self.edge[closest[2]:closest[3]], np.vstack((self.edge[closest[3]:-1],self.edge[0:closest[0]]))]

    def isStraight(self):
        straightmask = []
        for e in self.sides:
            if len(e) < 50:
                straightmask.append(1)
            else:
                straightmask.append(0)
        return straightmask

    def findContours(self):
        contours, heirarchy = cv2.findContours(self.im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [e for e in contours if len(e) > 60]
        cv2.fillPoly(self.im, contours, color=(255))
        return contours[0]
 
    def findCorners(self):
        cornerMap = cv2.cornerHarris(self.im, 12, 5, .01)
        y, x = np.where(cornerMap>.3*np.max(cornerMap))
        candidates = np.float32(np.array([[x[i], y[i]] for i in range(len(x))]))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret, label, centers=cv2.kmeans(candidates, 4, np.array([1,2,3,4]), criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        return centers
        '''
        for i in centers:
            x, y = round(i[0]), round(i[1])
            localmax = np.unravel_index(np.argmax(cornerMap[y-10:y+10,x-10:x+10]), (20, 20))
            self.corners.append((localmax[0] + i[0]-10, localmax[0] + i[1]-10))
        '''

    def show(self, scale=1, edges = False, corners = False):
        mod = cv2.cvtColor(np.copy(self.im), cv2.COLOR_GRAY2RGB)
        if (edges and len(self.edge) == 0) or (corners and len(self.corners) == 0):
            print("(requested elements have not been detected)")
            return imscale(mod, scale)
        if edges:
            if len(self.sides) > 0:
                for i, e in enumerate(self.sides):
                    #mod = cv2.drawContours(mod, [e], -1, (250-50*i, 150-50*i, 80*i), 3)
                    mod = cv2.polylines(mod, [e], False, (250-50*i, 150-50*i, 80*i), 3)
            else:
                #mod = cv2.drawContours(mod, [self.edge], -1, (250, 150, 0), 3)
                mod = cv2.polylines(mod, [self.edge], False, (250-50*i, 150-50*i, 80*i), 3)
        if corners:
            circles(mod, self.corners, radius=5, width=2)
        return imscale(mod, scale)

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

def dist(a,b):
    return np.linalg.norm(np.array(a)-np.array(b))

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
    subdims = (sampledim[0]//dim[1], sampledim[1]//dim[0])
    subs = []
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
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

def circles(img, pos, radius=20, color=(20, 120, 220), width=7):
    for e in pos:
        x, y = round(e[0]), round(e[1])
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

