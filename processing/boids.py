""" add this shit
implement local coherence
make turning less affected by general repulsion idk how tho
"""

import math, random, time, operator
h, w = 800, 800
def setup():
    global h
    global w
    size(w, h)
    stroke(50)

def setvel(m):
    b = PVector(0, m)
    a = random.randint(0, 359)
    return b.rotate(a)

class bird():
    def __init__(self, x, y, vrange, m):
        self.pos = PVector(x, y)
        self.m = m
        self.vel = setvel(self.m)
        self.vrange = vrange
        self.marker = color(random.randint(130,255), 1, random.randint(180, 255))

    def oob(self):
        if self.pos.x + self.vel.x > w-5:
            self.pos.x = 5
        if self.pos.x + self.vel.x < 5:
            self.pos.x = w-5
        if self.pos.y + self.vel.y > h-5:
            self.pos.y = 5
        if self.pos.y + self.vel.y < 5:      
            self.pos.y = h-5

    def move(self):
        self.oob()
        self.pos += self.vel
        if self.vel.mag() > self.m*3:
            self.vel *= .9
        if self.vel.mag() < self.m/3:
            self.vel *= 1.1


    def show(self):
        fill(self.marker)
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading() + PI/2)
        triangle(0, -10, -5, 10, 5, 10)
        resetMatrix()

pool = []

for i in range(30):
    rx = random.randint(1, w)
    ry = random.randint(1, h)
    pool.append(bird(rx, ry, 100, 3))

def draw():
    background(50)
    for i in pool:
        i.move()
        i.show()
        adiff = 0
        inRange = 0
        for j in pool:
            d = dist(i.pos.x, i.pos.y, j.pos.x, j.pos.y)
            if d < i.vrange:
                xdiff = i.pos.x-j.pos.x
                ydiff = i.pos.y-j.pos.y
                i.vel += PVector(xdiff, ydiff)/((d + .000001)**2)
                j.vel += PVector(-xdiff, -ydiff)/((d + .000001)**2)


            if d < i.vrange*3:
                p = PVector(i.vel/i.vel.mag() + j.vel/j.vel.mag())
                Havg = p.heading()
                i.vel.rotate(.5)
                j.vel.rotate(-.5)
            
                
        noStroke()
        fill(15, 250, 150, 10)
        ellipse(i.pos.x, i.pos.y, i.vrange, i.vrange)
        stroke(50)

    
    
    
    
    
    
    
    
    
    
    
    
