from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0.627, 0.322, 0.176,1)
    glClear(GL_COLOR_BUFFER_BIT)
    # glOrtho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

x = 0
angle=0
f=True
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global f
    glMatrixMode(GL_MODELVIEW)

    # ROAD
    glLoadIdentity()
    glColor3f(.1, .1, .1)
    glTranslate(0, -1.80, 0)
    glScale(100, .5, 10)
    glutSolidCube(1)

    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(0, -3, -2)
    glScale(.7, .001, .2)
    glutSolidCube(7)

    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(10, -3, -2)
    glScale(.7, .001, .2)
    glutSolidCube(7)

    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(-10, -3, -2)
    glScale(.7, .001, .2)
    glutSolidCube(7)

    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(-20, -3, -2)
    glScale(.7, .001, .2)
    glutSolidCube(7)



    #UPPER_CUBE
    glLoadIdentity()
    glColor3f(1,0,0)
    glTranslate(x,0,0)
    glScale(1, .25, .5)
    glutWireCube(5)

    #LOWER_CUBE
    glLoadIdentity()
    glTranslate(x,.25*5,0)
    glScale(.5,.25,.5)
    glutWireCube(5)


    #TORUS_1
    glLoadIdentity()
    glColor3f(0,0,1)
    glTranslate(x+2.5,-2.5*.25,2.5*.5)
    glRotate(angle,0,0,1)
    glutWireTorus(.125,.5,12,8)

    #TORUS_2
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glTranslate(x+2.5,-2.5*.25,-2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)

    #TORUS_3
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glTranslate(x-2.5,-2.5*.25,2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)

    #TORUS_4
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glTranslate(x-2.5,-2.5*.25,-2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(.125, .5, 12, 8)

    # SPHERE_1
    glColor(1, 1, 0)
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glTranslate(2.2, -.3, .4)
    glScale(.25, 1, 1)
    glutSolidSphere(.3, 20, 20)
    # SPHERE_2
    glLoadIdentity()
    glTranslate(x, 0, 0)
    glTranslate(2.2, -.3, -.4)
    glScale(.25, 1, 1)
    glutSolidSphere(.3, 20, 20)

    if x > 5:
      f = False

    if x < -10:
        f = True

    if f:
        x+=.001
        angle-=1
    else:
        x-=.001
        angle+=1


    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Moving Car")
glutInitWindowSize(2000, 2000)  # Set the window's initial width & height
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()