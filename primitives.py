import numpy as np
import math
from transformations import *
#TODO: Arcs, Rectangles, Triangles, and scanline for closed shapes
    
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
    

class Circle:
    def __init__(self, centre=Point(0,0), radius=200, filled=False):
        self.centre = centre
        self.radius = radius
        self.filled = filled
        self.vertices = []

    def midpoint(self):
        t1 = self.radius / 16
        x = self.radius
        y = 0
        while x >= y:
            if not self.filled:
                self.vertices.extend([
                    Point(self.centre.x + x, self.centre.y + y, self.centre.color),
                    Point(self.centre.x + y, self.centre.y + x, self.centre.color),
                    Point(self.centre.x - x, self.centre.y + y, self.centre.color),
                    Point(self.centre.x - y, self.centre.y + x, self.centre.color),
                    Point(self.centre.x + x, self.centre.y - y, self.centre.color),
                    Point(self.centre.x + y, self.centre.y - x, self.centre.color),
                    Point(self.centre.x - x, self.centre.y - y, self.centre.color),
                    Point(self.centre.x - y, self.centre.y - x, self.centre.color),
                ])
            else:
                self.vertices.extend(
                    Line(
                        Point(self.centre.x + x, self.centre.y + y, self.centre.color),
                        Point(self.centre.x - x, self.centre.y + y, self.centre.color)
                        ).ls())
                self.vertices.extend(Line(
                        Point(self.centre.x + y, self.centre.y + x, self.centre.color),
                        Point(self.centre.x - y, self.centre.y + x, self.centre.color)
                        ).ls())
                self.vertices.extend(Line(
                        Point(self.centre.x + x, self.centre.y - y, self.centre.color),
                        Point(self.centre.x - x, self.centre.y - y, self.centre.color)
                        ).ls())
                self.vertices.extend(Line(
                        Point(self.centre.x - y, self.centre.y - x, self.centre.color),
                        Point(self.centre.x + y, self.centre.y - x, self.centre.color)
                        ).ls())

            y += 1
            t1 = t1 + y
            t2 = t1 - x
            if t2 >= 0:
                t1 = t2
                x -= 1

    def ls(self):
        if len(self.vertices) == 0:
            self.midpoint()
        return self.vertices
    
class Arc(Circle):
    def __init__(self, centre=Point(0, 0), radius=200, filled=False, quadrants=[]):
        super().__init__(centre, radius, filled)
        self.quadrants = quadrants

    def ls(self):
        verts = super().ls()
        final_verts = []
        for point in verts:
            if 1 in self.quadrants:
                if point.x >= 0 and point.y >= 0:
                    final_verts.append(point)
            if 2 in self.quadrants:
                if point.x < 0 and point.y >= 0:
                    final_verts.append(point)
            if 3 in self.quadrants:
                if point.x < 0 and point.y < 0:
                    final_verts.append(point)
            if 4 in self.quadrants:
                if point.x >= 0 and point.y < 0:
                    final_verts.append(point)
        self.vertices = final_verts
        return self.vertices
    

#TODO: Implement transformation matrices and add them to all Primitives

def translate(shape, tx, ty):
    points = shape.ls()
    translate_mat = np.array([[1, 0, tx],
                             [0, 1, ty],
                             [0, 0, 1]])
    color = points[0].color
    final = []
    for point in points:
        vec = np.array([[point.x], [point.y], [1]])
        newPoint = translate_mat @ vec
        final.append(Point(newPoint[0,0], newPoint[1,0], color=color))
    shape.vertices = final
    return shape

def reflect_y(shape):
    points = shape.ls()
    reflect_mat = np.array([[-1, 0, 0],
                            [ 0, 1, 0],
                            [ 0, 0, 1]])
    color = points[0].color
    final = []
    for point in points:
        vec = np.array([[point.x], [point.y], [1]])
        newPoint = reflect_mat @ vec
        final.append(Point(newPoint[0,0], newPoint[1,0], color=color))
    shape.vertices = final
    return shape

