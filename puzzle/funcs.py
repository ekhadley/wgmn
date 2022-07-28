import math, random, cv2, similaritymeasures, imutils, numpy as np

def imscale(img, s):
    return cv2.resize(img, (round(len(img[0])*s), round(len(img)*s)), interpolation=cv2.INTER_NEAREST)

def listSim(a, b):
    diff = [dist(a[q], b[q]) for q in range(min(len(a), len(b)))]
    return sum(diff)/len(diff)
    '''
    diffs = []
    for i, e in enumerate(a):
        closest = b[0]
        low = i-5 if i-5>=0 else 0
        up = i+5 if i+5<=len(b) else len(b)-1
        for j, f in enumerate(b[low:up]):
            if dist(e, f) < dist(e, closest):
                closest = f
        diffs.append(dist(closest, e))
    return sum(diffs)/len(diffs)
    '''


def rotateby(pos, angle, origin = (0, 0)):
    cx, cy = origin[0], origin[1]
    x, y = pos[0]-cx, pos[1]-cy
    theta = math.atan2(y,x)
    h = dist(pos,origin)
    return [h*math.cos(theta+angle)+cx, h*math.sin(theta+angle)+cy]

def rotateto(pos, angle, origin=(0,0)):
    cx, cy = origin[0], origin[1]
    x, y = pos[0]-cx, pos[1]-cy
    theta = math.atan2(y,x)
    h = dist(pos,origin)
    return [h*math.cos(theta-angle)+cx, h*math.sin(theta-angle)+cy]

def rmv(arr, ind):
    new = []
    for i, e in enumerate(arr):
        if i != ind:
            np.append(new, e)
    return new

def arcdir(pts, center=(0, 0)):
    cx, cy = center
    adir = 0
    for i, e in enumerate(pts):
        x, y = e[0]-cx, e[1]-cy
        px, py = pts[(i+1)%len(pts)][0]-cx, pts[(i+1)%len(pts)][1]-cy
        adir += (math.atan2(py, px) - math.atan2(y,x))
    return adir > 0

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
            if j[channel] > lower and j[channel] < upper:
                inrange += 1
    return inrange

def dist(a,b):
    return np.linalg.norm(np.array(a)-np.array(b))

def scaleImgSet(img, lower, upper, steps):
    inc = (upper-lower)/steps
    return [imscale(img, lower+inc*i) for i in range(steps+1)]

def filter(arr, d):
    n = np.copy(arr)
    mod = 1
    while mod:
        mod = 0
        for i, e in enumerate(n):
            for j, f in enumerate(n):
                if (dist(e, f) < d) and (i != j):
                    mod = 1
                    n = np.delete(n, j, axis=0)
                    n[i] = ptavg(e, f)
                    break
            if mod:
                break
    return n

def choices(arr, n, out=[], head=True):
    if head:
        out = []
    out.append(arr)
    if len(arr) > n:
        for i, e in enumerate(arr):
            choices(np.delete(arr, i, 0), n, out, head=False)
    return np.unique([e for e in out if len(e) == n], axis=0)

def bestMatch(target, queries):
    matches = multiMatch(target)
    best = 0
    for i, e in enumerate(matches):
        if matches[i][1] > matches[best][1]:
            best = i
    return matches[best]

def shiftPts(arr, shift):
    return [[e[0]-shift[0], e[1]-shift[1]] for e in arr]

def ptavg(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

def ptdiff(p1, p2):
    return [p1[0]-p2[0], p1[1]-p2[1]]

def areaDiff(a, b):
    a1 = cv2.contourArea(a) if len(a) > 0 else 0
    a2 = cv2.contourArea(b) if len(b) > 0 else 0
    return abs(a1-a2)

def match(target, query, retMap = False):
    map = cv2.matchTemplate(target, query, cv2.TM_SQDIFF_NORMED)
    minSim, maxSim, maxSimPos, minSimPos = cv2.minMaxLoc(map)
    return ((maxSimPos, map[maxSimPos[1]][maxSimPos[0]], query, map) if retMap else (maxSimPos, map[maxSimPos[1]][maxSimPos[0]], query))

def splitImage(img, dim):
    sampledim = np.shape(img)
    subdims = (sampledim[0]//dim[1], sampledim[1]//dim[0])
    subs = []
    for j in range(0, dim[0]):
        for i in range(0, dim[1]):
            subs.append(img[subdims[0]*j:subdims[0]*(j+1), subdims[1]*i:subdims[1]*(i+1),])
    return subs

def rectangles(img, posList, dim, weight=5, color=(90, 0, 255)):
    for i, pos in enumerate(posList):
        if type(dim) == tuple:
            cv2.rectangle(img, pos, (pos[0] + dim[0], pos[1] + dim[1]), color, weight)
        if type(dim) == list:
            cv2.rectangle(img, pos, (pos[0] + dim[i][0], pos[1] + dim[i][1]), color, weight)
    return img

def circles(img, pos, radius=20, color=(20, 120, 220), width=7):
    i = np.copy(img)
    for e in pos:
        x, y = round(e[0]), round(e[1])
        i = cv2.circle(img, (x, y), radius, color, width)
    return i