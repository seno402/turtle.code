import turtle

my_wn=turtle.Screen()
my_pen=turtle.Turtle()
size=100

while True:
    for i in range(4):
        my_pen.fd(size)
        my_pen.left(90)
        size+=20
    size+=20
    
turtle.done()