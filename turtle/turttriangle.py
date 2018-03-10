from turtle import *


if __name__ == '__main__':

    def drawtriangle(size=100):
        for x in range(3):
            forward(size)
            left(240)

    def drawpentagon(size=100):
        for x in range(5):
            forward(size)
            left(72)

    def drawoct(size=100):
        for x in range(8):
            forward(size)
            left(45)

    def drawhex(size=100):
        for x in range(6):
            forward(size)
            left(60)

    def drawcircle(size=100):
        pencolor('blue')
        circle(size)

    def drawstar(size=100):
        for x in range(5):
            forward(size)
            right(144)
