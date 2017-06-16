import turtle


def tilted_square():
    turtle.left(angle)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

angle = 20            # <--
for i in range(1, 12, 1):
    #print(i)
    tilted_square()
    tilted_square()
    tilted_square()
