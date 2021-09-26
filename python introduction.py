# this is basic python function
import turtle

mark_turtle = turtle.Turtle()


def square():

    mark_turtle.forward(100)
    mark_turtle.right(90)
    mark_turtle.forward(100)
    mark_turtle.right(90)
    mark_turtle.forward(100)
    mark_turtle.right(90)
    mark_turtle.forward(100)


square()
turtle.forward(300)
mark_turtle.forward(100)
square()

# IF ELSE STATEMENT
impala_weight = 40
goat_weight = 30

if impala_weight > goat_weight:
    square()
else:
    mark_turtle.forward(100)

# WHILE LOOP
mark = 'happy'
while mark == 'sad':  # two equal sign means checking something with another
    mark_turtle.forward(10)

# FOR LOOP
for count in range(3):
    square()
    print()

