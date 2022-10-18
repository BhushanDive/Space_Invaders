import pygame
# Initializing the game
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg,(playerX,playerY))


# MAin game loop
running = True
while running:
    # RGB Values for background fill colour
    screen.fill((0,200,150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()