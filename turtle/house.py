from turtle import *


title('House Drawing')
setup(width=.75, height=.60, startx=0, starty=0)
bgcolor('light blue')
speed(0)


def start(x, y):
    pu()
    seth(0)
    setposition(x, y)
    pd()


def drawhouse():
    start(-200, 100)
    color("#701e14")
    begin_fill()
    for x in range(2):
        fd(719)
        rt(90)
        fd(300)
        rt(90)
    end_fill()


def brick():
    pencolor('black')
    for x in range(2):
        fd(30)
        rt(90)
        fd(10)
        rt(90)


def buildbrick():

    x, y = (-470, 100)
    setposition(x, y)
    for i in range(17):
        while y != -190:
            brick()
            y -= 10
            pu()
            setposition(x, y)
            pd()
        x += 30
        while y != 100:
            brick()
            pu()
            setposition(x, y)
            y += 10
            pd()
        x += 30


def buildroof():
    pencolor('black')
    start(-220, 100)
    color('#1E1412')
    begin_fill()
    fd(759)
    lt(160)
    fd(405)
    lt(40)
    fd(405)
    end_fill()


def topwindow():
    start(-140, 80)
    x, y = (-140, 80)
    color('#1F5054')
    for i in range(5):
        for j in range(2):
            begin_fill()
            fd(60)
            rt(90)
            fd(90)
            rt(90)
            end_fill()

        x += 135
        pu()
        setposition(x, y)
        pd()


def bottomwindow():
    start(-140, -40)
    x, y = (-140, -40)
    color('#1F5054')
    for i in range(5):
        for j in range(2):
            begin_fill()
            fd(60)
            rt(90)
            fd(90)
            rt(90)
            end_fill()
        x += 135
        pu()
        setposition(x, y)
        pd()


def door():
    color('black')
    start(130, -40)
    for x in range(2):
        begin_fill()
        fd(80)
        rt(90)
        fd(140)
        rt(90)
        end_fill()
    seth(0)
    x, y = (150, -120)
    setposition(x, y)
    pd()
    color('silver')
    begin_fill()
    circle(5)
    end_fill()


def porch():
    start(120, -180)
    color('gray')
    for x in range(2):
        begin_fill()
        fd(100)
        rt(90)
        fd(35)
        rt(90)
        end_fill()


def grass():
    start(-900, -200)
    color('green')
    for i in range(2):
        begin_fill()
        fd(2000)
        rt(90)
        fd(400)
        rt(90)
        end_fill()


def sun():
    start(-600, 100)
    color('yellow')
    begin_fill()
    circle(90)
    end_fill()


def garage():
    start(-500, 100)
    color("#701e14")
    begin_fill()
    for x in range(2):
        fd(300)
        rt(90)
        fd(300)
        rt(90)
    end_fill()


def garageroof():
    start(-520, 100)
    pencolor('black')
    color('#1E1412')
    begin_fill()
    fd(340)
    lt(160)
    fd(170)
    lt(38)
    fd(170)
    end_fill()


def garagedoor():
    start(-470, 30)
    color('#F3F4E5')
    begin_fill()
    for x in range(2):
        fd(250)
        rt(90)
        fd(225)
        rt(90)
    end_fill()
    pencolor("black")
    pu()
    fd(83)
    rt(90)
    pd()
    fd(225)
    lt(90)
    pu()
    fd(83)
    lt(90)
    pd()
    fd(225)
    start(-470, -60)
    fd(250)
    rt(90)
    pu()
    fd(75)
    pd()
    rt(90)
    fd(250)
    start(-450, 10)
    x, y = (-450, 10)
    color('#1F5054')
    for j in range(3):
        begin_fill()
        for i in range(4):
            fd(50)
            rt(90)
        pu()
        x += 80
        setposition(x, y)
        pd()
        end_fill()


drawhouse()
garage()
garageroof()
buildbrick()
buildroof()
topwindow()
bottomwindow()
door()
grass()
porch()
sun()
garagedoor()
