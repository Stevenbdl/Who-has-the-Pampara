import pygame, sys

pygame.init()#init pygame components

W, H = 1000, 500#Window dimensions

fontWin = pygame.font.SysFont('arial', 50, bold=20)
font = pygame.font.SysFont('arial', 30, italic=20)


def getWinner():

    f = open('winner.txt', 'r')
    return f.readline()

def set_winner(player):
    f = open('winner.txt', 'w')
    f.write(str(player))
    f.close()


class Winner:

    def __init__(self, winner):
        self.winner = winner
        self.restart = font.render('press SPACE for restart the game', 1, (0,0,0))#restart instruction
        self.running = True

        if winner == "P1":
            self.winnertext = fontWin.render('Winner is ' + winner, 1, (217, 0, 0))
        elif winner == "P2":
            self.winnertext = fontWin.render('Winner is ' + winner, 1, (0, 54, 255))

    def run(self):
        screen = pygame.display.set_mode((W, H))

        #MAIN LOOP
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = False
            
        
            screen.fill((148,253,255))#BG
            if self.winner == "P1":
                screen.blit(self.winnertext, (330, 50))
                pygame.draw.rect(screen, (217, 0, 0), [400, 150, 200, 200])#Red rect
            elif self.winner == "P2":
                screen.blit(self.winnertext, (330, 50))
                pygame.draw.rect(screen, (0, 54, 255), [400, 150, 200, 200])#Blue rect
            screen.blit(self.restart, (300, 450))#restart title
            pygame.display.update()
        
