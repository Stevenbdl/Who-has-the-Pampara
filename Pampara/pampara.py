import pygame 


pygame.init()#Init pygame components


class Pampara:
    """
    Arrow fixed in player that got the pampara
    """


    def __init__(self, x, y):
        self.arrow = pygame.image.load('arrow2.png')#Arrow
        self.sizeImage = self.arrow.get_size()#Size of arrow image
        self.rect = pygame.Rect(x-142, y-115, self.sizeImage[0], self.sizeImage[1])
        self.whoHasPampara = "P1"#The player 1 start with the pampara

    def draw(self, screen):
        """
        Draw arrow image
        """
        screen.blit(self.arrow, self.rect)

    def setPosition(self, x, y):
        """
        Player is position that has the current pampara
        """
        self.rect.x = x-142
        self.rect.y = y-115

    def setHasThePampara(self):
        """
        Set who has current pampara
        """
        #If the player 1 has the pampara and they collide in one point the pampara is for player 2
        if self.whoHasPampara == "P1":
            self.whoHasPampara = "P2"
        else:#If the player 2 has the pampara and they collide in one point the pampara is for player 1
            self.whoHasPampara = "P1"

    def getHasPampara(self):
        """
        Return the current player with the pampara
        """
        return self.whoHasPampara