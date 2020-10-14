import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([800, 600])

pygame.display.set_caption('CMSC 150 is cool')

clock = pygame.time.Clock()


# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("playerShip1_orange.png").convert()
#設置去背
player_image.set_colorkey(WHITE)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, background_position)
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    
    screen.blit(player_image, [x, y])
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit ()
