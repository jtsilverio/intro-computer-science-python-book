import turtle

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def olympic(t):
    for i in range(5):
        t.circle(50)
        jump(t, t.position()[0] + 110, t.position()[1])
        if i == 2:
            jump(t, t.position()[0] - 3 * 91, t.position()[1] - 60)


s = turtle.Screen()
s.clear()
t = turtle.Turtle()
olympic(t)