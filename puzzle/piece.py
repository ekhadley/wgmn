import math, cv2, numpy as np
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
        self.centroid = [sum(self.corners[:,0]/4), sum(self.corners[:,1]/4)]
        self.attached = [0, 0, 0, 0]

    def evalFit(self, o):
        fits = []
        d = []
        rev = [np.flipud(e) for e in self.sides]
        mine = [[[e[0,0]-side[0,0,0], e[0,1]-side[0,0,1]] for e in side] for side in rev]
        other = [[[e[0,0]-side[0,0,0], e[0,1]-side[0,0,1]] for e in side] for side in o.sides]
        for i, a in enumerate(mine):
            for j, b in enumerate(other):
                if self.straightSides[i] or o.straightSides[j]:
                    fits.append(10000)
                elif round(dist(a[0], a[-1]) - dist(b[0], b[-1])) not in range(-20, 20):
                    fits.append(10000)
                #elif (self.straightSides[(i+1)%4], self.straightSides[(i-1)%4]) and not (o.straightSides[(i+1)%4], self.straightSides[(i-1)%4]):
                #    fits.append(10000)
                else:
                    offset =  math.atan2(b[-1][1], b[-1][0]) - math.atan2(a[-1][1], a[-1][0])
                    arot = np.array([rotateby(e, offset) for e in a])
                    fits.append(similaritymeasures.frechet_dist(arot, b))
                    #fits.append(round(listSim(arot, b), 2))
        return [np.unravel_index(i, (4,4)) for i in range(len(fits)) if fits[i]<30]
        #return fits 

    def findContours(self):
        contours, heirarchy = cv2.findContours(self.im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = [e for e in contours if len(e) > 60]
        cv2.fillPoly(self.im, contours, color=(255))
        try:
            return contours[0]
        except IndexError:
            return []

    def findCorners(self):
        cornerMap = cv2.cornerHarris(self.im, 7, 3, .001)
        #ret, bina = cv2.threshold(cornerMap, .25*np.max(cornerMap), 255, cv2.THRESH_BINARY)
        y, x = np.where(cornerMap>.5*np.max(cornerMap))
        self.cm = cornerMap
        candidates = np.float32(np.array([[x[i], y[i]] for i in range(len(x))]))
        criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
        compactness, labels, centers=cv2.kmeans(candidates, 4, np.array([1,2,3,4]), criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        return centers

    def preprocess(self, im):
        gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 50)
        ret, bin = cv2.threshold(blur, 190, 255, cv2.THRESH_BINARY_INV)
        #bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 1)
        for i in range(1):
            bin = cv2.erode(bin, np.ones((3, 3), np.uint8))
            bin = cv2.dilate(bin, np.ones((1, 1), np.uint8))       

        labels, labelids, values, centroids = cv2.connectedComponentsWithStats(bin, 4, cv2.CV_32S)
        for i, e in enumerate(values):
            if e[4] in range(40000, 150000):
                pcindex = i
        component = (labelids == pcindex).astype("uint8")*255
        return component

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

    def show(self, scale=1, edges = True, corners = True, center = True):
        mod = cv2.cvtColor(self.im, cv2.COLOR_GRAY2RGB)

        #(x,y),radius = cv2.minEnclosingCircle(self.edge)
        #center = (int(x),int(y))
        #radius = int(radius)
        #cv2.circle(mod,center,radius,(0,255,0),2)
        hull = cv2.convexHull(self.edge)
        mod = cv2.polylines(mod, np.int32([hull]), False, (0, 255, 0), 2)

        if (edges and len(self.edge) == 0) or (corners and len(self.corners) == 0 or (center and self.centroid == None)):
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
            circles(mod, self.corners, radius=7, width=2)
        if center:
            mod = cv2.circle(mod, (round(self.centroid[0]), round(self.centroid[1])), 10, (130, 255, 50), 2)
        return imscale(mod, scale)

class puzzle:
    def __init__(self, pcs, dims):
        self.pcs = pcs
        self.dims = dims
    
