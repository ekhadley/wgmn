'''add this shit 
detection of self-crossed loops result in re-ordering or deletion of loop segments
support for multiple initial loops
'''

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
        self.marker = color(0, 80, 255)
        self.weight = 3
    
    def showSmooth(self):
        stroke(self.marker)
        strokeWeight(self.weight)
        for i in range(0, len(self.path), 3):
            ellipse(self.path[i].x, self.path[i].y, 2, 2)
            noFill()
            bezier(self.path[i%len(self.path)].x, self.path[i%len(self.path)].y, 
                   self.path[(i+1)%len(self.path)].x, self.path[(i+1)%len(self.path)].y,
                   self.path[(i+2)%len(self.path)].x, self.path[(i+2)%len(self.path)].y,
                   self.path[(i+3)%len(self.path)].x, self.path[(i+3)%len(self.path)].y)
    
    def show(self):
        stroke(self.marker)
        strokeWeight(self.weight)
        for i in range(len(self.path)):
            ellipse(self.path[i].x, self.path[i].y, 2, 2)
            line(self.path[i%len(self.path)].x, self.path[i%len(self.path)].y,
                 self.path[(i+1)%len(self.path)].x, self.path[(i+1)%len(self.path)].y)

    
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
            curveTan /= (curveTan.mag()/ripDist)

            line(self.path[i].x, self.path[i].y, self.path[i].x + curveTan.x, self.path[i].y + curveTan.y)

            waves[-1].path.append(PVector(self.path[i].x + curveTan.x, self.path[i].y + curveTan.y))
    def rippleNew(self):
        waves.append(wave())
        for i in range(len(self.path)):
            lagVec = PVector(self.path[(i-1)%len(self.path)].x - self.path[(i)%len(self.path)].x, 
                self.path[(i-1)%len(self.path)].y - self.path[(i)%len(self.path)].y)
            leadVec = PVector(self.path[(i)%len(self.path)].x - self.path[(i+1)%len(self.path)].x, 
                self.path[(i)%len(self.path)].y - self.path[(i+1)%len(self.path)].y)
            curveTan = (lagVec+leadVec)/2
            curveTan.rotate(PI/2)
            curveTan /= (curveTan.mag()/ripDist)

            line(self.path[i].x, self.path[i].y, self.path[i].x + curveTan.x, self.path[i].y + curveTan.y)

            waves[-1].path.append(PVector(self.path[i].x + curveTan.x, self.path[i].y + curveTan.y))


w = wave()
w.marker = color(0, 10, 255)
waves = [w]

rippleCD = 0
ripDist = 30

def draw():
    global wstate
    global rippleCD

    background(0, 140, 235)
    if mouseButton == 37:
        block = 0
        for i in w.path:
            if dist(mouseX, mouseY, i.x, i.y) < 5:
                block = 1
        if not block:
            w.path.append(PVector(mouseX, mouseY))

    sinceRipple = frameCount-rippleCD
    if (mousePressed) and (mouseButton == 39) and (sinceRipple > 5):
            rippleCD = frameCount
            waves[-1].rippleNew()

    for i in waves:
        i.uncross()
        i.showSmooth()













































