import turtle


def stair(size, nb):
    for a in range(0,nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)

def square(size):
    for _ in range(0,4):
        t.forward(size)
        t.left(90)

def squares(size_int, nb):
    for i in range(0, nb):
        size = (i+1)*size_int
        square(size)
        
t = turtle.Turtle()
#stair(50,5)
squares(10, 5)
turtle.done()