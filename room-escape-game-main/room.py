import pygame
import os

from wall import *

living_room_1_image = pygame.transform.scale(pygame.image.load(f"image/Room/living_room_1.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_2_image = pygame.transform.scale(pygame.image.load(f"image/Room/living_room_2.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_3_image = pygame.transform.scale(pygame.image.load(f"image/Room/living_room_3.png"), (GAME_WIDTH, GAME_HEIGHT))
living_room_4_image = pygame.transform.scale(pygame.image.load(f"image/Room/living_room_4.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_1_image = pygame.transform.scale(pygame.image.load(f"image/Room/bedroom.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_2_image = pygame.transform.scale(pygame.image.load(f"image/Room/bedroom.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_3_image = pygame.transform.scale(pygame.image.load(f"image/Room/bedroom.png"), (GAME_WIDTH, GAME_HEIGHT))
bedroom_4_image = pygame.transform.scale(pygame.image.load(f"image/Room/bedroom.png"), (GAME_WIDTH, GAME_HEIGHT))

# 章節1的所有房間/牆面
#yj
class LivingRoom:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [living_room_1_image, living_room_2_image, living_room_3_image]

        # 房間牆面數
        self.wall_size = 3

        # 此房間在不同牆面有的物品/座標 (包括移動鍵)
        # 牆面1有這些東西
        self.__object_1 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50),DoorToExit(210, 315)]
        # 牆面2有這些東西
        self.__object_2 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50),DoorToStudy(210, 315),DoorToBedRoom(710, 315),Clock(450,315)]
        # 牆面3有這些東西
        self.__object_3 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50),DoorToKitchen(490, 315),Tv(250,303)]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image,self.__object_1),
                     '2': Wall(self.bg_image,self.__object_2),
                     '3': Wall(self.bg_image,self.__object_3)}

class Study:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [living_room_1_image, living_room_2_image, living_room_3_image, living_room_4_image]

        # 房間牆面數
        self.wall_size = 3

        # 此房間在不同牆面有的物品/座標
        # 牆面1有這些東西
        self.__object_1 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50), Tv(420, 400)]
        # 牆面2有這些東西
        self.__object_2 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50), Tv(420, 400)]
        # 牆面3有這些東西
        self.__object_3 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50), Tv(420, 400)]
        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image, self.__object_1),
                     '2': Wall(self.bg_image, self.__object_2),
                     '3': Wall(self.bg_image, self.__object_3)}

    def switch_wall(self):
        pass

class Kitchen:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [living_room_1_image, living_room_2_image, living_room_3_image, living_room_4_image]

        # 房間牆面數
        self.wall_size = 3

        # 此房間在不同牆面有的物品/座標
        # 牆面1有這些東西
        self.__object_1 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50)]
        # 牆面2有這些東西
        self.__object_2 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50)]
        # 牆面3有這些東西
        self.__object_3 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(900, 50)]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image, self.__object_1),
                     '2': Wall(self.bg_image, self.__object_2),
                     '3': Wall(self.bg_image, self.__object_3)}

    def switch_wall(self):
        pass

class Bedroom:
    def __init__(self):
        # data
        # 房間背景
        self.bg_image = [bedroom_1_image, bedroom_2_image, bedroom_3_image, bedroom_4_image]

        # 房間牆面數
        self.wall_size = 4

        # 此房間在不同牆面有的物品/座標
        # 牆面1有這些東西
        self.__object_1 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(255, 245)]
        # 牆面2有這些東西
        self.__object_2 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(255, 245), Tv(420, 400)]
        # 牆面3有這些東西
        self.__object_3 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(255, 245),DoorToLivingRoom(200, 300)]
        # 牆面4有這些東西
        self.__object_4 = [RightButton(WIN_WIDTH - 50,WIN_HEIGHT/2),LeftButton(20,WIN_HEIGHT/2),MenuButton(255, 245), Tv(420, 400)]

        # 當前牆面/建立此房間的牆面
        # 不同房間的牆面數會不一樣 要注意
        self.wall = {'1': Wall(self.bg_image, self.__object_1),
                     '2': Wall(self.bg_image, self.__object_2),
                     '3': Wall(self.bg_image, self.__object_3),
                     '4': Wall(self.bg_image, self.__object_4)}

    def switch_wall(self):
        pass