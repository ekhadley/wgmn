""" shit to add
use PVectors becuase its cleaner (?)
variable transferral/mutation rates based on change of fitness of recent generations
only search local space for walls (segmented lists based on position)
"""
import math, random, time, operator
h, w = 800, 800
def setup():
    global h
    global w
    background(50)
    size(w, h)
    stroke(50)


def randomDNA(l):
    q = []
    for i in range(0, l):
        val = [float(random.randint(-300, 300))/1000, float(random.randint(-300, 300))/1000]
        q.append([val[0], val[1]])
    return q

def mutate(lp, lc, t, m):
    for i in range(len(lc)):
        if random.randint(1, 100) > t:
            lc[i] = lp[i]
        if random.randint(1, 100) > m:
            lc[i] = [float(random.randint(-3, 300))/1000, float(random.randint(-300, 300))/1000]
    return(lc)

def m(l, t):
    for i in l:
        if t < random.randint(1, 100):
            lc[i] = [float(random.randint(-300, 300))/1000, float(random.randint(-300, 300))/1000]
    return(l)

class food():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
   
    def show(self):
        fill(230, 30, 30)
        ellipse(self.x, self.y, self.r, self.r)

class walker():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.dna = randomDNA(500)
        self.place = 0
        self.fitness = 10000
        self.dead = 0
        self.sp = [x, y]
        self.marker = color(15, 250, 150)
   
    def reset(self):
#        self.marker = color(15, 250, 150)
        self.x = self.sp[0]
        self.y = self.sp[1]
        self.vx = 0
        self.vy = 0
        self.place = 0
        self.fitness = 1000000
        self.dead = 0
   
    def mutate(self, l, m, t):
        for i in range(len(l)):
            if t > random.randint(0, 100):
                self.dna[i] = l[i]
            if m > random.randint(0, 100):
                self.dna[i] = [float(random.randint(-300, 300))/1000, float(random.randint(-300, 300))/1000]
   
    def kill(self):
        if not self.dead:
            self.dead = True
            if dist(self.x, self.y, 50, 50) < 25:
                self.fitness = self.place/(len(self.dna))
            else:
                self.fitness = dist(self.x, self.y, 50, 50)

    
    def oob(self):
        if self.x + self.vx > w-5:
            self.kill()
            self.x = 795
        if self.x + self.vx < 5:
            self.kill()
            self.x = 5
        if self.y + self.vy > h-5:
            self.kill()
            self.y = 795
        if self.y + self.vy < 5:
            self.kill()        
            self.y = 5

    def move(self):
        if self.place < len(self.dna) - 1:
            if not self.dead:
                self.vx += self.dna[self.place][0]
                self.vy += self.dna[self.place][1]
                self.x += self.vx
                self.y += self.vy
                self.place += 1
                self.oob()
                if dist(self.x + self.vx, self.y + self.vy, 50, 50) < 25:
                    self.kill()
                    self.x = 50
                    self.y = 50
        else:
            self.dead = True
            self.fitness = dist(self.x, self.y, 50, 50)
           
    def show(self):
        fill(self.marker)
        translate(self.x, self.y)
        rotate(PVector(self.vx, self.vy).heading() + PI/2)
        triangle(0, -10, -5, 10, 5, 10)
        resetMatrix()

poolsize = 500
borgir = food(50, 50, 30)
deadpool = []
pool = []
gen = 1
started = False
avg = 0
solved = False

points = []
walls = []
row = []
for i in range(w):
    row.append(0)
for i in range(h):
    walls.append(row)

thresh = float(20)
champs = (thresh/100)*(poolsize)

def draw():
    global avg
    global pool
    global deadpool
    global gen
    global walls
    global started
    global champs
    global thresh
    global points
    loadPixels()
    
    background(50)
    borgir.show()
    fill(200, 15, 200)
    textSize(30)

    stroke(50)
    if mouseButton == 37:
        if [mouseX, mouseY] not in points:
            points.append([mouseX, mouseY])
        fill(15, 130, 250)
    if not started:
        if mouseButton == 39:
            started = True 
            for i in range(0, poolsize):
                pool.append(walker(mouseX, mouseY))
    noStroke()
    for i in points:
        fill(15, 130, 250)
        ellipse(i[0], i[1], 24, 24)
    stroke(50)
    if started:  
        for i in pool:
            for k in points:
                if dist(i.x, i.y, k[0], k[1]) < 12:
                    i.kill()
            i.move()
            i.show()
            fill(250, 30, 100)
            text(i.place, 630, 40)
            if i.dead:
                deadpool.append(i)
                pool.remove(i)
        try:
            for i in range(0, len(deadpool)):
                deadpool[i].show()
                avg += deadpool[i].fitness
                deadpool.sort(key=operator.attrgetter('fitness'))
                if i <= champs+1:
                    deadpool[i].marker = color(250, 15, 130)
                else:
                    deadpool[i].marker = color(15, 250, 150)
                if len(deadpool) == poolsize:
                    for j in range(int(champs), poolsize):
                        deadpool[j].mutate(deadpool[random.randint(0, champs)].dna, 20, 80)
                    for k in deadpool:
                        pool.append(k)
                        k.reset()
                    deadpool = []
                    gen += 1
        except IndexError:
            pass
    try:
        avg /= len(deadpool)
        text(avg, 490, 40)
        avg = 0
    except:
        pass
    fill(250, 15, 200)
    text(gen, 710, 40)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
