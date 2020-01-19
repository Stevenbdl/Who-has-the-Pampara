import pygame
import sys, time
from Platform.platform import Platform
from Player.player import Player1, Player2
from Pampara.pampara import Pampara
from Menu.main import Menu
from Winner.winner import Winner, getWinner, set_winner

#@Author: Stevenbdl
pygame.init()#Start pygame components

W, H = 1000, 500#Window dimensions

font = pygame.font.SysFont('arial', 50, italic=10)#Font time 


pygame.display.set_caption("¿Who has the Pampara?")#Game's title

def main():
    
    screen = pygame.display.set_mode((W, H))#Window
    bg = pygame.Color(148,253,255)#Background
    platform = Platform()
    p1 = Player1()#Player 1
    p2 = Player2()# Player 2

    pampara = Pampara(p1.player.x, p1.player.y)#Arrow 

    fps = pygame.time.Clock()#FPS

    timelimit = 30#Time limit for the game over
    color_for_time = (217, 0, 0)#The initial color for the time is red because first the pampara is for player 1
    start = time.time()#Start time for get seconds

    running = True
    #MAIN LOOP
    while running:
        end = time.time()#End time for get seconds
        if pampara.getHasPampara() == "P1":#If the pampara is of player 1, color for time is red (217,0,0)
            color_for_time = (217, 0, 0)#Red color
        elif pampara.getHasPampara() == "P2":# if the pampara is of player 2, color for time is blue (0, 54, 255)
            color_for_time = (0, 54, 255)#Blue color

        clock = font.render(str(int(timelimit-(end-start))), 1, color_for_time)
        #print(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

            p1.capKeys(event)#Capture keys for player 1
            p2.capKeys(event)#Capture keys for player 2

            #Collide point with the player
        if int(end-start) == 30:
            set_winner(pampara.getHasPampara())
            running = False
            
            
        p1.move()#Move player 1
        p2.move()#Move player 2

        #P1 handler platform
        p1.aboveOfThePlatform()
        p1.belowOfThePlatform()

        #P2 handler platform 
        p2.aboveOfThePlatform()
        p2.belowOfThePlatform()

        #**********************************************Collisions *********************************************
        if p1.player.collidepoint((p2.player.x, p2.player.y)):
            pampara.setHasThePampara()

        #********************************** Pampara position ***************************************************
        if pampara.getHasPampara() == "P1":
            pampara.setPosition(p1.player.x, p1.player.y)
        else:
            pampara.setPosition(p2.player.x, p2.player.y)


        screen.fill(bg)
        platform.draw(screen)#Draw platform 
        p1.draw(screen)#Draw player 1
        p2.draw(screen)#Draw player 2
        pampara.draw(screen)#Draw arrow
        screen.blit(clock, (500, 0))#Draw clock
        pygame.display.update()
        fps.tick(100)#FPS for the game


def start():
    main_menu = Menu()
    main_menu.run()
    main()

def restart():
    main()
    winner = Winner(getWinner())
    winner.run()
    if winner.running == False:
        restart()

if __name__ == "__main__":
   start()
   winner = Winner(getWinner())
   winner.run()
   if winner.running == False:
       restart()