import pygame
import random

class Сandies:
    def __init__(self,x,y,w,h,img,speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed


    def draw(self, window):
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))



    def move(self):
        self.hitbox.y += self.speed
        if self.hitbox.y > 600:
            self.hitbox.y = 0
            self.hitbox.x = random.randint(0, 680)

