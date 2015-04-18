from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import math
import sys

global x, y, z, t, interval, v, vx, vy, vz
x = 0.0
y = 0.0
z = 0.0
t = 0.0
gt = 0.098
interval = 200
stop = 1

def timer(val):
    global t,hit,interval, x, y, z ,vx ,vy ,vz, vyi, vxi, stop, gt
    if hit==1:
        vx = -vxi
    if y<-0.5 and stop == 1:
        vx=(vx/2)
        vz=(vz/2)
        vy = -(vy/2)
        if vy < 0.098:
            vx = 0
            vy = 0
            vz = 0
            gt = 0
        stop = 0
        print(vx,vy,vz)
    if y > -0.5:
        stop = 1
    x = x + (vx*(0.01))
    y = y + (vy*(0.01))
    z = z + (vz*(0.01))
    if x <= -1.9 and (z<0.5 and z>-0.5) and (y<1.5 and y>0.5):
        hit = hit + 1
    vy = vy - gt
    glutPostRedisplay()
    glutTimerFunc(interval, timer, 0)

def init():

    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
    glOrtho(-100.0,100.0, -100.0,100.0, -10.0,10.0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.15,0.15,0.15,0.1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0,1.0,1.0,1.0))
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0,0.0,0.0,0.0))
    glEnable(GL_LIGHT0)

def keyboard(key, a, b):
    global xframe, yframe, zframe, interval, vx, vy, vz
    if key == chr(27): 
           sys.exit(0)
    elif key == 'q':
           zframe = zframe - 0.5
           glutPostRedisplay()
    elif key == 'a':
           xframe = xframe + 0.5
           glutPostRedisplay()
    elif key == 'e':
           zframe = zframe + 0.5
           glutPostRedisplay()
    elif key == 'd':
           xframe = xframe - 0.5
           glutPostRedisplay()
    elif key == 's':
           yframe = yframe - 0.5
           glutPostRedisplay()
    elif key == 'w':
           yframe = yframe + 0.5
           glutPostRedisplay()
    elif key == 'i':
            interval = interval - 40
            if interval < 10 :
                interval = 50
            glutPostRedisplay()
    elif key == 'o':
            interval = interval + 40
            glutPostRedisplay()
    elif key == 'r':
        vx = -1*vx
        vy = -1*vy
        vz = -1*vz
        print(vx,vy,vz)

def draw():
    global hit,x,y,z,xframe,yframe,zframe
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glLoadIdentity()
    
    gluLookAt(0.0,0.0,5.0, 0.0,0.0,0.0, 0.0,1.0,0.0)
    glTranslate(xframe,yframe,zframe)
    glPushMatrix()
    
    glTranslate(-2.05,1,0)
    glScale(0.1,1,1)
    glutWireCube(2)
    
    glPushMatrix()
    glTranslate(0,-3,0)
    glColor3f(139,90,0)
    glBegin(GL_QUADS)
    glVertex3f(-4,-3,-1)
    glVertex3f(40,-3,-1)
    glVertex3f(40,-3,1)
    glVertex3f(-4,-3,1)
    #glVertex3f(4,0,1)
    #glVertex2f(0,0,1)
    glEnd()
    glColor3f(1,1,1)
    glTranslate(0,3,0)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0,-3.5,0)
    glScale(1,5,0.1)
    glutWireCube(1)
    glPopMatrix()



    glPushMatrix()
    glTranslate(1.8,-0.44,0)
    glScale(5,0.5,0.5)
    glRotatef(90,1,0,0)
    glColor3f(1,1,1)
    glBegin(GL_LINE_LOOP)
    i = 0
    while i <= 300:
        angle = 2 * math.pi * i / 300
        a = 0.25*math.cos(angle)
        b = 0.25*math.sin(angle)
        glVertex2f(a,b)
        i = i + 1
    glEnd()
    glColor3f(1,1,1)
    glPopMatrix()

    
    glScale(10,1,1)
    glTranslate(2,-1,0)
    glTranslatef(x,y,z)
    glutSolidSphere(0.1, 1000, 1000);
    glTranslatef(-x, -y, -z)

    glPopMatrix()
    glFlush()


def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0,1.0,-1.0,1.0,1.5,20.0)
    
    glMatrixMode(GL_MODELVIEW)
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Cube")
    init()
    glutDisplayFunc(draw)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(interval, timer, 0)
    glutMainLoop()
    
v = input("Initial velocity: ");
vx = input("Enter direction: ")
vy = input("Enter x-direction: ")
vz = input("Enter y-direction: ")
print('\nLeft: a\t\tRight: d\nZoom in: f\tZoom out: r\nUp: w\t\tDown: s\n')
mag = math.sqrt(((vx*vx) + (vy*vy) + (vz*vz)));
vx = v*(vx/mag)
vy = v*(vy/mag)
vz = v*(vz/mag)
vxi = vx
vyi = vy
t = (vyi/9.8)*2
ymax = (vyi*t*0.5)-((9.8*t*t)/8)
xmax = vx*t
zmax = vz*t
if xmax == 0:
    xmax = 1
if ymax == 0:
    ymax = 1
if zmax == 0:
    zmax = 1
hit = 0
xframe = 0
yframe = 0
zframe = 0

main()
