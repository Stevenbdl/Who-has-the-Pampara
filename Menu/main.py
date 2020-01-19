import pygame, sys, time


pygame.init()#Init pygame components

font = pygame.font.SysFont('arial', 50, bold=20)#Style for title main menu
fontStart = pygame.font.SysFont('arial', 30, italic=20)
W, H = 1000, 500#Window dimensions

class Menu:

    def __init__(self):
        self.title = font.render('¿Who has The Pampara?', 1, (217, 0, 0))#Game's title
        self.start = fontStart.render('press SPACE for start the game', 1, (0,0,0))#Start instruction
        self.running = True
    
    def run(self):
        screen = pygame.display.set_mode((W, H))#Window
        start = time.time()#Start time for get seconds
        while self.running:
            end = time.time()#End time for get seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()#Cerrar la ventana

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:#IF SPACE KEY IS PRESSED START THE GAME
                        self.running = False

            #Change color each two seconds
            if int(end-start) % 2 == 0:
                self.title = font.render('¿Who has The Pampara?', 1, (0, 54, 255))
            else:
                self.title = font.render('¿Who has The Pampara?', 1, (217, 0, 0))



            screen.fill((148,253,255))#Background
            screen.blit(self.title, (150, 50))#Title
            screen.blit(self.start, (250, 450))#Start title
            pygame.draw.rect(screen, (217, 0, 0), [200, 200, 200, 200])#Red rect
            pygame.draw.rect(screen, (0, 54, 255), [550, 200, 200, 200])#Blue rect
            pygame.display.update()

    