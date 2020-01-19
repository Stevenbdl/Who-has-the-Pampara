import pygame


pygame.init()#init pygame components


class Platform:

    """
    Platform for the game 
    """

    def __init__(self):
        self.floor = pygame.Rect(0, 470, 1000, 30)
        self.plat = [[250, 200], [550, 200], [100, 340], [700, 340]]


    def draw(self, screen):
        """
        Draw floor and platform
        """
        #Draw floor
        pygame.draw.rect(screen, (0,0,0), self.floor)


        #Draw plat
        for p in self.plat:
            pygame.draw.rect(screen, (0,0,0), [p[0], p[1], 200, 20])