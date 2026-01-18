from turtle import *
tracer(1)
koef = 20

right(90)

for i in range(4):
    for z in range(4):
        forward(6 * koef)
        right(90)
    forward(10 * koef)
    right(90)
    forward(3 * koef)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef,y * koef)
        dot(3)
exitonclick()