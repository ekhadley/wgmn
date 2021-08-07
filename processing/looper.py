import time
def setup():
    size(800, 800)
    stroke(0, 80, 255)
    strokeWeight(3)
    background(50)
    
class wave():
    def __init__(self):
        global waves
        global ripDist
        self.path = []
        
    def show(self):
        for i in range(len(self.path)):
            ellipse(self.path[i].x, self.path[i].y, 2, 2)
            try:
                line(self.path[i].x, self.path[i].y, self.path[i+1].x, self.path[i+1].y)
            except:
                line(self.path[0].x, self.path[0].y, self.path[-1].x, self.path[-1].y)
    def uncross(self):
        for i in range(len(self.path)):
            for j in range(len(self.path)):
                pass
    
    def ripple(self):
        waves.append(wave())
        for i in range(len(self.path)):
            if i == 0:
                lagVec = PVector(self.path[-1].x - self.path[i].x, self.path[-1].y - self.path[i].y)
            if i == len(self.path)-1:
                leadVec = PVector(self.path[i].x - self.path[0].x, self.path[i].y - self.path[0].y)
            else:
                lagVec = PVector(self.path[i-1].x - self.path[i].x, self.path[i-1].y - self.path[i].y)
                leadVec = PVector(self.path[i].x - self.path[i+1].x, self.path[i].y - self.path[i+1].y)
            curveTan = (lagVec+leadVec)/2
            curveTan.rotate(PI/2)
            try:
                curveTan /= (curveTan.mag()/ripDist)
            except:
                curveTan = PVector(0, 0)
            waves[-1].path.append(PVector(self.path[i].x + curveTan.x, self.path[i].y + curveTan.y))


w = wave()
wstate = 0
waves = [w]
rippleCD = 0
ripDist = 30

def draw():
    global wstate
    global rippleCD
    
    background(0, 140, 255)
    if mouseButton == 37:
        block = 0
        for i in w.path:
            if dist(mouseX, mouseY, i.x, i.y) < 15:
                block = 1
        if not block:
            w.path.append(PVector(mouseX, mouseY))


    if frameCount - rippleCD > 20:
        if mouseButton == 39:
            rippleCD = frameCount
            waves[-1].ripple()

    for i in waves:
        #i.uncross()
        i.show()














































