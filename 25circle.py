import pygame

Black = (0,0,0)
White = (255,255,255)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(White)
    for i in range(100,341,60):
        for j in range(200,441,60):
            pygame.draw.circle(screen,Black,(i,j),30)

    pygame.display.flip()
    
pygame.quit()
            
