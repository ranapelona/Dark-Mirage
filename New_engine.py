import pygame
import random
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
