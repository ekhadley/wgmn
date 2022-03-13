import random
w, h = 800, 800
def setup():
    global w
    global h
    background(30)
    size(w, h)



def getSpherical(pos):
    theta = atan2(pos.x,pos.y)
    phi = atan2(pos.z,sqrt(pos.x**2+pos.y**2))
#print(theta, phi)
    return PVector(theta, phi)
    

class pointy():
    def __init__(self, pos, marker, girth):
        self.pos = pos
        self.marker = marker
        self.girth = girth

    def show(self, cam):
            diff = PVector(cam.pos.x-self.pos.x,
                           cam.pos.y-self.pos.y,
                           cam.pos.z-self.pos.z)

            sphericalDiff = getSpherical(diff)
            sphericalCamAngle = getSpherical(cam.dir)
            sphericalViewAngleDiff = -1*PVector(sphericalCamAngle.x-sphericalDiff.x,
                                             sphericalCamAngle.y-sphericalDiff.y,)
            
            showPos = PVector(sphericalViewAngleDiff.x*w/cam.fov, sphericalViewAngleDiff.y*h/cam.fov)
            print(showPos)
    
            strokeWeight(self.girth)
            stroke(self.marker)
            ellipse(showPos.x, showPos.y, self.girth, self.girth)
                        


class  cam():
    def __init__(self, pos, dir, fov):
        self.pos = pos
        self.dir = dir
        self.fov = fov

    def update(self):
        if keyPressed:
            if key=='a':
                self.pos.x -= .01
            if key=='d':
                self.pos.x += .01
            if key=='w':
                self.pos.z += .01
            if key=='s':
                self.pos.z -= .01
    
kodak = cam(PVector(-1, 0, 0), PVector(1, 0, 0), PI)

coord = [PVector(1,0,0), PVector(0,0,1), PVector(0,1,0), PVector(0,1,1), PVector(1,0,0), PVector(1,0,1), PVector(1,1,0), PVector(1,1,1)]
cube = []
for i in range(len(coord)-1):
    cube.append(pointy(coord[i], color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), 3))

def draw():
    background(30)    
    kodak.update()
    for i in cube:
        i.show(kodak)

