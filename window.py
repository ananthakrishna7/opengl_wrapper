import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

# === Shaders ===


class Window:
    def __init__(self, drawing=None, screen=(800,1000), clearColor=(24.0/255.0, 84.0/255.0, 122.0/255.0, 1.0)):
        pg.init()
        self.screen = screen
        pg.display.set_mode(screen, pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.drawing = drawing

        self.VERTEX_SHADER = """
        #version 330
        layout(location = 0) in vec2 position;
        layout(location = 1) in vec3 color;
        out vec3 vColor;

        

        void main() {
            // we assume middle of the screen as origin. 
            // SO, the screen extends till half the width and height in every direction
            vec2 screenDim = vec2""" + str(self.screen) + """;
            gl_Position = vec4((position - screenDim/2)/(screenDim/2), 0.0, 1.0);
            vColor = color/256;
        }
        """

        self.FRAGMENT_SHADER = """
        #version 330
        in vec3 vColor;
        out vec4 fragColor;
        void main() {
            fragColor = vec4(vColor, 1.0);
        }
        """

        r, g, b, a = clearColor
        glClearColor(r, g, b, a)
        glEnable(GL_PROGRAM_POINT_SIZE)
        self.shader = self.createShader()

        self.mainloop()
        
        
    def createShader(self):
        print("Compiling shaders...")

        shader = compileProgram(
            compileShader(self.VERTEX_SHADER, GL_VERTEX_SHADER),
            compileShader(self.FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
        )

        # uniformLoc = glGetUniformLocation(shader, "screenDim")
        # glUniform2f(uniformLoc, self.screen[0], self.screen[1])

        print("Shaders compiled.")

        return shader

    def mainloop(self):
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT :
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)

            glUseProgram(self.shader)
            if self.drawing == None:
                pass
            pg.display.flip() # swap buffers ig?

            self.clock.tick(60)