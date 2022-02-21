w, h = 800, 800
def setup():
    global w
    global h
    background(30)
    size(w, h)



def getSpherical(pos):
    theta = atan2(pos.x/pos.y)
    phi = atan2(z/sqrt(pos.x**2+pos.y**2))
    return PVector(theta, phi)

class pointy():
    def __init__(self, pos, marker, girth):
        self.pos = pos
        self.marker = marker
        self.girth = girth
    
    def getScreenPos(self, cam):
            diff = PVector(cam.pos.x-self.pos.x,
                           cam.pos.y-self.pos.y,
                           cam.pos.z-self.pos.z)
            sphericalDiff = getSpherical(diff)
            sphericalCamAngle = getSpherical(cam.dir.x, cam.dir.y, cam.dir.z)
            sphericalViewAngleDiff = PVector(sphericalCamAngle.x-sphericalDiff.x,
                                             sphericalCamAngle.y-sphericalDiff.y,)
            return PVector(sphericalViewAngle.x*w/cam.fov, sphericalViewAngle.y*h/cam.fov)
            
    
    def show(self, screenPos):
        strokeWeight(self.girth)
        stroke(self.marker)
        point(screenPos.x, screenPos.y)


class  cam():
    def __init__(self, pos, dir, fov):
        self.pos = pos
        self.dir = dir
        self.fov = fov

kodak = cam(PVector(-10, 0, 0), PVector(1, 0, 0), 90)
joe = pointy(0, 0, 0)

def draw():
    
    joe.show(joe.getScreenPosition(kodak))
    background(30)















































