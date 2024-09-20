import pygame
from pygame import *
import pygame.freetype
import json
def lvl2():
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
            if self.rect.x >= 200:
                self.speed *= -1
            if self.rect.x <= 600:
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
    display.set_caption("LvL 2")
    background = transform.scale(image.load("LvL/back.png"), (900, 500))


    window.blit(background,(0, 0))
    with open("LvL/SettingsC.json", "r", encoding="utf-8") as file:
        SettingsConfig = json.load(file)
    gold = Gold("LvL/portal.png", 810, 230, 2, 50, 50)
    hero = Player("LvL/hero.png", 50, 50, SettingsConfig['HeroSpeed'], 20, 20)
    cyborg = Enemy("LvL/enemyR.png", 200, 130, SettingsConfig['MonsterSpeed']+4, 50, 50)
    cyborg2 = Enemy("LvL/enemyR.png", 600, 330, SettingsConfig['MonsterSpeed']+4, 50, 50)

    button1 = GameSprite("LvL/button.png", 40, 90 ,2, 20, 20)
    button2 = GameSprite("LvL/button.png", 40, 100 ,2, 20, 20)
    button3 = GameSprite("LvL/button.png", 40, 110 ,2, 20, 20)
    button4 = GameSprite("LvL/button.png", 40, 120 ,2, 20, 20)
    button5 = GameSprite("LvL/button.png", 40, 130 ,2, 20, 20)
    button6 = GameSprite("LvL/button.png", 760, 230 ,2, 50, 50)

    walls = []
    walls.append(Wall(0, -9, 900, 10, (255, 255, 255)))
    walls.append(Wall(0, 499, 900, 10, (255, 255, 255)))
    walls.append(Wall(0, 0, 10, 500, (255, 255, 255)))
    walls.append(Wall(890, 0, 10, 500, (255, 255, 255)))

    walls.append(Wall(100, 0, 10, 225, (255, 255, 255)))
    walls.append(Wall(100, 275, 10, 250, (255, 255, 255)))

    mixer.init()
    mixer.music.load("LvL/Playboi-Anthem.ogg")
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

        if button1.rect.colliderect(hero.rect):
            walls.append(Wall(350, 200, 10, 100, (255, 255, 255)))
            walls.append(Wall(550, 200, 10, 100, (255, 255, 255)))

            walls.append(Wall(350, 200, 250, 10, (255, 255, 255)))
            walls.append(Wall(350, 300, 250, 10, (255, 255, 255)))

            walls.append(Wall(650, 100, 10, 300, (255, 255, 255)))
            walls.append(Wall(650, 0, 10, 50, (255, 255, 255)))
            walls.append(Wall(650, 450, 10, 50, (255, 255, 255)))

        if button2.rect.colliderect(hero.rect):
            walls.append(Wall(180, 400, 150, 10, (255, 255, 255)))
            walls.append(Wall(400, 400, 200, 10, (255, 255, 255)))
            walls.append(Wall(150, 450, 400, 10, (255, 255, 255)))
            walls.append(Wall(500, 400, 10, 50, (255, 255, 255)))

        if button3.rect.colliderect(hero.rect):
            walls.append(Wall(150, 50, 400, 10, (255, 255, 255)))
            walls.append(Wall(500, 50, 10, 50, (255, 255, 255)))
            walls.append(Wall(180, 100, 150, 10, (255, 255, 255)))
            walls.append(Wall(400, 100, 200, 10, (255, 255, 255)))

        if button4.rect.colliderect(hero.rect):
            walls.append(Wall(180, 100, 10, 100, (255, 255, 255)))
            walls.append(Wall(180, 300, 10, 100, (255, 255, 255)))
            walls.append(Wall(100, 300, 80, 10, (255, 255, 255)))
            walls.append(Wall(100, 190, 80, 10, (255, 255, 255)))

            walls.append(Wall(800, 200, 100, 10, (255, 255, 255)))
            walls.append(Wall(800, 300, 100, 10, (255, 255, 255)))

        if button5.rect.colliderect(hero.rect):

            walls.append(Wall(700, 110, 110, 10, (255, 255, 255)))
            walls.append(Wall(700, 380, 110, 10, (255, 255, 255)))
            walls.append(Wall(800, 0, 10, 120, (255, 255, 255)))
            walls.append(Wall(800, 380, 10, 120, (255, 255, 255)))

            walls.append(Wall(750, 150, 10, 50, (255, 255, 255)))
            walls.append(Wall(750, 300, 10, 50, (255, 255, 255)))
            
        if button6.rect.colliderect(hero.rect):
            gold = Gold("LvL/portal.png", 200, 230, 2, 50, 50)



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

        pygame.init()
        fontT = pygame.freetype.SysFont(None, 20)
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/2000 % 60)
        minutes=int(ticks/120000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        fontT.render_to(window, (410, 250), out, pygame.Color(250, 0, 0))
        pygame.display.flip()
        display.update()
        clock.tick(120)