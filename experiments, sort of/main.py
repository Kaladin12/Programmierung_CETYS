import pygame
import sys
from time import sleep
from grid import Grid

grid=[[1]*8 for n in range(8)]

width=500
height=400
orange=(255,69,0)

pygame.init()
surface=pygame.display.set_mode((600,600))
pygame.display.set_caption('Hello There')
surface.fill((255,69,0))
pygame.display.update()
salir=True
grid=Grid()

while salir:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            salir=False
            break

    surface.fill((0,0,0))
    grid.draw(surface)
    pygame.display.flip()