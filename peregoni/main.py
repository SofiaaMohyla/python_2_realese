import json
import sys
import time
from random import randint

import pygame
from car import Player
from car_bot import CAR

def endgame(window):
    fps = pygame.time.Clock()
    font = pygame.font.Font(None, 36)  # Choose a font and size for the text
    button_rect = pygame.Rect(105, 360, 290, 50)  # Define the button's rectangle

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")  # You can replace this with any action you want
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

        window.fill((250, 251, 250))  # Fill the window with white color
        pygame.draw.rect(window, (0, 0, 255), button_rect)  # Draw the button
        pygame.draw.rect(window, (0, 0, 255), button_rect, 10)  # Draw the button border
        text_surface = font.render("Програв", True, (0, 0, 0))  # Render the text
        window.blit(text_surface, (200, 255))  # Position the text
        text_surface = font.render("Вийти в головне меню", True, (0, 0, 0))
        window.blit(text_surface, (110, 373))

        pygame.display.flip()
        fps.tick(30)
    

def start_game():
    global settings
    pygame.font.init()
    window = pygame.display.set_mode((500, 650))
    pygame.display.set_caption('Гра')
    fps = pygame.time.Clock()
    settings = {}
    start_time = time.time()

    def read_data():
        global settings
        try:
            with open("settings.json", "r", encoding="utf-8") as file:
                settings = json.load(file)
        except:
            settings = {
                "skin": "optimys_prime/img.png",
                "money": 100
            }

    def write_data():
        global settings
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4, ensure_ascii=False)

    read_data()

    roket = Player(270, 290, 58, 128, settings["skin"], 1)
    bacground = pygame.transform.scale(
        pygame.image.load("optimys_prime/дорога.png"), (500, 650)
    )

    car1 = []
    for i in range(1):
        car1.append(CAR(randint(36, 36), randint(-800, -200), 58, 128, "optimys_prime/автомобіль_бот.png", 4))
        car1.append(CAR(randint(107, 107), randint(-600, -200), 58, 128, "optimys_prime/автомобіль_бот_2.png", 4))
        car1.append(CAR(randint(185, 185), randint(-1100, -600), 58, 128, "optimys_prime/автомобіль_бот.png", 4))
        car1.append(CAR(randint(419, 419), randint(-900, -400), 58, 128, "optimys_prime/автомобіль_бот_2.png", 4))
        car1.append(CAR(randint(270, 270), randint(-1100, -800), 58, 128, "optimys_prime/автомобіль_бот3.png", 4))
        car1.append(CAR(randint(339, 339), randint(-900, -200), 58, 128, "optimys_prime/втомобіль_бот4.png", 4))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            for car in car1:
               if roket.hitbox.colliderect(car.hitbox):
                    endgame(window)
                    pygame.quit()
                    return
        window.blit(bacground, (5, 5))
        for car in car1:
            car.draw(window)
            car.move()
        if time.time()- start_time > 3:
            read_data()
            settings["money"] += 1

            write_data()
            start_time = time.time()
       
        roket.move()
        roket.draw(window)
        pygame.display.flip()
        
        
        fps.tick(30)

