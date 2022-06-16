import math, cv2, numpy as np
from misc import *

class pc:
    def __init__(self, im):
        self.im = im
        self.edge = self.findContours()
        self.corners = self.findCorners()
        self.sides = self.segment()
        self.straightSides = self.isStraight()
        self.attached = [0, 0, 0, 0]

    def evalFit(self, o):
        fits = []
        mine = [[[e[0,0]-side[0,0,0], e[0,1]-side[0,0,1]] for e in side] for side in self.sides]
        other = [[[e[0,0]-side[0,0,0], e[0,1]-side[0,0,1]] for e in side] for side in o.sides]
        for i, a in enumerate(mine):
            for j, b in enumerate(other):
                print(math.atan2(a[-1][1], a[-1][0]) - math.atan2(b[-1][1], b[-1][0]), math.atan2(a[-1][1], a[-1][0]) - math.atan2(b[-1][1], b[-1][0]))
                #print(math.atan2(b[-1][1], b[-1][0]))
                if self.straightSides[i] or o.straightSides[j]:
                    fits.append(10000)
                elif dist(a[0], a[-1]) - dist(b[0], b[-1]) >= 15:
                    fits.append(1000)
                else:
                    #offset = math.atan2(a[-1][1], a[-1][0]) - math.atan2(b[-1][1], b[-1][0])
                    #arot = np.array([[rotate(e[0], offset)] for e in a])
                    fits.append(listSim(a, b))
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
                    mod = cv2.polylines(mod, np.int32([e]), False, (250-70*i, 150-50*i, 80*i), 3)
            else:
                #mod = cv2.drawContours(mod, [self.edge], -1, (250, 150, 0), 3)
                mod = cv2.polylines(mod, np.int32([self.edge]), False, (250-70*i, 150-50*i, 80*i), 3)
        if corners:
            circles(mod, self.corners, radius=5, width=2)
        return imscale(mod, scale)
