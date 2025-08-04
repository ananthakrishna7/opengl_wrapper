from numpy import array, float32
from primitives import Point
from OpenGL.GL import *

"""
Module for managing and processing drawable shapes for OpenGL rendering.

Classes:
    Drawing: Handles a collection of shapes, computes their vertex data, and converts coordinates to Normalized Device Coordinates (NDC).

Drawing Methods:
    __init__(screenSize, shapes=[]):
        Initializes the Drawing object with a screen size and an optional list of shapes.

    add_shape(shape):
        Adds a shape to the drawing. The shape must provide a list of Point objects.

    compute_vertices():
        Computes the vertex data for all shapes in the drawing. Supports both individual Point objects and shapes containing multiple points.

    screentoNDC():
        Converts screen coordinates of vertices to Normalized Device Coordinates (NDC) and normalizes color information.

    ls():
        Returns the processed vertex data as a NumPy array of type float32. Computes and processes vertices if not already done.
"""
class Drawing:
    def __init__(self, screenSize, shapes=[]):
        self.shapes = shapes
        self.screenSize = screenSize
        self.vertices = []
        self.processed_verts = False
        print(shapes)

    def add_shape(self, shape):
        self.shapes.append(shape) # Shape object must have Points

    def updateScreenSize(self, size):
        self.screenSize = size
        self.processed_verts = False

    def compute_vertices(self):
        # POINT FORMAT --> x, y, colour info
        self.vertices = []
        for shape in self.shapes:
            if isinstance(shape, Point): # just add points
                if shape.x < self.screenSize[0]/2 and shape.y < self.screenSize[1]/2 and shape.x > - self.screenSize[0]/2 and shape.y > -self.screenSize[1]/2:
                    self.vertices.extend(shape.ls())
                continue
            points = shape.ls()
            for point in points:
                # clipping
                if point.x < self.screenSize[0]/2 and point.y < self.screenSize[1]/2 and point.x > - self.screenSize[0]/2 and point.y > - self.screenSize[1]/2:
                    self.vertices.extend(point.ls())
            # print(self.vertices)

    def screentoNDC(self): # could do this in shader???
        w, h = self.screenSize
        for i in range(0, len(self.vertices), 5):
            # Map origin to center of screen
            self.vertices[i] = (self.vertices[i]) / (w / 2)
            self.vertices[i + 1] = (self.vertices[i + 1]) / (h / 2)
            # color info (divide by 255 for [0,1] range)
            self.vertices[i + 2] = self.vertices[i + 2] / 255
            self.vertices[i + 3] = self.vertices[i + 3] / 255
            self.vertices[i + 4] = self.vertices[i + 4] / 255
        # print('NDC vertices:', self.vertices)

    def ls(self):
        if not self.processed_verts:
            self.compute_vertices()
            self.screentoNDC()
            self.processed_verts = True
            vertices = array(self.vertices, dtype=float32)
            self.vertex_count = len(self.vertices) // 5
            self.vao = glGenVertexArrays(1)
            glBindVertexArray(self.vao)
            self.vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
            glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(8))
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glBindVertexArray(0)
        # Bind VAO and draw each frame
        glBindVertexArray(self.vao)
        glDrawArrays(GL_POINTS, 0, self.vertex_count)
        err = glGetError()
        if err != 0:
            print('OpenGL Error:', err)
        glBindVertexArray(0)