from turtle import *
from turtle1 import *

coord_list = [
    (-100, 100, 800),
    (100, 100, 20),
    (100, -100, 55),
    (-100, -100, 100)]

for coord in coord_list:
    up()
    home()
    x, y ,z = coord
    setheading(270)
    forward(x)
    setheading(0)
    forward(y)
    down()
    draw_square(z)

mainloop()
