import pygame

class Grid:
    def __init__(self):
        self.grid_lenis=[((0,200),(600,200)),
                         ((0,400),(600,400)),
                         ((200,0),(200,600)),
                         ((400,0),(400,600))]

    
    def draw(self, surface):
        for line in self.grid_lenis:
            pygame.draw.line(surface,(200,200,200),line[0],line[1],2)
        