import math, random, timeit, cv2, numpy as np
from re import A
from cv2 import cornerMinEigenVal
from funcs import *

class pc:
    def __init__(self, im):
        self.im = self.preprocess(im)
        self.edge = self.findContours()
        self.corners = self.findCorners()
        self.sides = self.segment()
        self.straightSides = self.isStraight()
        #self.locks = self.lockPoints()
        self.locks = []
        
        self.centroid = [sum(self.corners[:,0]/4), sum(self.corners[:,1]/4)]
        self.attached = [0, 0, 0, 0]

    def findContours(self):
        contours, heirarchy = cv2.findContours(self.im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = [e for e in contours if len(e) > 60]
        cv2.fillPoly(self.im, contours, color=(255))
        try:
            return contours[0]
        except IndexError:
            return []

    def findCorners(self):
        cornerMap = cv2.cornerHarris(self.im, 10, 5, .001)
        #ret, bina = cv2.threshold(cornerMap, .25*np.max(cornerMap), 255, cv2.THRESH_BINARY)
        y, x = np.where(cornerMap>.5*np.max(cornerMap))
        self.cm = cornerMap
        candidates = np.float32(np.array([[x[i], y[i]] for i in range(len(x))]))
        criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
        compactness, labels, centers = cv2.kmeans(candidates, 8, np.array([1,2,3,4]), criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = filter(centers, 5, 4)
        #quads = [e for e in choices(centers, 4) if cv2.contourArea(e) > 0]
        quads = choices(centers, 4)
        best = quads[0]
        for e in np.unique(quads, axis=0):
            rect, hull = cv2.boxPoints(cv2.minAreaRect(e)), cv2.convexHull(e)
            bestrect, besthull = cv2.boxPoints(cv2.minAreaRect(best)), cv2.convexHull(best)
            if areaDiff(hull, rect) < areaDiff(besthull, bestrect):
                best = e
        localmax = []
        size = 14
        assert size%2 == 0
        radius = int(size/2)
        for e in best:
            x, y = round(e[0]), round(e[1])
            local = cornerMap[y-radius:y+radius, x-radius:x+radius]
            m = np.unravel_index(np.argmax(local), (size, size))
            localmax.append([m[0]+x-radius, m[1]+y-radius])
        return np.array(localmax)

    def segment(self):
        closest = [0, 0, 0, 0]
        for i, p in enumerate(self.edge):
            for j, c in enumerate(self.corners):
                #print(dist(c, p), dist(c, self.edge[closest[j]]))
                if dist(c, p) < dist(c, self.edge[closest[j]]):
                    closest[j] = i
        closest = sorted(closest)
        edges =  [self.edge[closest[0]:closest[1]], self.edge[closest[1]:closest[2]],
                self.edge[closest[2]:closest[3]], np.vstack((self.edge[closest[3]:-1],self.edge[0:closest[0]]))]
        return edges

    def evalMatch(self, pc2, sidenums, show=False):
        s1, s2 = self.sides[sidenums[0]], pc2.sides[sidenums[1]]
        #fit = self.pcs[pc1].evalFit(self.pcs[pc2], 15, 20)
        s1, s2 = s1[:,0], s2[:,0]
        origin = [-e for e in s1[0]]
        s1, s2 = shiftPts(s1, s1[0]), shiftPts(np.flipud(s2), s2[-1])
        offset = math.atan2(s1[-1][1], s1[-1][0]) - math.atan2(s2[-1][1], s2[-1][0])
        s2 = [rotateby(e, offset) for e in s2]
        fit = similaritymeasures.frechet_dist(s1, s2)
        if show:
            #s1, s2 = shiftPts(s1, origin), shiftPts(s2, origin)
            shape = np.shape(self.im)
            im = np.zeros((shape[0], shape[1], 3), np.uint8)
            s1, s2 = shiftPts(s1, origin), shiftPts(s2, origin)
            im = cv2.polylines(im, np.int32([s1]), False, (250, 0, 50), 1)
            im = cv2.polylines(im, np.int32([s2]), False, (50, 0, 250), 1)
            return fit, im
        return fit
        

    def preprocess(self, im, lower=40_000, upper=150_000):
        self.base = im
        gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 50)
        ret, bin = cv2.threshold(blur, 190, 255, cv2.THRESH_BINARY_INV)
        #bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 1)
        for i in range(1):
            bin = cv2.erode(bin, np.ones((3, 3), np.uint8))
            bin = cv2.dilate(bin, np.ones((1, 1), np.uint8))

        labels, labelids, values, centroids = cv2.connectedComponentsWithStats(bin, 4, cv2.CV_32S)
        for i, e in enumerate(values):
            if e[4] in range(lower, upper):
                pcindex = i
        component = (labelids == pcindex).astype("uint8")*255
        return component

    def lockPoints(self):
        edges = [np.delete(e, range(-1, -1-len(e)%5, -1), axis=0) for e in self.sides]
        tans = [[], [], [], []]
        for i, e in enumerate(edges):
            disp = ptdiff(e[0][0], e[-1][0])
            off = math.atan2(disp[0], disp[1])
            for j in range(len(e)-5):
                diffs = [ptdiff(e[j][0], e[j+5][0])]
                diff = sum(diffs)/len(diffs)
                tan = math.degrees(math.atan2(diff[0], diff[1]) - off)
                if abs(tan) > 88 and tan < 92:
                    tans[i].append(e[j][0])
        return tans

    def isStraight(self):
        mask = [False, False, False, False]
        sides = [e[:,0] for e in self.sides]
        for i, side in enumerate(sides):
            crowdir = (side[-1] - side[0]) / dist(side[-1], side[0])
            c = []
            for pt in side:
                crowpt = side[0] + dist(side[0], pt)*crowdir
                pt2crow = dist(pt, crowpt)
                #print(pt2crow)
                c.append(pt2crow)
            mask[i] = 1 if (sum(c)/len(c) < 7) else 0
        return mask
    
    def show(self, base=False, scale=1, edges = True, corners = True, center = True, locks=False):
        if base:
            mod = np.copy(self.base)
        else:
            mod = cv2.cvtColor(self.im, cv2.COLOR_GRAY2BGR)

        #(x,y),radius = cv2.minEnclosingCircle(self.edge)
        #center = (int(x),int(y))
        #radius = int(radius)
        #cv2.circle(mod,center,radius,(0,255,0),2)
        
        #box = cv2.boxPoints(rect)
        #box = np.int0(box)
        #hull = cv2.convexHull(self.corners)
        #cv2.drawContours(mod,[box],0,(0,0,255),2)
        #mod = cv2.polylines(mod, np.int32([hull]), True, (0, 255, 0), 2)

        if (edges and len(self.edge) == 0) or corners and len(self.corners) == 0 or (center and self.centroid == None) or (locks and len(self.locks)==0):
            print("(requested elements have not been detected)")
            return imscale(mod, scale)
        if edges:
            if len(self.sides) > 0:
                for i, e in enumerate(self.sides):
                    #mod = cv2.drawContours(mod, [e], -1, (250-50*i, 150-50*i, 80*i), 3)
                    mod = cv2.polylines(mod, np.int32([e]), False, (250-70*i, 150-50*i, 80*i), 2)
            else:
                #mod = cv2.drawContours(mod, [self.edge], -1, (250, 150, 0), 3)
                mod = cv2.polylines(mod, np.int32([self.edge]), False, (250-70*i, 150-50*i, 80*i), 2)
        if corners:
            mod = circles(mod, self.corners, radius=8, width=2)
        if center:
            mod = cv2.circle(mod, (round(self.centroid[0]), round(self.centroid[1])), 10, (130, 255, 50), 2)
        if locks:
            for e in self.locks:
                mod = circles(mod, e, radius=5, width=1, color=(190, 255, 45))
        return imscale(mod, scale)

class puzzle:
    def __init__(self, pcs, dims):
        self.pcs = pcs
        self.dims = dims

        self.edgepcs = [e for e in self.pcs if sum(e.straightSides) == 1]
        self.cornerpcs = [e for e in self.pcs if sum(e.straightSides) == 2]