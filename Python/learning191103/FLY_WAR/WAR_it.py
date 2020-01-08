import pygame
import random
import time
import WAR as war
import os

pygame.init()
pygame.mixer.init()

WIDTH = 750
HEIGHT = 750
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我的第一个游戏")


game_forder=os.path.dirname('E:\Workspace\Python\learning191103\FLY_WAR\\')
img_folder=os.path.join(game_forder,'img')
player_img = pygame.image.load(os.path.join(img_folder,'python-logo.png')).convert()


# 颜色
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 定义文本
myfont = pygame.font.Font(None, 60)


# 一个精灵的CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 确定图片
        self.image = player_img
        # 设计一个矩形跟踪精灵的坐标
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # 声明精灵所在位置
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        self.rect.x+=5
        if self.rect.left>WIDTH:
            self.rect.right=0





# pygame.display.flip()
# screen.fill(BLUE)
# pygame.display.flip()

# 添加精灵组
clock = pygame.time.Clock()

# 精灵组声明
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)






# 输出文本
def showFont(some_font):
    # 声明字体与字号
    myfont = pygame.font.Font(None, 60)
    textImage = myfont.render(some_font, True, WHITE)
    screen.blit(textImage, (10, 10))
    pygame.display.flip()


# 程序开始时
count = 0
start = time.time()
war.putHello()
turn_on = True
while turn_on:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    clock.tick(FPS)
    showFont('ok')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            turn_on = False
    now = time.time()
    fps = count / (now - start)
    fps = int(fps)
    fpsImage = myfont.render('FPS:' + str(fps), True, WHITE)
    screen.blit(fpsImage, (WIDTH / 2, 0))
    # 精灵组更新
    all_sprites.update()
    # DRAW/RENDER
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    count += 1
pygame.quit()
