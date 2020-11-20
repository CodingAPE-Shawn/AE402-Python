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
fire = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire = True
                bullet_x,bullet_y = pygame.mouse.get_pos()
    x,y = pygame.mouse.get_pos()
    screen.fill(white)
    screen.blit(bg_image,(0,0))
    if fire:
        bullet_y-=5
        pygame.draw.circle(screen,white,(bullet_x+50,bullet_y-20),10)
        
    screen.blit(player_image,(x,y))
    pygame.display.flip()
    clock.tick(40)

pygame.quit()
