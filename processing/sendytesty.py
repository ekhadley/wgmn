def setup():
    size(200, 200)
    background(50)

i = 0

def draw():
    global i
    translate(100, 100)
    i += .1
    rotate(i)
    background(30)
    noStroke()
    fill(255, 0, i%255)
    ellipse(-15, 50, 35, 35)
    ellipse(15, 50, 35, 35)
    ellipse(0, 5, 25, 90)
