import math, random, timeit, cv2, time, numpy as np
from funcs import *

class pc:
    def __init__(self, im, undistort=None):
        self.im = self.preprocess(im, undistort)
        self.edge = self.findContours()
        self.corners = self.findCorners()
        self.sides = self.segment()
        self.straightSides = self.isStraight()
        self.correctedSides = self.correctSides()
        self.pos = None
        self.rotation = None
        #self.locks = self.lockPoints()
        self.centroid = [sum(self.corners[:,0]/4), sum(self.corners[:,1]/4)]

    def findContours(self):
        contours, heirarchy = cv2.findContours(self.im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = [e for e in contours if len(e) > 60]
        #cv2.fillPoly(self.im, contours, color=(255))
        return contours[0]

    def findCorners(self):
        #cornerMap = cv2.cornerHarris(self.im, 10, 5, .001)
        cornerMap = cv2.cornerHarris(self.im, 25, 5, .001)
        #ret, bina = cv2.threshold(cornerMap, .25*np.max(cornerMap), 255, cv2.THRESH_BINARY)
        y, x = np.where(cornerMap>.5*np.max(cornerMap))
        self.cm = cornerMap
        candidates = np.float32(np.array([[x[i], y[i]] for i in range(len(x))]))
        criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
        compactness, labels, centers = cv2.kmeans(candidates, 8, np.array([1,2,3,4]), criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = filter(centers, 15)
        quads = [e for e in choices(centers, 4) if cv2.contourArea(e) > 0]
        assert len(quads)>0, "Corner finding failed, zero candidate groupings"
        best = quads[0]
        for e in np.unique(quads, axis=0):
            rect, hull = cv2.boxPoints(cv2.minAreaRect(e)), cv2.convexHull(e)
            bestrect, besthull = cv2.boxPoints(cv2.minAreaRect(best)), cv2.convexHull(best)
            if areaDiff(hull, rect) < areaDiff(besthull, bestrect):
                best = e
        localmax = []
        size = 14
        radius = int(size/2)
        for e in best:
            x, y = round(e[0]), round(e[1])
            local = cornerMap[y-radius:y+radius, x-radius:x+radius]
            m = np.unravel_index(np.argmax(local), (size, size))
            localmax.append([m[0]+x-radius, m[1]+y-radius])
        return np.flip(cv2.convexHull(np.array(localmax))[:,0], axis=0)

    def segment(self):
        closest = [0, 0, 0, 0]
        for i, p in enumerate(self.edge):
            for j, c in enumerate(self.corners):
                if dist(c, p) < dist(c, self.edge[closest[j]]):
                    closest[j] = i
        edges = []
        for i in range(len(closest)):
            if closest[i] < closest[(i+1)%4]:
                seg = self.edge[closest[i]:closest[(i+1)%4],0]
            else:
                seg = np.vstack((self.edge[closest[i]:-1,0],self.edge[0:closest[(i+1)%4],0]))
            edges.append(seg)
        return edges

    def correctSides(self):
        corners = cv2.convexHull(np.array(self.corners, np.float32))
        #corners = np.array(self.corners, np.float32)
        #rect = cv2.convexHull(np.array([[x, y], [x, y+h], [x+w, y+h], [x+w, h]], np.float32))
        sqrSize = 2000
        rect = np.array([[80, 80], [sqrSize-80, 80], [sqrSize-20, sqrSize-80], [80, sqrSize-80]], np.float32)
        mat = cv2.getPerspectiveTransform(corners, rect)
        shifted = [[], [], [], []]
        for i, side in enumerate(self.sides):
            for p in side:
                shifted[i].append([(mat[0][0]*p[0] + mat[0][1]*p[1] + mat[0][2])/(mat[2][0]*p[0] + mat[2][1]*p[1] + mat[2][2]),
                                   (mat[1][0]*p[0] + mat[1][1]*p[1] + mat[1][2])/(mat[2][0]*p[0] + mat[2][1]*p[1] + mat[2][2])])
        s = np.shape(self.base)
        self.warped = cv2.warpPerspective(self.base, mat, (sqrSize, sqrSize))
        return shifted
    
    def preprocess(self, im, undistort, lower=1_000_000, upper=2_000_000):
        if undistort != None:
            mtx,dst,newmtx = undistort
            im = cv2.undistort(im, mtx, dst, None, newmtx)
        self.base = im
        gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 50)
        ret, bin = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
        #bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 1)
        for i in range(1):
            bin = cv2.erode(bin, np.ones((3, 3), np.uint8))
            bin = cv2.dilate(bin, np.ones((1, 1), np.uint8))
        labels, labelids, values, centroids = cv2.connectedComponentsWithStats(bin, 4, cv2.CV_32S)
        shape = np.shape(bin)

        pcindex=-1
        for i, e in enumerate(values):
            if e[4] in range(lower, upper) and e[3]<shape[0] and e[2]<shape[1]:
                pcindex = i

        assert pcindex != -1, f"connected component failed: no match.\nComponents found:\n{values}"
        component = (labelids == pcindex).astype("uint8")*255

        return component

    def isStraight(self):
        mask = [0, 0, 0, 0]
        for i, side in enumerate(self.sides):
            crowdir = (side[-1] - side[0]) / dist(side[-1], side[0])
            c = []
            for q in range(0, len(side), 5):
                pt = side[q]
                crowpt = side[0] + dist(side[0], pt)*crowdir
                pt2crow = dist(pt, crowpt)
                #print(pt2crow)
                c.append(pt2crow)
            mask[i] = 1 if (sum(c)/len(c))<5 else 0
        return mask
    
    def show(self, base=False, scale=1, edges = True, corners = True, center = True, locks=False, radius=8,thickness=2):
        if base:
            mod = np.copy(self.base)
        else:
            mod = cv2.cvtColor(self.im, cv2.COLOR_GRAY2BGR)

        if (edges and len(self.edge) == 0) or corners and len(self.corners) == 0 or (center and self.centroid == None) or (locks and len(self.locks)==0):
            print("(requested elements have not been detected)")
            return imscale(mod, scale)
        if edges:
            if len(self.sides) > 0:
                for i, e in enumerate(self.sides):
                    #mod = cv2.drawContours(mod, [e], -1, (250-50*i, 150-50*i, 80*i), 3)
                    mod = cv2.polylines(mod, np.int32([e]), False, (250-70*i, 150-50*i, 80*i), thickness)
            else:
                #mod = cv2.drawContours(mod, [self.edge], -1, (250, 150, 0), 3)
                mod = cv2.polylines(mod, np.int32([self.edge]), False, (250-70*i, 150-50*i, 80*i), thickness)
        if corners:
            for i, e in enumerate(self.corners):
                mod = circles(mod, [e], radius=radius, width=thickness, color=(250-70*i, 150-50*i, 80*i))
        if center:
            mod = cv2.circle(mod, (round(self.centroid[0]), round(self.centroid[1])), radius, (130, 255, 50), thickness)
        if locks:
            for e in self.locks:
                mod = circles(mod, e, radius=radius, width=thickness, color=(190, 255, 45))
        return imscale(mod, scale)

class puzzle:
    def __init__(self, pcs, dims):
        self.pcs = pcs
        self.unplaced = [e for e in pcs]
        self.placed = []
        self.dims = dims
        self.edgepcs = [e for e in self.pcs if sum(e.straightSides) == 1]
        self.cornerpcs = [e for e in self.pcs if sum(e.straightSides) == 2]
        self.solved = False
        self.place(self.pcs[0], (0,0), 0)

    def getBorders(self, pos):
        x, y = pos[0], pos[1]
        c = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
        borders = [None, None, None, None]
        for pc in self.placed:
            if pc.pos in c:
                s = c.index(pc.pos)
                borders[(s+2)%4] = (pc, (s+pc.rotation)%4)
        return borders 

    def place(self, p, pos, r):
        p.pos = pos
        p.rotation = r
        self.unplaced.remove(p)
        self.placed.append(p)
        self.solved = len(self.unplaced)==0

    def bestFit(self, pos):
        fits = []
        for pc in self.unplaced:
            for rot in range(0, 3):
                score = self.evalPlacement(pc, pos, rot)
                fits.append((pc, rot, score))
        #best = np.argmin(np.array(fits)[:,2])
        fits = sorted(fits, key=lambda x:x[2])
        print(f"{fits}, \n")
        return fits[0]

    def bestPlacement(self):
        spots = self.perimeterPositions()[0]
        s = [self.bestFit(e) for e in spots]
        return s

    def evalPlacement(self, p, pos, rot):
        borders = self.getBorders(pos)
        score = 0
        for i in range(4):
            if borders[i] != None:
                otherpc, otherside = borders[i]
                score += p.evalMatch(otherpc, ((i+rot)%4, otherside))
        return score

    def perimeterPositions(self):
        coords = [(e.pos[0], e.pos[1]) for e in self.placed]
        maxX, maxY = np.max([e[0] for e in coords]), np.max([e[1] for e in coords])
        maxX, maxY = min(maxX, self.dims[0]), min(maxY, self.dims[1])
        borders = [[], [], [], []]
        for i in range(maxX+2):
            for j in range(maxY+2):
                if (i, j) not in coords:
                    edges = self.getBorders((i, j))
                    m = sum([1 for e in edges if e != None])
                    if m > 0:
                        borders[4-m].append((i, j))
        return [e for e in borders if len(e)>0]

    def evalMatch(self, pieces, sidenums, show=False, thickness=1):
        first, second = sidenums
        pc1, pc2 = pieces
        s1, s2 = pc1.correctedSides[first], pc2.correctedSides[second]
        origin = [-200, -200]
        #s1, s2 = shiftPts(s1, s1[0]), shiftPts(np.flipud(s2), s2[-1])
        s1, s2 = shiftPts(s1, s1[0]), shiftPts(s2, s2[0])
        offset = math.atan2(s1[-1][1], s1[-1][0]) - math.atan2(s2[-1][1], s2[-1][0])
        s2 = [rotateby(e, offset) for e in s2]

        s1o, s2o = pc1.sides[first], pc2.sides[second]
        d = dist(s1o[0], s1o[-1]) - dist(s2o[0], s2o[-1])

        smask1, smask2 = pc1.straightSides, pc2.straightSides
        if (1 in smask1) and (1 in smask2):
            check = not ((smask1[(first-1)%4] and smask2[(second+1)%4]) or (smask1[(first+1)%4] and smask2[(second-1)%4]))
        elif (1 in smask1) and (not 1 in smask2):
            i = smask1.index(1)
            check = (first!=((i+2)%4))
        elif (not 1 in smask1) and (1 in smask2):
            i = smask2.index(1)
            check = (second!=((i+2)%4))
        else:
            check = False

        if d > 15 or smask1[first] or smask2[second] or check:
            fit = 1000
        else:
            #fit = similaritymeasures.frechet_dist(s1, s2)
            fit = listSim(s1, s2)
        if show:
            x, y = np.shape(pc1.im)
            im = np.zeros((x, y, 3), np.uint8)
            s1, s2 = shiftPts(s1, origin), shiftPts(s2, origin)
            im = cv2.polylines(im, np.int32([s1]), False, (250, 0, 50), thickness)
            im = cv2.polylines(im, np.int32([s2]), False, (50, 0, 250), thickness)
            return fit, im
        return fit
