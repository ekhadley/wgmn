import random, time
w = 600
h = 600
def setup():
    size(w, h)
    background(30)
    noStroke()
    

class particle():
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.marker = color(20, 250, 125)
        self.state = 1
        global particles
        
    def show(self):
        fill(self.marker)
        ellipse(self.pos.x, self.pos.y, 8, 8)
        
    def update(self):
        self.ord = round(self.pos.x/50) + round(self.pos.y/50)*w/50
        for i in particles:
            d = dist(self.pos.x, self.pos.y, i.pos.x, i.pos.y)
            if d < 8 and not i.state:
                self.state = 0
        if self.state:
            self.pos += PVector(random.randint(-5, 5)*.8, random.randint(-5, 5)*.8)
        else:
            self.marker = color(250, 30, 5)
        

particles = [particle(w/2, h/2)]
particles[0].state = 0
for i in range(100):
    particles.append(particle(random.randint(0, w), random.randint(0, h)))

cells = []
for i in range(w/50*h/50):
    cells.append([])

def draw():
    stime = time.time()
    background(30)
    
    for i in particles:
        i.update()
        i.show()

    mcell = round(mouseX/50) + round(mouseY/50)*w/50
    print(mcell)

    #print(1/(time.time()-stime))


























































