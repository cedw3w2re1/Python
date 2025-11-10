from turtle import *
tracer(0)
koef = 20

right(90)
for i in range(5):
    forward(1  * koef)
    right(90)
    forward(3*koef)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()