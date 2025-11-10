from turtle import *
tracer(0)
koef = 20

right(90)
for i in range(4):
    forward( 7* koef)
    right(90)
    forward(7 * koef)
    left(90)
    forward(7 * koef)
    right(90)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)


for i in range(1):
    back(10 * koef)
    right(90)
    forward(8 * koef)
    left(90)
down()

for i in range(2):
    forward(16 * koef)
    right(90)
    forward(8 * koef)
    right(90)


exitonclick()