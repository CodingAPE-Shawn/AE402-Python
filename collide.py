"""
碰撞 -- 一對多
"""
import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# player的初始位置
player_x = 0
player_y = 0
player_w = 50
player_h = 50
# block的初始位置

block_w = 50
block_h = 50
block_x = []
block_y = []
collision = []
for i in range(10):
    block_x.append(random.randrange(screen_width-block_w))
    block_y.append(random.randrange(screen_height-block_h))
    collision.append(False)
# 判斷有無撞到的布林變數

# 分數
score = 0
# font物件
font = pygame.font.Font(None, 50)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    # 判斷是否碰撞到了
    for i in range(10):
        xin = block_x[i]<=player_x<=block_x[i]+block_w or block_x[i]<=player_x+player_w<=block_x[i]+block_w
        yin = block_y[i]<=player_y<=block_y[i]+block_h or block_y[i]<=player_y+player_h<=block_y[i]+block_h
        if  xin and yin and not collision[i]:
            collision[i] = True
            score += 1
        
    # 清除視窗畫面
    screen.fill(WHITE)

    # 取得滑鼠座標 (list of (x,y))
    pos = pygame.mouse.get_pos()
    # 畫出player & block
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    for i in range(10):
        if not collision[i]:
            pygame.draw.rect(screen, BLACK, [block_x[i], block_y[i], block_w, block_h])

    # 顯示分數
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))
    
    # 新畫面更新
    pygame.display.flip()

    # 一秒60個frame
    clock.tick(60)
pygame.quit()
