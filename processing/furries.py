'''add this shit
stupid fucking getReach function is broken for no reason (bioluminescence)
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
        self.vec = PVector(r, 0)
        self.v = v*.05
        self.r = r
        self.child = None
        self.marker = color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
   
    def getReach(self):
        if self.child != None:
            self.child.getReach()
        else:
            return self.pos + self.vec
            print("huh????")
            
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


t = tater(w/2, h/2, 80, 1)

t.attach(70, 2)

t.attach(60, -5)

t.attach(50, 4)

t.attach(40, -5)

t.attach(30, 8)



trail = []
reach = PVector(0, 0)
def draw():
    global reach
    background(30)
    
    t.spin()
    t.vshow("")
    print(t.getReach())
    
    trail.append(reach)
    for i in range(len(trail)):
        strokeWeight(5)
        stroke(30, 250, 150, 150)
        if len(trail) > 299:
            trail.pop(0)
        try:
            line(trail[i].x, trail[i].y, trail[i+1].x, trail[i+1].y)
        except:
            pass
