import numpy as np
class Point:
    def __init__(self, x, y, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color

    def ls(self):
        r, g, b = self.color
        return [self.x, self.y, r, g, b]
    
class Line:
    def __init__(self, start:Point, end:Point):
        self.start = start
        self.end = end

    def _bressenham(self):
        x1 = self.start.x
        y1 = self.start.y
        x2 = self.end.x
        y2 = self.end.y
        if x1 > x2:
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        verts = [self.start]
        dx = x2 - x1
        dy = y2 - y1 # neg
        neg = False
        if dy < 0:
            neg = True
            dy = -dy
        p = 2*dy - dx # neg
        x = x1
        y = y1
        if x1 != x2:
            while x <= x2: # need to add a case for lines that go straight up
                if p < 0:
                    x += 1
                    p += 2*dy # neg
                else:
                    x += 1
                    if not neg:
                        y += 1
                    else:
                        y -= 1
                    p += 2*dy - 2*dx
                verts.append(Point(x, y, self.start.color))
        else:
            if y1 > y2:
                y1, y2 = y2, y1
                y = y1
            while y < y2:
                y += 1
                verts.append(Point(x, y, self.start.color))

        return verts
    
    def ls(self):
        return self._bressenham()