import turtle

angle1 = 90
distance1 = 50

def tilted_square():
    turtle.left(angle)
    turtle.forward(distance1)
    turtle.left(angle1)
    turtle.forward(distance1)
    turtle.left(angle1)
    turtle.forward(distance1)
    turtle.left(angle1)
    turtle.forward(distance1)
    turtle.left(angle1)

angle = 20            # <--
for i in range(1, 12, 1):
    #print(i)
    tilted_square()
    tilted_square()
    tilted_square()
