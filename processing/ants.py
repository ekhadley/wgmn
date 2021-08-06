import math, time, random

def setup():
    size(big, big)
    background(30)


sav = []
big = 800


for i in range(big):
    sav.insert(i, [])
    for j in range(big):
        sav[i].insert(j, 0)


class ant():
    def __init__(self, x, y):
        self.diet = 2
        self.pos = PVector(x, y)
        self.mode = 'search'
        self.marker = color(180, 30, 30)
        self.target = random.randint(0, self.diet)
        self.path = []
        
        
    def walk(self):
        if self.mode == 'search':
            sav[int(self.pos.x)][int(self.pos.y)] -= dist(int(self.pos.x), int(self.pos.y), foods[self.target].pos.x, foods[self.target].pos.y)
            
            self.path.append(self.pos)
        
            best = PVector(0, 0, 100000000)
            neighbors = []
            
            neighbors.append(PVector(-1, -1))
            neighbors.append(PVector(-1, 0))
            neighbors.append(PVector(-1, 1))
            neighbors.append(PVector(0, 1))
            neighbors.append(PVector(0, -1))
            neighbors.append(PVector(1, -1))
            neighbors.append(PVector(1, 0))
            neighbors.append(PVector(1, 1))
    
            for k in neighbors:
                k.z = dist(self.pos.x + k.x, self.pos.y + k.y, foods[self.target].pos.x, foods[self.target].pos.y) + sav[int(self.pos.x)][int(self.pos.y)]
                k.z += sav[int(self.pos.x)][int(self.pos.y)]
                if k.z < best.z:
                    best = k
    
            if random.randint(0, 100) > 80:
                step = PVector(best.x, best.y)
            else:
                step = PVector(random.randint(-1, 1), random.randint(-1, 1))    
            

            
            if self.pos.x + step.x > 0 and self.pos.x + step.x < 800 and self.pos.y + step.y > 0 and self.pos.y + step.y < 800:
                self.pos.x += step.x
                self.pos.y += step.y
        
    def show(self):
        fill(self.marker)
        noStroke()
        ellipse(int(self.pos.x), int(self.pos.y), 5, 5)

    

      
          
class food():
    def __init__(self):
        self.foodSize = random.randint(10, 100)
        self.marker = color(150, 30, 150)
        self.pos = PVector(random.randint(10, 790), random.randint(10, 790))
        while dist(int(self.pos.x), int(self.pos.y), 400, 400) < 100:
            self.pos = PVector(random.randint(10, 790), random.randint(10, 790))
               
               
    def show(self):
        fill(self.marker)
        ellipse(int(self.pos.x), int(self.pos.y), self.foodSize/2, self.foodSize/2)

    
colony = []
for i in range(30):
    colony.append(ant(400, 400)) 
    
foods = []
for i in range(3):
    foods.append(food())



def draw():   

#    background(30)

    if mouseButton == 37:
        colony.append(ant(mouseX, mouseY))        

    if random.randint(-8000, 1) > 0:
        foods.append(food())
        for i in colony:
            i.diet = len(foods)-1
            i.target = random.randint(0, i.diet)
        
        
    for i in foods:
        noStroke()
        i.show()
    
    for i in colony:
        noStroke
        i.walk()
        i.show()
        strokeWeight(.01)
        stroke(255)
#      line(i.pos.x, i.pos.y, foods[i.target].pos.x, foods[i.target].pos.y)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
