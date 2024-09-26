from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from time import sleep
# def iterate():
#     glViewport(0, 0, 800, 800)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
def drawConeSphere():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [0., 0., 0., 0.]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(10, 10, 0)
    glutWireCone(50, 250, 20, 10)
    glPopMatrix()
    glPushMatrix()
    color = [1.0, 0.5, 0., 0.5]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(20, 20, 0)
    glutWireSphere(50, 20, 10)
    glPopMatrix()
    glutSwapBuffers()
    sleep(3)
    return
def moveConeSphere():
    for i in range(1000):
        temp = i * 5 / 1000
        tempCone = 10 + temp
        tempCyl = 20 - temp
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        color = [0., 0., 0., 0.]
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(tempCone, tempCone, 0)
        glutWireCone(50, 250, 20, 10)
        glPopMatrix()
        glPushMatrix()
        color = [1.0, 0.5, 0., 0.5]
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(tempCyl, tempCyl, 0)
        glutWireSphere(50, 20, 10)
        glPopMatrix()
        glutSwapBuffers()
        sleep(0.001)
    sleep(3)
    return
def drawTorCylinder():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0, 0.5, 0., 0.5]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, 0)
    glutWireTorus(20, 50, 30, 30)
    glPopMatrix()
    glPushMatrix()
    color = [0., 0., 0., 0.]
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
    glTranslate(0, 0, 0)
    glutWireCylinder(30, 80, 20, 10)
    glPopMatrix()
    glutSwapBuffers()
    sleep(3)
    return
def moveTorCylinder():
    for i in range (400):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        color = [1.0, 0.5, 0., 0.5]
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(0, 0, 0)
        glScalef(1 + 0.5 * (i/400), 1 + 0.5 * (i/400), 1 + 0.5 * (i / 400))
        glutWireTorus(20, 50, 30, 30)
        glPopMatrix()
        glPushMatrix()
        color = [0., 0., 0., 0.]
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, color)
        glTranslate(0, 0, 0)
        glRotate(0 + 0.9 * i/4, 0, 0 , 1)
        glutWireCylinder(30, 80, 20, 10)
        glPopMatrix()
        glutSwapBuffers()
        sleep(0.001)
    sleep(3)
    return
def draw():
    drawConeSphere()
    moveConeSphere()
    drawTorCylinder()
    moveTorCylinder()
    return
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Task 1")
glClearColor(1.0, 1.0, 1.0, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glutDisplayFunc(draw)
glMatrixMode(GL_PROJECTION)
gluPerspective(80., 1, 1., 500.)
glMatrixMode(GL_MODELVIEW)
gluLookAt(250, 0, 100,50, 0, 100,0, 0, 1)
glPushMatrix()
glutMainLoop()
