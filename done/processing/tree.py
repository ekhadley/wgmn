""" add this shit
- branch happiness related to crowdedness(?)
- weighted function for branch genesis according to parent happiness
- better branch breakage probablilty based on branch age and happiness
"""
import random, math
from p5 import *
w, h = 600, 600
def setup():
    size(w, h)
    background(30)

class light():
    def __init__(self, x, y, i):
        self.pos = PVector(x, y)
        self.i = i
    def show(self):
        noStroke()
        fill(230, 200, 10)
        ellipse(self.pos.x, self.pos.y, 30, 30)

class branch():
    def __init__(self, px, py, dx, dy):
        self.pos = PVector(px, py)
        self.dir = PVector(dx, dy)
        self.dir /= self.dir.mag()
        self.age = 1
        self.l = PVector(0, 0)
        self.kids = []
        self.ratio = 0
        self.happiness = 1/dist(l.pos.x, l.pos.y, self.pos.x, self.pos.y)
        self.falling = False
        self.v = 0
        
    def sprout(self):
        for i in self.kids:
            i.sprout()
        if len(self.kids) < 2:
            if random.random() > .990:
                ratio = 1-(1/(2.718**(3*random.uniform(0, 1.5))))
                kPos = self.pos + self.l * ratio
                self.kids.append(branch(kPos.x, kPos.y, random.uniform(-1, 1), random.uniform(-1, .1)))
                self.kids[len(self.kids)-1].ratio = ratio
    
    def grow(self):
        self.age += 1
        lfactor = 10 * math.log(self.age + 1)
        self.l = PVector(self.dir.x * lfactor, self.dir.y * lfactor)
        for i in self.kids:
            i.pos = self.pos + self.l * i.ratio
            i.grow()
            #this threshold function is fuckin stupid
            thresh = 1/(10*(self.happiness+self.age))
            print(.999+thresh)
            if random.random() > 1:
                self.kids.remove(i)
                
    def fall(self):
        for i in self.kids:
            self.falling = True
            i.fall()
        if self.falling:
            self.v += .1
            self.pos.y += self.v
                
    def show(self):
        wfactor = 5 * math.log((self.age/8)+1)
        cfactor = 50 * math.log(self.age+1)
        strokeWeight(wfactor)
        stroke(125, 255-cfactor, 40)
        line(self.pos.x, self.pos.y, self.pos.x + self.l.x, self.pos.y + self.l.y)
        for i in self.kids:
            i.show()

started = 0
def draw():
    global started
    global l
    global trunk
    global branches
    global happies
    background(30)

    if mouse_is_pressed:
        if mouse_button == 37:
            started = 1
            l = light(mouse_x, mouse_x, 1)
            branches = 0
            trunk = branch(w/2, h, random.uniform(-1, 1), random.uniform(-1, .1))
            
    if started:
        l.show()
        trunk.grow()
        trunk.show()
        trunk.sprout()

run()