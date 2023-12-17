import pygame
import os

from object import *
from setting import *


# 章節1的所有房間/牆面

class Wall:
    def __init__(self, bg, item):
        # data
        # 房間背景
        self.bg_image = bg

        # 此牆面有的可互動物品
        self.object = item

