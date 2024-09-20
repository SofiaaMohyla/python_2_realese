import pygame
import math
from pygame import *
import pygame.freetype
import json
def lvl3():
    def showEndWindow(window, message):
            clock = time.Clock()
            run = True
            font.init()
            text = font.Font(None, 170).render(message, True, (0, 255, 255))
            while run:
                # обробка подій
                for e in event.get():
                    if e.type == QUIT:
                        run = False
                        quit()
                #рендер
                window.blit(text, (100, 170))
                display.update()
                clock.tick()


    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, x, y, speed, size_w, size_h):
            self.x = x
            self.y = y
            self.speed = speed
            self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
            self.rect = self.player_image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def draw(self, screen):
            screen.blit(self.player_image, (self.rect.x, self.rect.y))

    class Gold(sprite.Sprite):
        def __init__(self, player_image, x, y, speed, size_w, size_h):
            self.x = x
            self.y = y
            self.speed = speed
            self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
            self.rect = self.player_image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def draw(self, screen):
            screen.blit(self.player_image, (self.rect.x, self.rect.y))

    class Player(GameSprite):
        def update(self):
            #moveSound = mixer.Sound('kick.ogg')
            keys = key.get_pressed()
            if keys[K_a]:
                self.rect.x -= self.speed
                #moveSound.play()
            if keys[K_d]:  
                self.rect.x += self.speed
                #moveSound.play()
            if keys[K_w]:
                self.rect.y -= self.speed
                #moveSound.play()
            if keys[K_s]:
                self.rect.y += self.speed
                #moveSound.play()


    class Enemy(GameSprite):
        def update(self):
            self.rect.x += self.speed
            if self.rect.x >= 110:
                self.speed *= -1
            if self.rect.x <= 650:
                self.speed *= -1
                
    class EnemyB(GameSprite):
        def update(self):
            self.rect.y += self.speed
            if self.rect.y >= 490:
                self.speed *= -1
            if self.rect.y <= 410:
                self.speed *= -1

    class Wall:
        def __init__(self, x, y, w, h, color):
            self.image = Surface((w, h))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    window = display.set_mode((900, 500))
    clock = time.Clock()
    timer = time.Clock()
    display.set_caption("LvL 3")
    background = transform.scale(image.load("LvL/back.png"), (900, 500))


    window.blit(background,(0, 0))
    with open("LvL/SettingsC.json", "r", encoding="utf-8") as file:
        SettingsConfig = json.load(file)
    gold = Gold("LvL/portal.png", 750, 430, 2, 50, 50)
    hero = Player("LvL/hero.png", 50, 50, SettingsConfig['HeroSpeed'], 20, 20)
    cyborg = Enemy("LvL/enemyR.png", 110, 100, SettingsConfig['MonsterSpeed']+7, 50, 50)
    cyborg2 = Enemy("LvL/enemyR.png", 650, 315, SettingsConfig['MonsterSpeed']+7, 70, 70)
    enemyB = EnemyB("LvL/enemyB.png", 200, 410, SettingsConfig['MonsterSpeed']+1, 30, 30)
    enemyB2 = EnemyB("LvL/enemyB.png", 260, 485, SettingsConfig['MonsterSpeed'], 30, 30)
    enemyB3 = EnemyB("LvL/enemyB.png", 320, 410, SettingsConfig['MonsterSpeed']+2, 30, 30)
    enemyB4 = EnemyB("LvL/enemyB.png", 380, 485, SettingsConfig['MonsterSpeed']+1, 30, 30)
    enemyB5 = EnemyB("LvL/enemyB.png", 440, 410, SettingsConfig['MonsterSpeed'], 30, 30)
    enemyB6 = EnemyB("LvL/enemyB.png", 500, 485, SettingsConfig['MonsterSpeed']+2, 30, 30)
    enemyB7 = EnemyB("LvL/enemyB.png", 560, 410, SettingsConfig['MonsterSpeed']+1, 30, 30)
    enemyB8 = EnemyB("LvL/enemyB.png", 620, 485, SettingsConfig['MonsterSpeed'], 30, 30)

    button1 = GameSprite("LvL/button.png", 40, 90 ,2, 20, 20)
    button2 = GameSprite("LvL/button.png", 40, 100 ,2, 20, 20)
    button3 = GameSprite("LvL/button.png", 40, 110 ,2, 20, 20)
    button4 = GameSprite("LvL/button.png", 40, 120 ,2, 20, 20)
    button5 = GameSprite("LvL/button.png", 50, 120 ,2, 20, 20)
    button6 = GameSprite("LvL/button.png", 850, 400 ,2, 50, 50)

    walls = []
    walls.append(Wall(0, -9, 900, 10, (255, 255, 255)))
    walls.append(Wall(0, 499, 900, 10, (255, 255, 255)))
    walls.append(Wall(0, 0, 10, 500, (255, 255, 255)))
    walls.append(Wall(890, 0, 10, 500, (255, 255, 255)))
    walls.append(Wall(700, 50, 200, 10, (255, 255, 255)))

    walls.append(Wall(100, 0, 10, 100, (255, 255, 255)))
    walls.append(Wall(100, 150, 10, 350, (255, 255, 255)))

    walls.append(Wall(700, 0, 10, 325, (255, 255, 255)))
    walls.append(Wall(700, 375, 10, 125, (255, 255, 255)))

    mixer.init()
    mixer.music.load("LvL/Playboi-Sky.ogg")
    mixer.music.set_volume(SettingsConfig['MusicVolumeLvl'])
    mixer.music.play()


    run = True
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
                

        if cyborg.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if cyborg2.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if gold.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти виграв!")
        if enemyB.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB2.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB3.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB4.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB5.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB6.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB7.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if enemyB8.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")

            
        if button6.rect.colliderect(hero.rect):
            gold = Gold("LvL/portal.png", 780, 80, 2, 50, 50)

        if button1.rect.colliderect(hero.rect):
            walls.append(Wall(100, 75, 100, 10, (255, 255, 255)))
            walls.append(Wall(250, 75, 300, 10, (255, 255, 255)))
            walls.append(Wall(600, 75, 100, 10, (255, 255, 255)))  

            walls.append(Wall(100, 165, 450, 10, (255, 255, 255)))
            walls.append(Wall(600, 165, 100, 10, (255, 255, 255)))  

        if button2.rect.colliderect(hero.rect):
            walls.append(Wall(150, 30, 450, 10, (255, 255, 255))) 
            walls.append(Wall(300, 30, 10, 45, (255, 255, 255))) 

        if button3.rect.colliderect(hero.rect):
            walls.append(Wall(190, 200, 10, 200, (255, 255, 255)))
            walls.append(Wall(250, 200, 450, 10, (255, 255, 255)))
            walls.append(Wall(200, 230, 450, 10, (255, 255, 255)))  
            walls.append(Wall(250, 260, 450, 10, (255, 255, 255)))
            walls.append(Wall(200, 290, 450, 10, (255, 255, 255))) 

        if button4.rect.colliderect(hero.rect):
            walls.append(Wall(190, 400, 460, 10, (255, 255, 255))) 
            walls.append(Wall(700, 400, 150, 10, (255, 255, 255))) 
            
        if button5.rect.colliderect(hero.rect):
            walls.append(Wall(750, 300, 150, 10, (255, 255, 255))) 
            walls.append(Wall(700, 270, 150, 10, (255, 255, 255))) 
            walls.append(Wall(750, 240, 150, 10, (255, 255, 255))) 
            walls.append(Wall(700, 210, 150, 10, (255, 255, 255))) 
            walls.append(Wall(750, 180, 150, 10, (255, 255, 255))) 
            walls.append(Wall(700, 150, 150, 10, (255, 255, 255))) 

        button1.update()
        button2.update()
        button3.update()
        button4.update()
        button5.update()
        button6.update()
        gold.update()
        hero.update()
        cyborg.update()
        cyborg2.update()
        enemyB.update()
        enemyB2.update()
        enemyB3.update()
        enemyB4.update()
        enemyB5.update()
        enemyB6.update()
        enemyB7.update()
        enemyB8.update()

        for wall in walls:
            if wall.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")

        window.blit(background,(0, 0))
        for wall in walls:
            wall.draw(window)
                
        button1.draw(window)
        button2.draw(window)
        button3.draw(window)
        button4.draw(window)
        button5.draw(window)
        button6.draw(window)
        gold.draw(window)
        hero.draw(window)
        cyborg.draw(window)
        cyborg2.draw(window)
        enemyB.draw(window)
        enemyB2.draw(window)
        enemyB3.draw(window)
        enemyB4.draw(window)
        enemyB5.draw(window)
        enemyB6.draw(window)
        enemyB7.draw(window)
        enemyB8.draw(window)

        pygame.init()
        fontT = pygame.freetype.SysFont(None, 20)
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/2000 % 60)
        minutes=int(ticks/120000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        fontT.render_to(window, (750, 20), out, pygame.Color(250, 0, 0))
        pygame.display.flip()
        display.update()
        clock.tick(120)