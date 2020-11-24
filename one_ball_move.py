import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("My Ball Game")
clock = pygame.time.Clock()
done = False

#ball setup
ball = pygame.Surface((70,70)) 
ball.fill(WHITE)
pygame.draw.circle(ball, RED, (35,35), 35)
rect = ball.get_rect()
rect.center = (320,240)
x, y = rect.topleft
speed = 3

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
    screen.fill(WHITE)
    x += speed
    rect.center = (x,y)     #坐標差異讓它移動
    print(rect.center)
    if(rect.left <= 0 or rect.right >= screen.get_width()):   #到達左右邊界
        speed *= -1            #正負值交換

    screen.blit(ball, rect.topleft)  #繪製藍球
    clock.tick(60)
    pygame.display.flip()


pygame.quit()