import numpy as np
from math import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from particle import Particle


PLATE_COLOR = (0.5, 0.5, 0.5, 1)
class Emitter:
    def __init__(self, size, position, direction, plate_magnitude_area, cone_height,
    life_time, cone_radius):
        self.size = size
        self.position = position
        self.direction = direction / np.linalg.norm(direction)
        self.plate_magnitude_area = plate_magnitude_area
        self.cone_height = cone_height
        self.life_time = life_time
        self.cone_radius = cone_radius
    def emit_particle(self):
        z = np.random.uniform(0, self.cone_height)
        heigth = (self.cone_height - z)
        tan = self.cone_radius / self.cone_height
        x = heigth * (tan) * np.random.uniform(-1, 1)
        y = heigth * (tan) * np.random.uniform(-1, 1)
        coef = 0.01
        # угол под которым вылетают частицы
        angle_x = np.radians(np.random.uniform(-180, 180))
        angle_y = np.radians(np.random.uniform(-180, 180))
        angle_z = np.radians(np.random.uniform(-180, 180))
        velocity = np.array([coef * np.cos(angle_x), coef * np.cos(angle_y), coef *
        np.cos(angle_z)])
        return Particle(np.array([x, y, z]), velocity, self.life_time, self.plate_magnitude_area, self.cone_radius)
    def draw(self):
        sides = 50
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, PLATE_COLOR)
        # glPushMatrix()
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        glEnd()
        # glFlush()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glutSolidCone(self.cone_radius, self.cone_height, sides, sides)
        # glPopMatrix()
