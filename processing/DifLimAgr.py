'''add this shit

optimize for more particles by only doing local search of sorted list of frozen particles

'''


import random, time
w = 800
h = 800
def setup():
    size(w, h)
    background(30)
    noStroke()
     

class particle():
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.marker = color(20, 250, 125)
        self.state = 1
        self.ord = int(round(self.pos.x/50) + round(self.pos.y/50)*w/50)
        global particles
        global deadparticles
        
    def show(self):
        fill(self.marker)
        ellipse(self.pos.x, self.pos.y, 5, 5)
        
    def update(self):
        self.ord = self.pos.y*w + self.pos.x
        for i in deadparticles:
            d = dist(self.pos.x, self.pos.y, i.pos.x, i.pos.y)
            if d < 5 and not i.state:
                self.state = 0
        if self.state:
            self.pos += PVector(random.randint(-5, 5), random.randint(-5, 5))
        else:
            self.marker = color(255+frameCount*.1, 15, frameCount*.1)
        

particles = []

for i in range(1000):
    particles.append(particle(random.randint(0, w), random.randint(0, h)))

deadparticles = [particle(w/2, h/2)]
deadparticles[0].state = 0
deadparticles[0].marker = color(255, 15, 0)

def draw():
    stime = time.time()
    background(30)
    
    for i in range(len(particles)-1):
        particles[i].update()
        particles[i].show()
        if particles[i].pos.x not in range(0, w) or particles[i].pos.y not in range(0, h):
            particles.pop(i)
            particles.append(particle(random.randint(0, w), random.randint(0, h)))
        if not particles[i].state:
            deadparticles.append(particles[i])
            particles.pop(i)
            particles.append(particle(random.randint(0, w), random.randint(0, h)))
    for i in deadparticles:
        i.show()
    
    print(1/(time.time()-stime))


























































