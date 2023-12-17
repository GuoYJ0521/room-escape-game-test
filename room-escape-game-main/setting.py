import pygame
import os

# game window
WIN_WIDTH = 1024
WIN_HEIGHT = 600

# 解謎視窗大小
# TODO : 大小待訂
GAME_WIDTH = WIN_WIDTH * 0.8
GAME_HEIGHT = WIN_HEIGHT * 0.8

# Frame Per Second
FPS = 60

# base
BASE = pygame.Rect(740, 30, 270, 100)
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("image", "background.png")), (1024, 600))

# 關卡布局
