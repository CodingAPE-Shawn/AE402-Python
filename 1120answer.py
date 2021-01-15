import pygame
white = (255,255,255)
black = (0,0,0)

pygame.init()
window_size = (800,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('load_image')

done = False

clock = pygame.time.Clock()
player_image = pygame.image.load("C:\\Users\\ShawnHou\\Desktop\\image\\player.png")
bg_image = pygame.image.load("C:\\Users\\ShawnHou\\Desktop\\image\\space.jpg")
player_image.convert( )

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x,y = pygame.mouse.get_pos()
    screen.fill(white)
    screen.blit(bg_image,(0,0))
    screen.blit(player_image,(x,y))
    pygame.display.flip()
    clock.tick(40)

pygame.quit()
# test
