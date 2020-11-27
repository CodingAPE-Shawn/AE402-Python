import pygame
import random

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()
window_size = (800,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('collide game')

done = False
clock = pygame.time.Clock()

block_x = random.randrange(0,800)
block_y = random.randrange(0,600)
block_width = 50
block_height = 50

player_x = 300
player_y = 300
player_width = 50
player_height = 50
collide = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #判斷碰撞
    x_collide = block_x<player_x<block_x+block_width or block_x<player_x+player_width<block_x+block_width
    y_collide = block_y<player_y<block_y+block_height or block_y<player_y+player_height<block_y+block_height
    if x_collide and y_collide and not collide:
        collide = True
    
    player_x,player_y = pygame.mouse.get_pos()
    screen.fill(white)
    pygame.draw.rect(screen, red, [player_x,player_y,player_width,player_height])
    if not collide:
        pygame.draw.rect(screen, black, [block_x,block_y,block_width,block_height])
    
    
    pygame.display.flip()
    clock.tick(40)

pygame.quit()
