w, h = 800, 800
def setup():
    global w
    global h
    background(30)
    size(w, h)



def getSpherical(pos):
    theta = atan2(pos.x,pos.y)
    phi = atan2(pos.z,sqrt(pos.x**2+pos.y**2))
    print(theta, phi)
    return PVector(theta, phi)
    

class pointy():
    def __init__(self, pos, marker, girth):
        self.pos = pos
        self.marker = marker
        self.girth = girth
        self.showPos = PVector(0,0)

    def getScreenPos(self, cam):
            diff = PVector(cam.pos.x-self.pos.x,
                           cam.pos.y-self.pos.y,
                           cam.pos.z-self.pos.z)
            sphericalDiff = getSpherical(diff)
            sphericalCamAngle = getSpherical(cam.dir)
            sphericalViewAngleDiff = PVector(sphericalCamAngle.x-sphericalDiff.x,
                                             sphericalCamAngle.y-sphericalDiff.y,)
            self.showPos = PVector(sphericalViewAngleDiff.x*w/cam.fov, sphericalViewAngleDiff.y*h/cam.fov)
            
    
    def show(self):
        strokeWeight(self.girth)
        stroke(self.marker)
        point(self.showPos.x, self.showPos.y)


class  cam():
    def __init__(self, pos, dir, fov):
        self.pos = pos
        self.dir = dir
        self.fov = fov

kodak = cam(PVector(-10, 0, 0), PVector(0, 0, 0), PI/2)
joe = pointy(PVector(1, 1, 1), color(30, 200, 80), 5)

def draw():
    
    joe.getScreenPos(kodak)
    joe.show()
    
    background(30)















































