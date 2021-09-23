w, h = 600, 600
def setup():
    size(600, 600)
    background(30)
    
class wire():
    def __init__(self, x, y, a, b):
        self.pos1 = PVector(x, y)
        self.pos2 = PVector(a, b)
        self.markers = [color(250, 0, 30), color(15, 230, 120)]
        self.state = 0
        self.OUT = []
    def show(self):
        strokeWeight(5)
        stroke(self.markers[self.state])
        line(self.pos1.x, self.pos1.y, self.pos2.x, self.pos2.y)
        for i in self.OUT:
            pass

class AND():
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.markers = [color(250, 0, 30), color(15, 230, 120)]
        self.state = 0
        self.OUT = []
        self.IN = []
    def update(self):
        global mouses
        if (not mouses[0] and mouses[1]) and (mouseButton == 37) and (dist(mouseX, self.pos.x, mouseY, self.pos.y) < 30):
            self.state = not self.state
        for i in self.OUT:
            i.state = self.state
    def show(self):
        fill(self.markers[self.state])
        ellipse(self.pos.x, self.pos.y, 30, 30)

class XOR():
    pass

class toggle():
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.markers = [color(250, 0, 30), color(15, 230, 120)]
        self.state = 0
        self.OUT = []
    def update(self):
        global mouses
        if (not mouses[0] and mouses[1]) and (mouseButton == 37) and (dist(mouseX, mouseY, self.pos.x, self.pos.y) < 30):
            self.state = not self.state
        for i in self.OUT:
            i.state = self.state
    def show(self):
        fill(self.markers[self.state])
        ellipse(self.pos.x, self.pos.y, 30, 30)
    
w = wire(300, 300, 500, 450)
t = toggle(300, 300)
t.OUT.append(w)

mouses = [0, 0]
def draw():
    background(30)
        
    mouses.append(mousePressed)
    mouses.pop(0)
    
    t.update()
    t.show()
    w.show()
    