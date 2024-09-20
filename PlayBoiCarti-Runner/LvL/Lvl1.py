import pygame
from pygame import *
import pygame.freetype
import json

def lvl1():
    def showEndWindow(window, message):
        clock = time.Clock()
        run = True
        font.init()
        text = font.Font(None, 170).render(message, True, (0, 255, 255))
        while run:
            # обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        exit_game() 
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
            if self.rect.x >= 340:
                self.speed *= -1
            if self.rect.x <= 460:
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
    display.set_caption("LvL 1")
    background = transform.scale(image.load("LvL/back.png"), (900, 500))


    window.blit(background,(0, 0))
    with open("LvL/SettingsC.json", "r", encoding="utf-8") as file:
        SettingsConfig = json.load(file)
    gold = Gold("LvL/portal.png", 800, 50, 2, 50, 50)
    hero = Player("LvL/hero.png", 50, 50, SettingsConfig['HeroSpeed'], 20, 20)
    cyborg = Enemy("LvL/mons.png", 350, 150, SettingsConfig['MonsterSpeed'], 30, 40)

    button1 = GameSprite("LvL/button.png", 100, 365 ,2, 20, 20)
    button2 = GameSprite("LvL/button.png", 200, 215 ,2, 20, 20)
    button3 = GameSprite("LvL/button.png", 200, 465 ,2, 20, 20)
    button4 = GameSprite("LvL/button.png", 480, 165 ,2, 20, 20)
    button5 = GameSprite("LvL/button.png", 680, 115 ,2, 20, 20)
    button6 = GameSprite("LvL/button.png", 680, 75 ,2, 20, 20)

    walls = []
    walls.append(Wall(100, 0, 10, 350, (255, 255, 255)))
    walls.append(Wall(100, 400, 10, 100, (255, 255, 255)))

    walls.append(Wall(100, 100, 100, 10, (255, 255, 255)))

    walls.append(Wall(0, -9, 900, 10, (255, 255, 255)))
    walls.append(Wall(0, 499, 900, 10, (255, 255, 255)))

    walls.append(Wall(0, 0, 10, 500, (255, 255, 255)))
    walls.append(Wall(890, 0, 10, 500, (255, 255, 255)))

    mixer.init()
    mixer.music.load("LvL/playboi.ogg")
    mixer.music.set_volume(SettingsConfig['MusicVolumeLvl'])
    mixer.music.play()


    run = True
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
            

        if cyborg.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти програв!")
        if gold.rect.colliderect(hero.rect):
                showEndWindow(window, "Ти виграв!")

        if button1.rect.colliderect(hero.rect):
            walls.append(Wall(200, 250, 10, 200, (255, 255, 255)))
            walls.append(Wall(200, 100, 10, 100, (255, 255, 255)))
            walls.append(Wall(200, 50, 10, 60, (255, 255, 255)))
            walls.append(Wall(300, 0, 10, 60, (255, 255, 255)))

            walls.append(Wall(380, 200, 10, 200, (255, 255, 255)))
            walls.append(Wall(300, 100, 10, 100, (255, 255, 255)))
            walls.append(Wall(360, 450, 10, 100, (255, 255, 255)))

            walls.append(Wall(200, 400, 100, 10, (255, 255, 255)))
            walls.append(Wall(200, 50, 100, 10, (255, 255, 255)))
            walls.append(Wall(250, 100, 100, 10, (255, 255, 255)))
            walls.append(Wall(280, 300, 100, 10, (255, 255, 255)))

        if button2.rect.colliderect(hero.rect):
            walls.append(Wall(520, 0, 10, 50, (255, 255, 255)))
            walls.append(Wall(480, 50, 10, 100, (255, 255, 255)))
            walls.append(Wall(480, 200, 10, 250, (255, 255, 255)))
            walls.append(Wall(580, 100, 10, 100, (255, 255, 255)))

            walls.append(Wall(380, 50, 300, 10, (255, 255, 255)))
            walls.append(Wall(360, 450, 130, 10, (255, 255, 255)))
        if button3.rect.colliderect(hero.rect):
            walls.append(Wall(520, 0, 10, 50, (255, 255, 255)))
            walls.append(Wall(480, 50, 10, 100, (255, 255, 255)))
            walls.append(Wall(480, 200, 10, 250, (255, 255, 255)))
            walls.append(Wall(580, 100, 10, 100, (255, 255, 255)))

            walls.append(Wall(380, 50, 300, 10, (255, 255, 255)))
            walls.append(Wall(360, 450, 130, 10, (255, 255, 255)))

        if button4.rect.colliderect(hero.rect):
            walls.append(Wall(580, 250, 10, 200, (255, 255, 255)))
            walls.append(Wall(780, 250, 10, 300, (255, 255, 255)))

            walls.append(Wall(700, 150, 300, 10, (255, 255, 255)))
            walls.append(Wall(580, 400, 100, 10, (255, 255, 255)))
            walls.append(Wall(580, 250, 200, 10, (255, 255, 255)))

        if button5.rect.colliderect(hero.rect):
            gold = Gold("LvL/portal.png", 810, 400, 2, 50, 50)
        
        if button6.rect.colliderect(hero.rect):
            gold = Gold("LvL/portal.png", 810, 400, 2, 50, 50)



        button1.update()
        button2.update()
        button3.update()
        button4.update()
        button5.update()
        button6.update()
        gold.update()
        hero.update()
        cyborg.update()

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

        def exit_game():
            pygame.quit()

        pygame.init()
        fontT = pygame.freetype.SysFont(None, 20)
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/2000 % 60)
        minutes=int(ticks/120000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        fontT.render_to(window, (410, 20), out, pygame.Color(250, 0, 0))
        pygame.display.flip()
        display.update()
        clock.tick(120)