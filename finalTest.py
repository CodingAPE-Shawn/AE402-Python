#匯入pygame模組
import pygame
#設定顏色
black = (0,0,0)
white = (255,255,255)
#pygame初始化
pygame.init()
#設定螢幕
size = (640,70)
screen = pygame.display.set_mode(size)
#設定視窗標題
pygame.display.set_caption("final test")
#設定更新時鐘
clock = pygame.time.Clock()
#設定迴圈開關
done = False
#設定球x原先座標
x = 10
#主迴圈
while not done:
    #偵測關閉事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #偵測鍵盤事件
    keys = pygame.key.get_pressed()
    #判斷鍵盤是否為左右按鈕，若是則移動球位置
    if keys[pygame.K_RIGHT]:
        x+=5
    elif keys[pygame.K_LEFT]:
        x-=5
    #螢幕填色
    screen.fill(white)
    #畫出球
    pygame.draw.circle(screen,black,(x,35),10)
    if x>=630:
        x=630
    #螢幕更新
    pygame.display.flip()
    #設定更新時間
    clock.tick(40)
#關閉pygame
pygame.quit()