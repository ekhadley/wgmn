import turtle
t = turtle.Turtle()

t.penup()
t.speed(0)
l = turtle.Turtle()



def rect(x, y, w, h, c):
    t.fillcolor(c)
    t.begin_fill()
    t.setposition(x, y)
    t.pendown()
    t.setheading(90)
    t.forward(h)
    t.setheading(0)
    t.forward(w)
    t.setheading(270)
    t.forward(h)
    t.setheading(180)
    t.forward(w)
    t.end_fill()
    t.penup()

def circle(x, y, r, c):
    t.setpos(x, y)
    t.color(c)
    t.pendown()
    t.dot(r)
    t.penup()

def triangle(x, y, i, j, a, b, c):
    t.setpos(x, y)
    t.fillcolor(c)
    t.begin_fill()
    t.pendown()
    t.setpos(i, j)
    t.setpos(a, b)
    t.setpos(x, y)
    t.end_fill()
    t.penup()

holdback = True
while holdback:
    try:
        skyColor = input("What color should the sky be? (sky blue reccomended) ")
        l.fillcolor(skyColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')

holdback = True
while holdback:
    try:
        houseColor = input("what color should the house be? ")
        l.fillcolor(houseColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        roofColor = input("What color should the roof be?")
        l.fillcolor(roofColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        firstWindowColor = input("What should the color of the first window be? ")
        l.fillcolor(firstWindowColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        secondWindowColor = input("What should the color of the second window be? ")
        l.fillcolor(secondWindowColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        thirdWindowColor = input("What should the color of the third window be? ")
        l.fillcolor(thirdWindowColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        doorColor = input("What color should the door be?")
        l.fillcolor(doorColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        firstTreeColor = input("What is the color of the first tree? ")
        l.fillcolor(firstTreeColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        secondTreeColor = input("What is the color of the second tree? ")
        l.fillcolor(secondTreeColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')
holdback = True
while holdback:
    try:
        thirdTreeColor = input("What is the color of the third tree? ")
        l.fillcolor(thirdTreeColor)
        holdback = False
    except:
        print('Color not recognized, please try again. ')

leftedge = -380
center = -230

rect(-600, -600, 5000, 5000, 'sky blue')
rect(-600, -600, 5000, 5000, 'sky blue')
rect(-600, -700, 1100, 500, 'green')
triangle(50, -200, 240, 80, 420, -200, 'grey')
triangle(-50, -200, 140, 100, 350, -200, 'grey')
triangle(250, -200, 400, 60, 570, -200, 'grey')
circle(420, 350, 100, 'yellow')
t.color("black")

rect(leftedge, -400, 300, 300, houseColor)
triangle(leftedge, -100, -80, -100, -230, 100, roofColor)
circle(center, -20, 60, firstWindowColor)
rect(leftedge+40, -250, 60, 80, firstWindowColor)
rect(leftedge+200, -250, 60, 80, secondWindowColor)
rect(center-40, -400, 80, 120, doorColor)
rect(100, -400, 40, 220, "brown")
rect(200, -350, 40, 220, "brown")
rect(300, -300, 40, 220, "brown")
circle(320, -80, 130, thirdTreeColor)
circle(220, -130, 130, secondTreeColor)
circle(120, -180, 130, firstTreeColor)

turtle.done()


















