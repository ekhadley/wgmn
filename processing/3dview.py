w, h = 600, 600
def setup():
    size(w, h)
    background(30)

def vshow(pos, vec, m, w):
    strokeWeight(w)
    stroke(m)
    line(pos.x, pos.y, pos.x + vec.x, pos.y + vec.y)

def proj(t, v):
    return t.x*v.x + t.y*v.y + t.z*v.z

class wireframe():
    def __init__(wires):
        self.wires = []
        for i in wires:
            self.wires.append(PVector(i[0], i[1], i[2]))
        self.marker = color(0, 50, 200)
        
    def show(self):
        global viewvec
        wire = self.wires[0] - self.wires[1]
        Pwire = proj(wire, viewvec)
        line(pwire.x, pwire.y, wires[0].x, wires[0].y)
    
qwe = wireframe([PVector(300, 300, 0), PVector(300, 300, 300)])
viewvec = PVector(0, 0, 1)
viewpos = PVector()

def draw():
    background(50)
    qwe.show()













































































































