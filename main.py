from window import Window
from primitives import Point, Line, Circle
from drawing import Drawing
SCREEN = (800, 1000) # can make this configurable

x = Line(Point(-400, 0), Point(400, 0))
y = Line(Point(0, 500), Point(0, -500))
c = Circle(centre=Point(200,200, (255,0,0)))
d = Drawing(SCREEN)
d.add_shape(c)

d.add_shape(y)
d.add_shape(x)

Window(drawing=d, screen=SCREEN)