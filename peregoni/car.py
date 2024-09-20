import pygame


class Player:
    def __init__(self,x,y,w,h,img,speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w,h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.dir = "right"
        self.dir = "up"
        self.dir = "down"
        self.dir = "left"



    def draw(self,window):
        #pygame.draw.rect(window,(225,0,0),self.hitbox)
        window.blit(self.photo,(self.hitbox.x, self.hitbox.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.hitbox.x += self.speed*4
            self.dir = "right"
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed*4
            self.dir = "left"
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed*6
            self.dir = "up"
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed*5
            self.dir = "down"