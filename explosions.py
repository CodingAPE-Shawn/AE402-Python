import pygame
black = (0,0,0)
red = (255,0,0)

pygame.init()
windowSize = (400, 300)
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

count = 0
click = False #控制判斷是否點擊
limit = 30 #圓要爆炸的大小
pos = (0, 0)

done = False
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
        if event.type == pygame.QUIT:
            done = True
    if click and count < limit:
        pygame.draw.circle(screen, red, pos, count)
        count += 1
        if count >= limit:
            click = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()