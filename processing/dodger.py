'''
collisions detection
player abilities (?)
score counter
predictive projectile launching
partially randomized projectile parameters(?)
'''
import random, time

w, h = 800, 800
def setup():
    size(w, h)
    background(50)
    rectMode(CORNERS)

def isBetween(x, u, l):
    if x > l and x < u:
        return True
    return False

def inSquare(pos, x1, y1, x2, y2):
    return (isBetween(pos.x, x1, x2) and isBetween(pos.y, y1, y2))

def inView(pos):
    return inSquare(pos, 0, 0, w, h)

class player():
    def __init__(self, x, y, v):
        self.pos = PVector(x, y)
        self.v = v
        self.marker = color(250, 30, 100)
        self.dest = PVector(x, y)
        self.dir = PVector(0, 0)
        
    def moveTo(self, x, y):
        self.dest = PVector(x, y)
        self.dir = PVector(x - self.pos.x, y - self.pos.y)
        try:
            self.dir /= self.dir.mag()
        except:
            self.dir = PVector(0, 0)
        self.dir *= self.v
        
    def update(self):
        self.pos += self.dir
        if dist(self.pos.x, self.pos.y, self.dest.x, self.dest.y) < self.v:
            self.pos = self.dest
            self.dir = PVector(0, 0)
    def takeHit(self):
        pass
    
                
    def show(self):
        strokeWeight(2)
        stroke(255, 255, 255, 50)
        line(self.pos.x, self.pos.y, self.dest.x, self.dest.y)
        noStroke()
        fill(self.marker)
        ellipse(self.pos.x, self.pos.y, playerSize, playerSize)

class projectile():
    def __init__(self, x, y, t, v, s):
        self.pos = PVector(x, y)
        self.dir = PVector(t.pos.x-x, t.pos.y-y)
        try:
            self.dir *= (v/self.dir.mag())
        except:
            self.dir = PVector(0, 0)
        self.marker = color(random.randint(130,255), 1, random.randint(100, 255))
        self.s = s
        
    def run(self):
        self.pos += self.dir
        fill(self.marker)
        ellipse(self.pos.x, self.pos.y, self.s, self.s)

class turret():
    def __init__(self, x, y, t, sp, si):
        self.pos = PVector(x, y)
        self.psize = si
        self.pspeed = sp
        self.target = t
    def show(self):
        fill(250, 30, 80)
        ellipse(w/2, 100, 25, 25)
        translate(self.pos.x, self.pos.y)
        rotate(PVector(self.target.pos.x - self.pos.x, self.target.pos.y - self.pos.y).heading() - PI/2)
        rect(-5, 0, 5, 25)
        resetMatrix()
    def shoot(self):
        distToTarget = dist(self.pos.x, self.pos.y, self.target.pos.x, self.target.pos.y)
        
        projectiles.append(projectile(self.pos.x, self.pos.y, self.target, self.pspeed, self.psize))

projectiles = []



playerSize = 50
playerSpeed = 10
projectileSize = 15
projectileSpeed = 10
spawnChance = .03

swain = player(w/3, h/4, playerSpeed)
gun = turret(w/2, 100, swain, projectileSpeed, projectileSize)
def draw():
    stime = time.time()
    background(30)
    
    
    if mousePressed:
        if mouseButton == 39:
            swain.moveTo(mouseX, mouseY)

    if random.randint(0, 1000) < spawnChance*1000:
        spos = PVector(w/2, 100)
#        projectiles.append(projectile(spos.x, spos.y, swain, projectileSpeed, projectileSize))
        gun.shoot()
    
    for i in range(len(projectiles)):
        projectiles[i].run()
        if inView(projectiles[i].pos):
            projectiles.pop(i)

    #print(len(projectiles), 1/(time.time()-stime+.00001))
    print(mouseX, mouseY, isBetween(mouseX, 0, w))
    gun.show()
    swain.update()
    swain.show()
