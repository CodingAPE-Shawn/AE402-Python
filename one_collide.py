import pygame
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()
window_size = (800,600)
screen = pygame.display.set_mode(window_size)

#block 被撞擊的方塊
block_x = 100
block_y = 100
block_width = 50
block_height = 50

#player
play_x = 500
play_y  = 500
player_width = 50
player_height = 50

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #play_x,play_y = pygame.mouse.get_pos()
    screen.fill(white)
    pygame.draw.rect(screen,black,[100,100,50,50])
    pygame.draw.rect(screen,red,[play_x,play_y,50,50])
    pygame.display.flip()
    clock.tick(40)

pygame.quit()

