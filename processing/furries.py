'''add this shit
¯\_(ツ)_/¯
'''
import random, time
w = 800
h = 800
def setup():
    size(w, h)
    background(30)

class tater():
    def  __init__(self, x, y, r, v):
        self.pos = PVector(x, y)
        #self.vec = PVector(r, 0).rotate(radians(random.randint(0, 360)))
        self.vec = PVector(r, 0)
        self.v = v*.05
        self.r = r
        self.child = None
        self.marker = color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        
    def getReach(self):
        global reach
        if self.child == None:
            reach = (self.pos + self.vec)
        else:
            self.child.getReach()
    
    def attach(self, r, v):
        if self.child == None:
            self.child = tater(self.pos.x+self.r, self.pos.y, r, v)
        else:
            self.child.attach(r, v)
            
    def spin(self):
        self.vec.rotate(self.v)
        if self.child != None:
            self.child.pos = self.pos + self.vec
            self.child.spin()

    def vshow(self, mode="noCircles"):
        stroke(self.marker)
        if mode == "circles":
            noFill()
            strokeWeight(1)
            ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)        
        strokeWeight(4)
        line(self.pos.x, self.pos.y, self.vec.x+self.pos.x, self.vec.y+self.pos.y)    
        if self.child != None:
            self.child.vshow(mode)


if 0:
    t = tater(w/2, h/2, random.randint(1, 10), random.randint(-10, 10))
    for i in range(10):
        t.attach(random.randint(0, i/100), random.randint(0, i/100))
        #t.attach(50, i/100))
else:
    t = tater(w/2, h/2, 50, 1)
    t.attach(50, 2)




trail = []

def draw():
    global reach
    time.sleep(0)
    background(30)
    
    t.spin()
    t.vshow()
    t.getReach()
    
    trail.append(reach)
    for i in range(len(trail)):
        strokeWeight(5)
        stroke(30, 250, 150, 150)
        
        if len(trail) > 299:
            trail.pop(0)
        
        try:
            line(trail[i].x, trail[i].y, trail[i+1].x, trail[i+1].y)
            '''
            bezier(trail[i%len(trail)].x, trail[i%len(trail)].y,
            trail[(i+1)%len(trail)].x, trail[(i+1)%len(trail)].y,
            trail[(i+2)%len(trail)].x, trail[(i+2)%len(trail)].y,
            trail[(i+3)%len(trail)].x, trail[(i+3)%len(trail)].y)
            '''
        except:
            pass
