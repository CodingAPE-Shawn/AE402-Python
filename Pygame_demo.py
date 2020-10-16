import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My game')
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    pygame.display.flip()
pygame.quit()
