# Задание 30.
# 1. Изобразить каркасный тор и поместить его в каркасный куб. Размеры и местоположение примитивов на экране задать самостоятельно.
# 2. Промасштабировать тор с коэффициентом 1,3
# 3. Изобразить конус, сферу и куб, где вершина конуса является центром сферы, куб помещен внутрь сферы (центры куба и сферы совпадают).
# 4. Переместить сферу таким образом, чтобы ее центр совпал с центром основания конуса

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep


def drawConeSphereCube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    color = [0.5, 1.0, 0, 1.]
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, 0)
    height=100
    glutWireCone(50, height, 20, 10)
    glPopMatrix()
    glPushMatrix()
    color = [1.0, 0.5, 0., 0.5]
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, height)
    r=50
    glutWireSphere(r, 20, 10)
    glPopMatrix()
    glPushMatrix()
    color = [1., 1., 1., 1]
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, height)
    glutWireCube(2 * r / 1.8)
    glPopMatrix()

    glutSwapBuffers()
    sleep(1)
def moveConeSphereCube():
    n=20
    for i in range(n):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        color = [0.5, 1.0, 0, 1.]
        # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(0, 0, 0)
        height=100
        glutWireCone(50, height, 20, 10)
        glPopMatrix()
        glPushMatrix()
        color = [1.0, 0.5, 0., 0.5]
        # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(0, 0, height * (1 - i / n))
        r=50
        glutWireSphere(r, 20, 10)
        glPopMatrix()
        glPushMatrix()
        color = [1., 1., 1., 1]
        # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(0, 0, height)
        glutWireCube(2 * r / 1.8)
        glPopMatrix()

        glutSwapBuffers()
        sleep(0.1)
    sleep(1)
def drawTorusCube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    # color = [1.0, 0.5, 0., 0.5]
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, 0)
    glutWireTorus(20, 30, 30, 30)
    glPopMatrix()
    glPushMatrix()
    # color = [1., 1., 1., 1]
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, 0)
    glutWireCube(100)
    glPopMatrix()

    glutSwapBuffers()
    sleep(2)
def moveTorusCube():
    n=10
    koef=1.3 - 1
    for i in range (n):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslate(0, 0, 0)
        glScalef(1 + koef * (i/n), 1 + koef * (i/n), 1 + koef * (i / n))
        glutWireTorus(20, 30, 30, 30)
        glPopMatrix()
        glPushMatrix()
        glTranslate(0, 0, 0)
        glutWireCube(100)
        glPopMatrix()

        glutSwapBuffers()
        sleep(0.1)
    sleep(1)
def draw():
    color = [1., 1., 1., 1]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    drawTorusCube()
    moveTorusCube()

    drawConeSphereCube()
    moveConeSphereCube()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Task 1")
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glutDisplayFunc(draw)
glMatrixMode(GL_PROJECTION)
# gluPerspective(90., 1, 1., 500.)
s=250
glOrtho (-s, s,-s, s,-s, 2*s)
# glRotate(30, 1, 1, 1)

glMatrixMode(GL_MODELVIEW)
gluLookAt(110, 90, 100,0, 0, 0,0, 0, 1)
glPushMatrix()
glutMainLoop()
