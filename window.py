import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Window:
    def __init__(self, drawing=None, screen=(800,1000), clearColor=(24.0/255.0, 84.0/255.0, 122.0/255.0, 1.0)):
        pg.init()
        self.screen = screen
        pg.display.set_mode(screen, pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.drawing = drawing

        r, g, b, a = clearColor
        glClearColor(r, g, b, a)
        glEnable(GL_PROGRAM_POINT_SIZE)

        self.mainloop()

    def mainloop(self):
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT :
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)

            pg.display.flip() # swap buffers ig?

            self.clock.tick(60)