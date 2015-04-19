

from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from Image import *
import math
import sys

quadratic = 0

#Global vars
interval = 200
translate_x = 0
translate_y = 0
translate_z = 0
angle_x = 0
angle_y = 0
angle_z = 0
texture_num = 0

def init():
	global quadratice
	
	LoadTextures(3)

	quadratic = gluNewQuadric()
	gluQuadricNormals(quadratic, GLU_SMOOTH)                
	gluQuadricTexture(quadratic, GL_TRUE)                  

	glEnable(GL_TEXTURE_2D)
	glClearColor(135.0,206.0,255.0,1.0)
	glClearDepth(1.0)                       
	glDepthFunc(GL_LESS)                    
	glEnable(GL_DEPTH_TEST)                 
	glShadeModel(GL_SMOOTH)
	glShadeModel(GL_FLAT)
	glOrtho(-100.0,100.0, -100.0,100.0, -10.0,10.0)
	#glEnable(GL_LIGHTING)
	glLightfv(GL_LIGHT0, GL_AMBIENT, (0.15,0.15,0.15,0.1))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0,1.0,1.0,1.0))
	glLightfv(GL_LIGHT0, GL_POSITION, (0.0,0.0,0.0,0.0))
	#glEnable(GL_LIGHT0)

def timer(val):
	return True

def CreateTexture(imagename, number):
    global textures

    image = open(imagename)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)

    glBindTexture(GL_TEXTURE_2D, int(textures[number]))   

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def CreateLinearFilteredTexture(imagename, number):
    global textures

    image = open(imagename)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)

    glBindTexture(GL_TEXTURE_2D, int(textures[number]))   
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

def CreateMipMappedTexture(imagename, number):
    global textures

    image = open(imagename)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)

    glBindTexture(GL_TEXTURE_2D, int(textures[number]))
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_NEAREST)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)
           
def LoadTextures(number):
    global texture_num, textures

    textures = glGenTextures(number)
    CreateTexture("Wall.jpg", 0)
##      CreateTexture("W.png", 1)
##      CreateTexture("myfire.jpg", 2)
    #CreateLinearFilteredTexture("mirrow2.bmp", 1)
    #CreateMipMappedTexture("BasketballColor.jpg", 2)

def keyboard(key, a, b):
    global translate_x, translate_y, translate_z, angle_x, angle_y, angle_z
    if key == chr(27): 
           sys.exit(0)
    elif key == 'a':
           translate_z = translate_z - 0.5
           glutPostRedisplay()
    elif key == 's':
           translate_x = translate_x + 0.5
           glutPostRedisplay()
    elif key == 'z':
           translate_z = translate_z + 0.5
           glutPostRedisplay()
    elif key == 'x':
           translate_x = translate_x - 0.5
           glutPostRedisplay()
    elif key == 'd':
           translate_y = translate_y - 0.5
           glutPostRedisplay()
    elif key == 'c':
           translate_y = translate_y + 0.5
           glutPostRedisplay()
    elif key == 'f':
            interval = interval - 40
            if interval < 10 :
                interval = 50
            glutPostRedisplay()
    elif key == 'v':
            interval = interval + 40
            glutPostRedisplay()
    elif key == 'q':
    		sys.exit()
    elif key == 'r':
        x_dir = -1*x_dir
        y_dir = -1*y_dir
        z_dir = -1*z_dir
        print(x_dir,y_dir,z_dir)



def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0,1.0,-1.0,1.0,1.5,10.0)
    
    glMatrixMode(GL_MODELVIEW)


def draw():
	global translate_x, translate_y, translate_z, angle_x, angle_y, angle_z, texture_num
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)	
	glLoadIdentity()
	gluLookAt(0.0,0.0,5.0, 0.0,0.0,0.0, 0.0,1.0,0.0)				#Functions to transform the camera	
	glTranslate(translate_x, translate_y, translate_z)
	glRotate(angle_x,1.0,0.0,0.0)
	glRotate(angle_y,0.0,1.0,0.0)
	glRotate(angle_z,0.0,0.0,1.0)


	glPushMatrix()
	#Mainspace. Let's just create a ground. That is all
	glBindTexture(GL_TEXTURE_2D, int(textures[texture_num]))

	glPushMatrix()
	#Place for the court
	glColor3f(139,90,0)
	glBegin(GL_QUADS)
	glTexCoord2f(0.0,0.0)
	glVertex3f(-4,-3,-1)
	glTexCoord2f(1.0,0.0)
	glVertex3f(4,-3,-1)
	glTexCoord2f(1.0,1.0)
	glVertex3f(4,-3,1)
	glTexCoord2f(0.0,1.0)
	glVertex3f(-4,-3,1)
	glEnd()
	#End of basketball court 
	glPopMatrix()

	glPushMatrix()
	#This place is the left post
	glColor(0,0,0)	
	glPushMatrix()
	#Just the pole
	glTranslate(-4,-1.3,0)
	glScale(0.1,4,0.1)
	glutSolidCube(1)
	#Ending the pole
	glPopMatrix()

	glPushMatrix()
	#Within the post pole, now to make the board
	glTranslate(-4,1,0)
	glScale(0.1,1,1)
	glutWireCube(1)
	
	glPushMatrix()
	#The hoop
	glTranslate(1.8,-0.44,0)
	glScale(5,0.5,0.5)
	glRotatef(90,1,0,0)
	glRotate(180,0,1,0)
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
	#Ending the hoop
	glPopMatrix()

	#Ending the board
	glPopMatrix()

	#End of the left post
	glPopMatrix()
	
	glPushMatrix()
	#This place is the right post
	glColor(0,0,0)	
	glPushMatrix()
	#Just the pole
	glTranslate(4,-1.3,0)
	glScale(0.1,4,0.1)
	glutSolidCube(1)
	#Ending the pole
	glPopMatrix()

	glPushMatrix()
	#Within the post pole, now to make the board
	glTranslate(4,1,0)
	glScale(0.1,1,1)
	glutWireCube(1)

	glPushMatrix()
	#The hoop
	glTranslate(1.8,-0.44,0)
	glScale(-5,0.5,0.5)
	glRotatef(270,1,0,0)
	glColor3f(1,1,1)
	glBegin(GL_LINE_LOOP)
	i = 0
	while i <= 300:
	    angle = 2 * math.pi * i / 300
	    a = -0.25*math.cos(angle)
	    b = 0.25*math.sin(angle)
	    glVertex2f(a,b)
	    i = i + 1
	glEnd()
	#Ending the hoop
	glPopMatrix()

	#Ending the board
	glPopMatrix()

	#End of the right post
	glPopMatrix()

	glPopMatrix()
	glFlush()



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
    #glutTimerFunc(interval, timer, 0)
    glutMainLoop()

velocity = input("Enter the inital velocity")
x_dir, y_dir, z_dir = input("Input x direction vector"), input("Input y direction vector"), input("Input z direction vector")
x_dir = x_dir/math.sqrt((x_dir*x_dir) + (y_dir*y_dir) + (z_dir*z_dir))
y_dir = y_dir/math.sqrt((x_dir*x_dir) + (y_dir*y_dir) + (z_dir*z_dir))
z_dir = z_dir/math.sqrt((x_dir*x_dir) + (y_dir*y_dir) + (z_dir*z_dir))
#x y z are now normalized

main()