import math
w, h = 800, 800
def setup():
    size(w, h)
    background(30)

def vshow(pos, vec, m, w):
    strokeWeight(w)
    stroke(m)
    line(pos.x, pos.y, pos.x + vec.x, pos.y + vec.y)

def getSpherical(p):
    if p.x == 0 and p.y == 0:
        return(PVector(0, 0))
    if p.x == 0:
        return(PVector(PI/2, atan(p.y/p.z)))
    if p.y == 0:
        return(PVector(0, atan(p.z/p.x)))
    return(PVector(atan(p.x/p.y), atan((sqrt(p.x**2+p.y**2))/p.z)))

def getSpherical(p):
    return(PVector(math.atan2(p.x,p.y), math.atan2((sqrt(p.x**2+p.y**2)),p.z)))

def degreeVec(v):
    return PVector(degrees(v.x), degrees(v.y), degrees(v.z))

def getSphericalDifference(p):
    global viewvec
    global viewpos
    viewPolar = getSpherical(viewvec)
    pointPolar = getSpherical(viewpos-p)
    sphericalDiff = pointPolar-viewPolar
    return(sphericalDiff)

class vox():
    def __init__(self, x, y, z):
        self.marker = color(30, 200, 30)
        self.pos = PVector(x, y, z)
    
    def getpos(self):
        global w
        global h
        global viewvec
        global viewpos
        azimuth = getSphericalDifference(self.pos)
        return PVector((azimuth.x/(1.48353*PI))*w + w/2, (azimuth.y/(1.48353*PI))*h/2)
    
    def show(self):
        global w
        global h
        global viewvec
        global viewpos
        azimuth = getSphericalDifference(self.pos)
        fill(self.marker)
        noStroke()
        ellipse((azimuth.x/(2*PI))*w + w/2, (azimuth.y/(2*PI))*h + h/2, 15, 15)
        return PVector((azimuth.x/(1.48353*PI))*w + w/2, (azimuth.y/(1.48353*PI))*h + h/2)

class beam():
    def __init__(self, w, z):
        self.marker = color(200, 15, 30)
        self.end1 = w
        self.end2 = z
    def show(self):
        global w
        global h
        global viewvec
        global viewpos
        end1 = w.getpos()
        end2 = z.getpos()

        stroke(self.marker)
        strokeWeight(1)
        line(end1, endpoints[0].y, endpoints[1].x, endpoints[1].y)
        
        
viewvec = PVector(-1, 1, 0)
viewpos = PVector(1, 0, 0)

v = vox(0, 0, 0)
xaxis = vox(1000, 0, 0)
yaxis = vox(0, 1000, 0)
zaxis = vox(0, 0, 1000)
xb = beam(v, xaxis)
yb = beam(v, yaxis)
zb = beam(v, zaxis)

elements = [v, xaxis, yaxis, zaxis, xb, yb, zb]

def draw():
    background(30)
    global viewvec
    global viewpos
    viewvec /= viewvec.mag()
    
    for i in elements:
        i.show()
        
    print(viewpos)
    
    
    if keyPressed and key=='w':
        viewpos.x += .3
    if keyPressed and key=='a':
        viewpos.y -= .3
    if keyPressed and key=='s':
        viewpos.x -= .3
    if keyPressed and key=='d':
        viewpos.y += .3
    if keyPressed and key=='r':
        viewpos = PVector(1, 0, 0)










































































































