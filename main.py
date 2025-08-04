from window import Window
from primitives import Point
from drawing import Drawing
SCREEN=(800,90) # can make this configurable

p = Point(400, 45)
d = Drawing(SCREEN, [p])
Window(screen=SCREEN)