from OpenGL.GL import *
from OpenGL.GLU import *

import random
import pygame
import os

from pygame.locals import *
from constants import *
from MeshRenderer import CubeMesh, ChairMesh

os.environ["SDL_VIDEO_CENTERED"]='1'


def random_color():
    x = random.randint(0, 255) / 255
    y = random.randint(0, 255) / 255
    z = random.randint(0, 255) / 255
    color = (x, y, z)
    return color

colors_list= []

for n in range(len(chair_faces_vector4)):
    colors_list.append(random_color())


def main():
    pygame.init()
    display = (1000, 1080)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)
    glRotatef(-90, 2, 0, 0)


main()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glRotatef(4, 3, -10, -45)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    ChairMesh()
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
quit()
