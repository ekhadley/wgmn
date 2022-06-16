import math, cv2, numpy as np

def imscale(img, s):
    return cv2.resize(img, (round(len(img[0])*s), round(len(img)*s)))

def listSim(a, b):
    diff = [dist(a[q], b[q]) for q in range(min(len(a), len(b)))]
    return sum(diff)/len(diff)

def rotate(pos, angle, origin=(0,0)):
    cx, cy = origin[0], origin[1]
    x, y = pos[0]-cx, pos[1]-cy
    theta = math.atan2(y,x)
    h = dist(pos,origin)
    return [h*math.cos(theta+angle)+cx, h*math.sin(theta+angle)+cy]

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
