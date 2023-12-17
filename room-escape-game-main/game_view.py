import pygame
from setting import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font_size = 30
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)
        self.bg = None

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    # TODO : 畫出不同房間與牆面的布局 裏頭要有個判別式 以便選擇背景
    # 依照 room 中的 layout data 將物品畫出
    def draw_room(self, room,wall):
        self.win.blit(room.bg_image[wall-1], (50, 50))
        for item in room.wall[str(wall)].object:
            self.win.blit(item.image, item.rect)
    # TODO : 畫出調查物件的畫面
    def draw_item(self, investigation_item):
        self.win.blit(investigation_item.focus, (50, 50))
        for item in investigation_item.object:
            self.win.blit(item.image, item.rect)