import time, random, math
import turtle

width = int(input('width of window? (must be greater than 250 to accomodate the bin size)'))
height = int(input('height of window?'))
vx = float(input("what is the x velocity"))
vy = float(input("what is the y velocity"))

x = 0
y = 0

binX = random.randint(-width/2 + 50, width/2 - 50)
t = turtle.Turtle()
t.screen.setup(width + 20, height + 20)
t.shape('circle')
t.penup()
t.setposition(binX, -height/2-30)

def rect(x):
    turtle.tracer(0)
    t.begin_fill()
    t.setposition(x, -height/2-30)
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(100)
    t.setheading(270)
    t.forward(50)
    t.end_fill()
    turtle.tracer(1)
t.pendown()
rect(binX)
t.penup()
while 1:
    if (y + vy) > (height)/2:
        vy *= -1
        y = (height)/2
    if (y + vy) < -(height)/2:
        vy *= -1
        y = -(height)/2
    if (x + vx) > (width)/2:
        vx *= -1
        x = (width)/2
    if (x + vx) < -(width)/2:
        vx *= -1
        x = -(width)/2
    else:
        x += vx
        y += vy
    if y < -height/2+20:
        if x in range(binX-100, binX):
            print('game over')
            break
    t.setposition(x, y)
    print(vx, ', ', vy)






















