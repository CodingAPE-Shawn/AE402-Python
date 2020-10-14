import pygame
import random
pygame.init()


def randColour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

black = pygame.color.Color("#000000")
colour = randColour()

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
            colour = randColour()
        if event.type == pygame.QUIT:
            done = True
    if click and count < limit:
        pygame.draw.circle(screen, colour, pos, count)
        count += 1
        if count >= limit:
            click = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()









