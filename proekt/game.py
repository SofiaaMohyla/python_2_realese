import pygame
import random

from random import *
from Um_yum import Um_yum
from file1 import read_data, write_data
from Сandies import Сandies
settings={}
def game():
    global settings
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((700,500))
    fps = pygame.time.Clock()

    backround = pygame.transform.scale(
        pygame.image.load("kartunka/fon.jpg"),(700,500)
    )
    settings=read_data()
    points = settings["money"]

    um_yum = Um_yum(280,360,100,100, "kartunka/player.png",10)

    candies1 = []
    candies1.append(Сandies(randint(0, 450),randint(-500,0),100,50,"kartunka/candies.png",5))
    candies1.append(Сandies(randint(0, 450),randint(-500,0),100,50,"kartunka/candies.png",5))
    candies1.append(Сandies(randint(0, 450),randint(-500,0),100,50,"kartunka/candies.png",5))
    candies1.append(Сandies(randint(0, 450),randint(-500,0),100,50,"kartunka/candies.png",5))


    font = pygame.font.Font(None, 36)

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        text_surface = font.render("Рахунок :", True, (0, 0, 0))

        text_surface1 = font.render(str(points), True, (0, 0, 0))
        window.blit(text_surface, (20, 20))
        window.blit(text_surface1, (140, 20))
        pygame.display.flip()
        fps.tick(60)


        window.blit(backround, (0, 0))
        um_yum.move()
        um_yum.draw(window)

        for candies in candies1:
            candies.draw(window)
            candies.move()



            if um_yum.hitbox.colliderect(candies.hitbox):
                candies.hitbox.x = randint(0, 450)
                candies.hitbox.y = randint(-500,0)
                points+=1
                settings = read_data()
                settings["money"]=points
                write_data(settings)
                pygame.display.flip()
                break



        pygame.display.flip()
        fps.tick(60)