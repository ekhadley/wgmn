'''
delete this stupid fucking file lol
'''

import random
w = 300
h = 300
def setup():
    size(w, h)
    background(30)
    noStroke()
    
class particle():
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random.uniform(-3, 3), random.uniform(-3, 3))
            
    def move(self):
        self.vel.y += 1
        dest = self.pos + self.vel
        if dest.x > w-3:
            self.vel.x *= -.8
            self.pos.x = w
        if dest.x < 3:
            self.vel.x *= -.8
            self.pos.x = 0
        if dest.y > h-3:
            self.vel.y *= -.8
            self.pos.y = h
        if dest.y < 3:
            self.vel.y *= -.8
            self.pos.y = 0
        self.pos += self.vel
    
    def show(self):
        fill(30, 120, 250)
        ellipse(self.pos.x, self.pos.y, 3, 3)
    
puddle = []
def draw():
    background(30)
    if mousePressed:
        if mouseButton == 37:
            puddle.append(particle(mouseX, mouseY))
    
    for i in puddle:
        for j in puddle:
            if dist(i.pos.x, i.pos.y, j.pos.x, j.pos.y) < 13:
                i.vel += .0001*PVector(i.vel.x-j.vel.x, i.vel.y-j.vel.y)
        i.move()
        i.show()
