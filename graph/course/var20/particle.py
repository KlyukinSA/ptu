import numpy as np
import math
from OpenGL.GL import *


PLATE_MAX_FORCE = 0.001
PLATE_MAX_DISTANCE = 20
PARTICLE_MAX_VELOCITY = 0.03
PARTICLE_COLOR = [1.0, 1.0, 1.0, 1.0]
X_MAX = 0.01
Y_MAX = 0.01
Z_MAX = 0.01
D_MAX = math.sqrt(X_MAX**2 + Y_MAX**2 + Z_MAX**2)
ATTRACTOR_RADIUS = 8
class Particle:
    def __init__(self, position, velocity, life_time, plate_magnitude_area, plate_side):
        self.position = np.array(position, dtype=np.float64)
        self.emitter_position = np.array(position, dtype=np.float64)
        self.velocity = np.array(velocity, dtype=np.float64)
        self.life_time = life_time
        self.max_life_time = life_time
        self.plate_magnitude_area = plate_magnitude_area
        self.plate_side = plate_side
        self.color = [0.5, 0.8, 0.8, 1.0]
    def getDistance(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    def update(self, attractor_position):
        x1, y1, z1 = self.position
        x2, y2, z2 = attractor_position
        x_dist = x2 - x1
        y_dist = y2 - y1
        z_dist = z2 - z1
        x_vec = x_dist / abs(x_dist)
        y_vec = y_dist / abs(y_dist)
        z_vex = z_dist / abs(z_dist)
        move_vector = [0, 0, 0]
        # считаем расстояние до аттрактора
        distance = self.getDistance(self.position, attractor_position)
        if (self.color[0] < 1):
            self.color[0] += 1 / (self.life_time)
        else:
            if (self.color[1] > 0.5):
                self.color[1] -= 1 / (self.life_time)
            else:
                if (self.color[2] > 0.4):
                    self.color[2] -= 1 / (self.life_time)
        # логика аттрактора
        if distance <= ATTRACTOR_RADIUS and distance > D_MAX:
            # увеличиваем скорость приближения к аттрактору
            self.velocity[0] += (x_dist) / 500
            self.velocity[1] += (y_dist) / 500
            self.velocity[2] += (z_dist) / 500
            # определяем положение относительно ускорения
            if (abs(x_dist) < abs(self.velocity[0])):
                move_vector[0] = x_dist
            else:
                move_vector[0] = self.velocity[0]
            if (abs(y_dist) < abs(self.velocity[1])):
                move_vector[1] = y_dist
            else:
                move_vector[1] = self.velocity[1]
            if (abs(z_dist) < abs(self.velocity[2])):
                move_vector[2] = z_dist
            else:
                move_vector[2] = self.velocity[2]
        else:
            if distance <= D_MAX:
                move_vector = x_dist, y_dist, z_dist
            else:
                move_vector = self.velocity
        self.position += move_vector
        self.life_time -= 1
    def reachedAttractor(self, attractor_position):
        x1, y1, z1 = self.position
        x2, y2, z2 = attractor_position
        return self.getDistance(self.position, attractor_position) <= D_MAX
    def draw(self):
        glPushMatrix()
        self.drawParticle(2, [self.position[0], self.position[1], self.position[2]])
        glPopMatrix()
    def drawParticle(self, size, position):
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_POINT_SPRITE)
        glEnable(GL_VERTEX_PROGRAM_POINT_SIZE)
        glPointSize(size)
        glBegin(GL_POINTS)
        # тут надо вспомнить что влияет на яркость и впихнуть сюда параметр функции, который ты передашь после его интерполяции
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.color)
        glVertex3f(position[0], position[1], position[2])
        glEnd()
        glDisable(GL_POINT_SMOOTH)
        glDisable(GL_BLEND)
        glDisable(GL_POINT_SPRITE)
        glDisable(GL_VERTEX_PROGRAM_POINT_SIZE)
