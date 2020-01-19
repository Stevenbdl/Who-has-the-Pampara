import pygame



pygame.init()#Init pygame components

#Player 1
class Player1:
    

    def __init__(self, ):
        """
        Class for player 1
        """
        self.player = pygame.Rect(100, 420, 50, 50)
        self.color = pygame.Color(217, 0, 0)#Blue color
        self.keys = [False, False]# LEFT - RIGHT 
        self.jump = False#UP(JUMP)
        self.isDown = False
        self.gravity = 200
        self.forceJump = 0
        self.force = 5
        self.currentPlatform = 420#Platform for the player(floor)
        
        


    def draw(self, screen):
        """
        Draw player
        """

        pygame.draw.rect(screen, self.color, self.player)

    def capKeys(self, event):
        """
        event -> pygame.event
        """

        if event.type == pygame.KEYDOWN:
            #Player 1
            if event.key == pygame.K_a:#LEFT
                 self.keys[0] = True

            if event.key == pygame.K_d:#RIGHT
                self.keys[1] = True
                
            if event.key == pygame.K_w:#UP(JUMP)
                self.jump = True

        elif event.type == pygame.KEYUP:
            #Player 1
            if event.key == pygame.K_a:#LEFT
                self.keys[0] = False

            if event.key == pygame.K_d:#RIGHT
                self.keys[1] = False
                
            
            
    def move(self):
        """
        Move the player
        """
        
        if self.keys[0]:#Move left
            self.player.x -= 5
            #limit left
            if self.player.x < 1:
                self.player.x = 0
        
        if self.keys[1]:#Move right
            self.player.x += 5
            #limit right
            if self.player.x > 950:
                self.player.x = 950

        #Jump
        if self.jump:
            #print("Current platform", self.currentPlatform)
            #used for jumping if the player is not down to the floor
            if self.forceJump < self.gravity and not self.isDown:
                self.player.y -= self.force
                self.forceJump += self.force
                #if collide with the top
                if self.player.y < 1:
                    self.player.y = 0
            else:
                #self.isDown = False
                self.jump = False
        else:
            #Down player to the floor
            if self.player.y < 420:
                self.player.y += self.force
            else:
                self.forceJump = 0
                self.currentPlatform = 420

            if (self.player.y - 5) > self.currentPlatform:
                self.isDown = True
            elif (self.player.y - 5) == self.currentPlatform or self.player.y == 420:
                self.isDown = False

        #print(self.forceJump, self.gravity)
        #print(self.player.y, self.currentPlatform)
            

        
            
            
                
        
        #print(self.currentPlatform)

                
    def aboveOfThePlatform(self):
        """
        put the player above of the platform if this collide with any platform
        """
        platforms = [[250, 200], [550, 200], [100, 340], [700, 340]]    
        for p in platforms:
            
            if self.player.colliderect(pygame.Rect(p[0], p[1], 200, 20)):
                if self.player.y < p[1]:
                    #for platform left-down
                    if platforms.index(p) == 2:
                            self.forceJump = 0
                            self.player.y = 290
                            self.currentPlatform = 290
                         

                    #for platform right-down
                    if platforms.index(p) == 3:
                        self.player.y = 290
                        self.currentPlatform = 290
                        self.forceJump = 0
                      

                    #for platform left-up
                    if platforms.index(p) == 0:
                        self.player.y = 150
                        self.currentPlatform = 150
                        self.forceJump = 0
        

                        #for platform right-up
                    if platforms.index(p) == 1:
                        self.player.y = 150
                        self.currentPlatform = 150
                        self.forceJump = 0
                            

            
            
    
    def belowOfThePlatform(self):
        """
        If the player is below of the platform and jump then can't jump for up 
        """
        #If the player is below of platform left-down
        if self.player.x in range(50, 300) and self.player.y > 290:
            #if the player jump below platform left-down reduce gravity
            if self.jump:
                self.gravity = 60
            else:
                self.gravity = 200
        elif self.player.x in range(200, 450) and self.player.y < 220:
            #if the player jump below platform left-up reduce gravity
            if self.jump and self.player.y > 200:
                self.gravity = 10
            else:
                self.gravity = 200
        
        #If the player is below of platform right-down
        if self.player.x in range(650, 900) and self.player.y > 290:
            #if the player jump below platform left-down reduce gravity
            if self.jump:
                self.gravity = 60
            else:
                self.gravity = 200
        elif self.player.x in range(500, 750) and self.player.y < 220:
            #if the player jump below platform right-up
            if self.jump and self.player.y > 200:
                self.gravity = 10
            else:
                self.gravity = 200


#Player 2
class Player2:
    

    def __init__(self, ):
        """
        Class for Player 2
        """
        self.player = pygame.Rect(600, 420, 50, 50)
        self.color = pygame.Color(0, 54, 255)#Blue color
        self.keys = [False, False]# LEFT - RIGHT 
        self.jump = False#UP(JUMP)
        self.isDown = False
        self.gravity = 200
        self.forceJump = 0
        self.force = 5
        self.currentPlatform = 420#Platform for the player(floor)

        

    def draw(self, screen):
        """
        Draw player
        """

        pygame.draw.rect(screen, self.color, self.player)

    def capKeys(self, event):
        """
        event -> pygame.event
        """

        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_LEFT:#LEFT
                 self.keys[0] = True

            if event.key == pygame.K_RIGHT:#RIGHT
                self.keys[1] = True
                
            if event.key == pygame.K_UP:#UP(JUMP)
                self.jump = True
                
                

        elif event.type == pygame.KEYUP:
        
            if event.key == pygame.K_LEFT:#LEFT
                self.keys[0] = False

            if event.key == pygame.K_RIGHT:#RIGHT
                self.keys[1] = False

    def aboveOfThePlatform(self):
        """
        put the player above of the platform if this collide with any platform
        """
        platforms = [[250, 200], [550, 200], [100, 340], [700, 340]]    
        for p in platforms:
            
            if self.player.colliderect(pygame.Rect(p[0], p[1], 200, 20)):
                    if self.player.y < p[1]:
                        #for platform left-down
                        if platforms.index(p) == 2:
                            self.forceJump = 0
                            self.player.y = 290
                            self.currentPlatform = 290
                         

                        #for platform right-down
                        if platforms.index(p) == 3:
                            self.player.y = 290
                            self.currentPlatform = 290
                            self.forceJump = 0
                      

                        #for platform left-up
                        if platforms.index(p) == 0:
                            self.player.y = 150
                            self.currentPlatform = 150
                            self.forceJump = 0
        

                        #for platform right-up
                        if platforms.index(p) == 1:
                            self.player.y = 150
                            self.currentPlatform = 150
                            self.forceJump = 0
                            
        
            
            
    
    def belowOfThePlatform(self):
        """
        If the player is below of the platform and jump then can't jump for up 
        """
        #If the player is below of platform left-down
        if self.player.x in range(50, 300) and self.player.y > 290:
            #if the player jump below platform left-down reduce gravity
            if self.jump:
                self.gravity = 60
            else:
                self.gravity = 200
        elif self.player.x in range(200, 450) and self.player.y < 220:
            #if the player jump below platform left-up reduce gravity
            if self.jump and self.player.y > 200:
                self.gravity = 10
            else:
                self.gravity = 200
        
        #If the player is below of platform right-down
        if self.player.x in range(650, 900) and self.player.y > 290:
            #if the player jump below platform left-down reduce gravity
            if self.jump:
                self.gravity = 60
            else:
                self.gravity = 200
        elif self.player.x in range(500, 750) and self.player.y < 220:
            #if the player jump below platform right-up
            if self.jump and self.player.y > 200:
                self.gravity = 10
            else:
                self.gravity = 200
        
        
    
            
        

    def move(self):
        """
        Move the player
        """
        
        if self.keys[0]:#Move left
            self.player.x -= 5
            #limit left
            if self.player.x < 1:
                self.player.x = 0
        
        if self.keys[1]:#Move right
            self.player.x += 5
            #limit right
            if self.player.x > 950:
                self.player.x = 950

        #Jump
        if self.jump:
            #print("Current platform", self.currentPlatform)
            #used for jumping if the player is not down to the floor
            if self.forceJump < self.gravity and not self.isDown:
                self.player.y -= self.force
                self.forceJump += self.force
                #if collide with the top
                if self.player.y < 1:
                    self.player.y = 0
            else:
                #self.isDown = False
                self.jump = False
        else:
            #Down player to the floor
            if self.player.y < 420:
                self.player.y += self.force
            else:
                self.forceJump = 0
                self.currentPlatform = 420

            if (self.player.y - 5) > self.currentPlatform:
                self.isDown = True
            elif (self.player.y - 5) == self.currentPlatform or self.player.y == 420:
                self.isDown = False

        #print(self.forceJump, self.gravity)
        #print(self.player.y, self.currentPlatform)
            

        
            
            
                
        
        #print(self.currentPlatform)
