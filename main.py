from window import Window
from primitives import Point, Line, Circle
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
d = Drawing(SCREEN)

d.add_shape(y)
d.add_shape(x)
d.add_shape(c)
d.add_shape(e1)
d.add_shape(e2)
d.add_shape(b1)
d.add_shape(b2)
d.add_shape(m)
Window(drawing=d, screen=SCREEN)