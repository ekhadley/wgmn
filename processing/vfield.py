w = 1000
h = 1000
import math
import random
def setup():
    global w
    global h
    size(h, w)
    background(50)
    stroke(2)

def vshow(x, y, v, g, u):
    try:
        stroke(30, 150, 250, g)
        fill(30, 150, 250)
        ellipse(x, y, 2, 2)
        if not u:
            line(x, y, x + v.x, y + v.y)
        if u:
            line(x, y, x + v.x / v.mag() * resolution * .8,
                 y + v.y / v.mag() * resolution * .8)
    except:
        pass

def genfield(res, unit):
    for i in range(0, w, res):
        for j in range(0, h, res):
            set(j, i, 255)
            vshow(j, i, field(j - w / 2, i - h / 2), 50, unit)

class guy():

    def __init__(self, x, y, m):
        self.pos = PVector(x, y)
        self.vel = PVector(random.uniform(0, 0), random.uniform(0, 0))
        self.mass = m
        self.dead = False

    def move(self):
        try:
            self.vel += field(self.pos.x - w / 2,
                              self.pos.y - h / 2) / self.mass
            self.pos += self.vel
        except:
            self.dead = True

    def show(self):
        fill(255 - 275 * (self.pos.x / w), 1.5*(self.pos.x - self.pos.y), 255 - 185 * (self.pos.y / h))
        noStroke()
        ellipse(self.pos.x - w / 2, self.pos.y - h / 2, 8, 8)

def field(x, y):
    try:
        mx = (x**2)-(y**2)
        my = 2*x*y
        vec = PVector(mx, my)
        return vec
    except:
        pass

guys = []
started = False
resolution = 20
sources = []

def draw():
    global guys
    global started
    global sources
    background(30)
    MX = mouseX - w / 2
    MY = mouseY - h / 2

    genfield(resolution, 1)

    vshow(mouseX, mouseY, field(MX, MY), 250, 0)

    if keyPressed:
        if key == 'r':
            guys = []
            sources = []
        if key == 's':
            sources.append([MX, MY])

    if mousePressed and mouseButton == 39:
        started = True

    if mousePressed and mouseButton == 37:
        guys.append(guy(MX + w / 2, MY + h / 2, 10000))

    for i in sources:
        guys.append(guy(i[0] + w / 2, i[1] + h / 2, 10000))
    translate(w / 2, h / 2)
    for i in guys:
        if i.dead:
            guys.remove(i)
        if started:
            i.move()
        i.show()
