import numpy
import math
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
# import PIL
from PIL import Image
# import PIL.Image
# import stb_image`
def draw_cube(size):
    vertices = [
        [size/2, size/2, -size/2],
        [size/2, -size/2, -size/2],
        [-size/2, -size/2, -size/2],
        [-size/2, size/2, -size/2],
        [size/2, size/2, size/2],
        [size/2, -size/2, size/2],
        [-size/2, -size/2, size/2],
        [-size/2, size/2, size/2],
    ]
    # edges = [
    #     (0, 1), (1, 2), (2, 3), (3, 0),
    #     (4, 5), (5, 6), (6, 7), (7, 4),
    #     (0, 4), (1, 5), (2, 6), (3, 7)
    # ]
    faces = [
        (0, 1, 2, 3),
        (3, 2, 6, 7),
        (7, 6, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 6, 2),
        (4, 0, 3, 7)
    ]
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    # glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glVertex3fv(vertices[vertex])
    # glEnd()
    
    # texture_points = [
    #     [0, 0], [1, 0], [1, 1], [0, 1]
    # ]
    # index_points = [[0, 3, 2, 1]]
    # glVertexPointer(3, GL_FLOAT, 0, vertices)
    # glTexCoordPointer(2, GL_FLOAT, 0, texture_points)
    # glDrawElements(GL_QUADS, 4, GL_UNSIGNED_BYTE, index_points)

def load_texture(texture_file):
    texture_surface = Image.open(texture_file)
    texture_data = texture_surface.convert("RGBA").tobytes()
    
    width, height = texture_surface.size
    texture_id = glGenTextures(1)
    
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id
class Lab2:
    def __init__(self):
        self.texture_id = 0
        self.angle = 0
        self.light_pos_y = 5
        self.light_pos_x = 1
        self.index = 0
        self.brightness = 1
        self.change_angle = False
        self.colors = [
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 0.0],
        [0.55, 0.0, 1.0]
        ]
    def lightning_init(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        self.lightning_set_params()
    def calculate_angle(self):
        gluLookAt(math.cos(self.angle) * 4, math.sin(self.angle) * 4, 0, 0, 0,
        0, 0, 0, 1)
    def lightning_set_params(self):
        glLightfv(GL_LIGHT0, GL_POSITION, [self.light_pos_x, self.light_pos_y,
        10, 2])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [self.colors[self.index][0] +
        self.brightness - 1,
        self.colors[self.index][1] + self.brightness - 1,
        self.colors[self.index][2] + self.brightness - 1,
        self.brightness])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [self.colors[self.index][0] +
        self.brightness - 1,
        self.colors[self.index][1] + self.brightness - 1,
        self.colors[self.index][2] + self.brightness - 1,
        self.brightness])
    def read_texture(self, filename):
        img = Image.open(filename)
        img_data = numpy.array(list(img.getdata())).astype(numpy.int8)
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0] , img.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture_id
    def run_scene(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 800)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("lab2")
        self.texture_id = self.read_texture('2024-09-19_22-52.png')
        glutDisplayFunc(self.draw)
        glutSpecialFunc(self.special)
        self.lightning_init()
        glMatrixMode(GL_PROJECTION)
        # gluPerspective(90, 1, 1, 40)
        glOrtho (-5.0, 3.0,-3.0, 5.0,-5.0, 7.0)
        glRotate(30, 1, 1, 1)

        glMatrixMode(GL_MODELVIEW)
        glutMainLoop()
    def special(self, key, x, y):
        if key == GLUT_KEY_DOWN:
            self.light_pos_y -= 5
        if key == GLUT_KEY_UP:
            self.light_pos_y += 5
        if key == GLUT_KEY_LEFT:
            self.light_pos_x -= 5
        if key == GLUT_KEY_RIGHT:
            self.light_pos_x += 5
        if key == GLUT_KEY_PAGE_UP:
            if self.index < (len(self.colors) - 1):
                self.index += 1
            else:
                self.index = 0
        if key == GLUT_KEY_PAGE_DOWN:
            if self.index > 0:
                self.index -= 1
            else:
                self.index = len(self.colors) - 1
        if key == GLUT_KEY_HOME:
            self.brightness += 0.1
        if key == GLUT_KEY_END:
            self.brightness -= 0.1
    
    def draw(self):
        common_size = 2
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        self.angle = self.angle + 0.04 if self.change_angle else 0
        self.lightning_set_params()
        # textured cube
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        self.calculate_angle()

        glMaterialfv(GL_FRONT, GL_SPECULAR, [0, 0, 0, 0])
        glMaterialfv(GL_FRONT, GL_SHININESS, 0)
        glScalef(0.5, 0.5, 0.5)
        glTranslate(common_size * -2, common_size * -1.2, common_size * 0.4)
        q = gluNewQuadric()
        gluQuadricTexture(q, GLU_LINE)
        gluSphere(q, common_size * 1, 32, 32)

        # load_texture('2024-09-19_20-57.png')
        # self.read_texture('2024-09-19_21-39.png')
        # draw_cube(0.7)
        # glutSolidCube(common_size * 0.7)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        # polished torus
        glPushMatrix()
        self.calculate_angle()
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1., 1., 1, 1])
        glMaterialfv(GL_FRONT, GL_SHININESS, 128)
        glScalef(0.3, 0.3, 0.3)
        glTranslate(common_size * -2, common_size * -2, common_size * -2)
        glutSolidTorus(common_size * 1, common_size * 2, 25, 20)
        glPopMatrix()
        # matte sphere
        glPushMatrix()
        self.calculate_angle()
        glScalef(0.5, 0.5, 0.5)
        glTranslate(common_size * 2, common_size * 1, common_size * 0.7)
        glMaterialfv(GL_FRONT, GL_SPECULAR, [0, 0, 0, 0])
        glMaterialfv(GL_FRONT, GL_SHININESS, 0)
        glutSolidSphere(common_size * 0.5, 25, 25)
        glPopMatrix()
        # semi transparent cone
        glPushMatrix()
        self.calculate_angle()
        glScalef(0.5, 0.5, 0.5)
        glTranslatef(common_size * 1.2, common_size * 0.5, common_size * -1.2)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
        glutSolidCone(common_size * 0.4, common_size * 1, 60, 60)
        glDisable(GL_BLEND)
        glPopMatrix()
        glutSwapBuffers()
        glutPostRedisplay()

test = Lab2()
test.run_scene()
