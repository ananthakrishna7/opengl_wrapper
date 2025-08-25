from window import Window
from primitives import *
from random import randint
from drawing import Drawing
SCREEN = (800, 1000) # can make this configurable

x = Line(Point(-400, 0), Point(400, 0))
y = Line(Point(0, 500), Point(0, -500))
c = Circle(centre=Point(0,0, (255,219,172)), filled=True)
e1 = Circle(centre=Point(100,0,), radius=25, filled=True)
e2 = Circle(centre=Point(-100,0,), radius=25, filled=True)
b1 = Circle(centre=Point(100,0,(0,0,0)), radius=10, filled=True)
b2 = Circle(centre=Point(-100,0,(0,0,0)), radius=10, filled=True)
m = Circle(centre=Point(0, -100,(255,0,0)), radius=25, filled=True)
s = Arc(centre=(Point(-40,-50, (255,219,172))), filled=True, quadrants=[4])
s2 = Arc(centre=(Point(40,-50, (255,219,172))), filled=True, quadrants=[3])
s3 = Arc(radius=25, centre=Point(0, 0, (0,0,0)), quadrants=[3,4])
eb = Arc(radius=30, centre=Point(0, 0, (0,0,0)), quadrants=[1,2])
rec = Rectangle(width=200, height=100, x=0, y=-200, filled=True, color=(255,0,0))
shirt = Rectangle(width=600, height=500, x=0, y=-500, filled=True, color=(255,0,0))
hand1 = Line(Point(-200,-350,(0,0,0)), Point(-200,-600,(0,0,0)))
hand2 = Line(Point(200,-350,(0,0,0)), Point(200,-600,(0,0,0)))
eb = translate(eb, 102, 15)
cxs = []
for i in range(500):
    cxs.append(Circle(centre=Point(0 + randint(-200, 200), randint(100, 250),(0,0,0)), radius=50, filled=True))
eb2 = reflect_y(translate(Arc(radius=30, centre=Point(0, 0, (0,0,0)), quadrants=[1,2]), 102, 15))
d = Drawing(SCREEN)
s3 = translate(s3, 0, -170)
# d.add_shape(y)
# d.add_shape(x)
d.add_shape(rec)
d.add_shape(shirt)
d.add_shape(hand1)
d.add_shape(hand2)
d.add_shape(c)
d.add_shape(s)
d.add_shape(s2)
d.add_shape(e1)
d.add_shape(e2)
d.add_shape(b1)
d.add_shape(b2)
d.add_shape(m)
d.add_shape(s3)
d.add_shape(eb)
d.add_shape(eb2)
for i in range(50):
    d.add_shape(cxs[i])
# d.add_shape(reflect_y(translate(eb, 102, 15)))

Window(drawing=d, screen=SCREEN)
