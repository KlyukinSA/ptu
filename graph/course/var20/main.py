import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame import DOUBLEBUF, OPENGL, K_UP, K_DOWN, K_RIGHT, K_q, K_w, K_LEFT
from emitter import Emitter


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0.0, 0.0, 0.0, 1)
LIGHT_POS = (2, 5, -2)
LIGHT_COLOR = (1, 1, 1)
LIGHT_INTENSIVE = (0.2, 0.2, 0.2)
EMITTER_SIZE = 3
EMITTER_POSITION = np.array([0, 0, 0])
EMITTER_DIRECTION = np.array([0, 1, 0])
CONE_HEIGHT = 5
CONE_RADIUS = 1
CONE_MAGNITUDE_AREA = 5
PLATE_COLOR = (0.0, 0.0, 0.0, 1)
PARTICLES_MAX_NUM = 1000
PARTICLE_MAX_TIME = 1000
ATTRACTOR_COLOR = [1.0, 1.0, 1.0, 1.0]
ATTRACTOR_POSITION = [5, 2, 7]
particles = []
emitter = Emitter(EMITTER_SIZE,
    EMITTER_POSITION,
    EMITTER_DIRECTION,
    CONE_MAGNITUDE_AREA,
    CONE_HEIGHT,
    PARTICLE_MAX_TIME,
    CONE_RADIUS)
def drawAttractor():
    glPushMatrix()
    glPointSize(10)
    glBegin(GL_POINTS)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, ATTRACTOR_COLOR)
    glVertex3f(ATTRACTOR_POSITION[0], ATTRACTOR_POSITION[1],
    ATTRACTOR_POSITION[2])
    glEnd()
    glPopMatrix()
def update_particles():
    global particles, emitter
    if len(particles) < PARTICLES_MAX_NUM:
        particles.append(emitter.emit_particle())
    # print(particles[0].color)
    for particle in particles:
        particle.update(ATTRACTOR_POSITION)
        if (particle.life_time <= 0) or (particle.reachedAttractor(ATTRACTOR_POSITION)):
            particles.remove(particle)
def main():
    global particles, emitter
    pygame.init()
    display = (900, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glutInit()
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.01, 150.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LIGHT_COLOR)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LIGHT_INTENSIVE)
    cam_x = 0
    cam_y = 12
    cam_z = 4
    cam_orientation = [0, 0, 1]
    cam_look_at = [0, 0, 4]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            # cam_x = 10
            cam_y += 1
            # cam_z = 6
            # cam_orientation = [0, 1, 0]
            # cam_look_at = [0, 0, 5]
        if pressed[K_DOWN]:
            # cam_x = 0
            cam_y -= 1
            # cam_z = 4
            # cam_orientation = [0, 0, 1]
            # cam_look_at = [0, 0, 4]
        if pressed[K_RIGHT]:
            cam_x += 1
            # cam_y = 0
            # cam_z = 4
            # cam_orientation = [0, 1, 0]
            # cam_look_at = [0, 0, 4]
        if pressed[K_LEFT]:
            cam_x -= 1
            # cam_y = 0
            # cam_z = 8
            # cam_orientation = [0, 1, 0]
            # cam_look_at = [0, 0, 4]
        glClearColor(*BACKGROUND_COLOR)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawAttractor()
        emitter.draw()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1, 1, -display[1] / display[0], display[1] / display[0], 1, 400)
        gluLookAt(cam_x, cam_y, cam_z, *cam_look_at, *cam_orientation)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glMatrixMode(GL_MODELVIEW)
        glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POS)
        for particle in particles:
            particle.draw()
        # if pressed[K_q]:
        update_particles()
        pygame.display.flip()
        pygame.time.wait(10)

main()
