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
        self.vertices = 0
        self.processed_verts = False

    def add_shape(self, shape):
        self.shapes.append(shape) # Shape object must have Points

    def compute_vertices(self):
        # POINT FORMAT --> x, y, colour info
        for shape in self.shapes:
            if shape.isinstance(Point): # just add points
                self.vertices.extend(shape.ls())
                continue
            points = shape.ls()
            for point in points:
                self.vertices.extend(point.ls())

    def screentoNDC(self): # could do this in shader???
        for i in range(0, len(self.vertices), 5):
            self.vertices[i] = self.vertices[i]/self.screenSize[0]
            self.vertices[i + 1] = self.vertices[i + 1]/self.screenSize[1]
            # color info
            self.vertices[i + 2] = self.vertices[i + 2]/256
            self.vertices[i + 3] = self.vertices[i + 3]/256
            self.vertices[i + 4] = self.vertices[i + 4]/256

    def ls(self): # SHOULD SETUP VAO!!!!
        if not self.processed_verts:
            self.compute_vertices()
            # self.screentoNDC() # trying this in shader
        self.vertices = array(self.vertices, dtype=float32)
        self.vertex_count = len(self.vertices)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(8))