import pygame
import random
import json


rogelio_stats = { 
    "health": 100,
    "bolas": 5,
    "scraps": 1,
    "xp": 0,
    "size": [50,80],
    "base_damage": 5,
    "weapon_base_damage": 10,
    "location": [400,300]
}



enemy_stats= { 
    "skelly": {
    "health":20,
    "location": [400,300],
    "level": 1,
    "base_damage": 10,
    "size": [40,80]
    },
    "jorge_el_terrible": {
        "health":80,
        "location":[400,300],
        "level": 1,
        "base_damage": 17,
        "size": [400,120]
    },
    "Cumbia_skelly_boss": {
            "health": 80,
            "location": [400,300],
            "level": 1,
            "base_damage": 17,
            "size":[75,120]
}
}



def load_game():
    global rogelio
    try:
        with open("save_data.json", "r")as file:
            rogelio = json.load(file)
            print("Game loaded !")
    except FileNotFoundError:
        print("No save file found. Using default stats.")


def move_rogelio():
    global rogelio


def save_game():
    with open("save_data.json", "w")as file:
        json.dump(rogelio, file)
        print("Game saved !")


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Dark Mirage")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 22)
rogelio_x = 375
rogelio_y = 275
skelly_x = 440
skelly_y = 340
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    screen.fill((210, 180, 140))
    title_surface = font.render("DARK MIRAGE", True, (0, 0, 0))
    screen.blit(title_surface,  (350, 50))
    pygame.draw.rect(screen, (0, 255, 0), (rogelio_x, rogelio_y, 50, 50))
    pygame.display.flip()
pygame.quit()
