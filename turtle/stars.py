# import random for random number generation
import random
# import drawstar from my shapes.py module
from shapes import drawstar
# import everything from turtle
from turtle import *
# turn background blue using turtle
bgcolor('blue')
# run a for loop to draw a bunch of stars
for x in range(100):
    # set turtle to fastest speed
    speed(0)
    # turtle pen up
    pu()
    # set x and y position of the turtle using randomly generated interegers from -400 to 400
    setposition(random.randint(-400, 400), random.randint(-400, 400))
    # pen down
    pd()
    # use my drawstar function in my shape.py and
    # pass it a random size from 7 to 25, fill in True, color yellow
    drawstar(random.randint(7, 25), True, 'yellow')
