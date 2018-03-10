from turtle import *


def drawtriangle(size=100, bo=True, c="red"):
    color(c)
    if bo:
        begin_fill()
    for x in range(3):
        forward(size)
        left(240)
    if bo:
        end_fill()


def drawpentagon(size=100, bo=True, c="red"):
    color(c)
    if bo:
        begin_fill()
    for x in range(5):
        forward(size)
        left(72)
    if bo:
        end_fill()


def drawoct(size=100, bo=True, c="red"):
    color(c)
    if bo:
        begin_fill()
    for x in range(8):
        forward(size)
        left(45)
    if bo:
        end_fill()


def drawhex(size=100, bo=True, c="red"):
    color(c)
    if bo:
        begin_fill()
    for x in range(6):
        forward(size)
        left(60)
    if bo:
        end_fill()


def drawcircle(size=100, bo=True, c="red"):
    color(c)
    if bo:
        begin_fill()
    circle(size)
    if bo:
        end_fill()


def drawstar(size=100, bo=True, c="red"):
    color(c)
    if bo:
        begin_fill()
    for x in range(5):
        forward(size)
        right(144)
    if bo:
        end_fill()
