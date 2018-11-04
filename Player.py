import pygame
from utilities import load_png

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #pygame.display.init()
        self.image, self.rect = load_png('playerr.png')

        self.isMoving = False
        self.key = pygame.K_m #can't create an empty variable or something smh

        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = 0
        self.posX = 100
        self.posY = 100
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 500

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update_bounds(self):
        self.rect.x = self.posX - self.image.get_width() / 2
        self.rect.y = self.posY - self.image.get_height() / 2

    def input(self, up, down, left, right):
        lastangle = 0
        if(up):
            self.velY = self.speed
            self.image, self.rect = load_png('playert.png')
        elif(down):
            self.velY = -self.speed
            self.image, self.rect = load_png('playerd.png')
        else:
            self.velY = 0
        if(left):
            self.velX = self.speed
            self.image, self.rect = load_png('playerl.png')
        elif(right):
            self.velX = -self.speed
            self.image, self.rect = load_png('playerr.png')
        else:
            self.velX = 0

        if(up and right):
            self.image, self.rect = load_png('playertr.png')
        elif(up and left):
            self.image, self.rect = load_png('playertl.png')
        elif(down and left):
            self.image, self.rect = load_png('playerdl.png')
        elif(down and right):
            self.image, self.rect = load_png('playerdr.png')
            

    def calc_pos(self, deltatime):
        if(self.rect.right >= self.area.width or self.rect.left <= 0):
            print("out on sides")
            self.velX = 0
        if(self.rect.bottom >= self.area.height or self.rect.top <= 0):
            print("out on top or bottom")
            self.velY = 0

        self.velX = self.velX + self.accX * deltatime
        self.velY = self.velY + self.accY * deltatime

        self.posX = self.posX + self.velX * deltatime
        self.posY = self.posY + self.velY * deltatime

        self.update_bounds()

    def draw(self, screen): 
        screen.blit(self.image, (self.posX - self.image.get_width() / 2, self.posY - self.image.get_height() / 2))
        pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), self.rect)

        

