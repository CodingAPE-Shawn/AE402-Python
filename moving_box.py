import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("走動的方塊")

done = False

clock = pygame.time.Clock()

x = 10
y = 10

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-=5
            elif event.key == pygame.K_RIGHT:
                x+=5
            elif event.key == pygame.K_UP:
                y-=5
            elif event.key == pygame.K_DOWN:
                y+=5
            else:
                pass

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [x + 10, y + 10, 10, 10])
    pygame.display.flip()

    clock.tick(60)
pygame.quit()

