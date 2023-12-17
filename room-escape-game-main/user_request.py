import pygame

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class Move:
    def __init__(self, room):
        self.__observers = []
        self.room = room

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start new wave" and model.enemies.is_empty():
            model.enemies.add(10)
            model.wave += 1


class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_sell_cost()
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """(Bonus.1) upgrade tower"""
        if user_request in ['damage', 'range', 'cd_time']:
            upgrade_name = user_request
            if model.selected_tower.level[upgrade_name] < 5:
                # ---Bonus-1---
                # upgrade tower
                # if the money > upgrade cost of the selected tower , level+1
                # use model.selected_tower to access the selected tower data
                # use model.selected_tower.get_upgrade_cost(str) to access the upgrade cost
                # use model.money to access to money data
                pass


class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["fireman", "firetruck", "extinguisher"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"fireman": Tower.Fireman(x, y), "firetruck": Tower.Firetruck(x, y), "extinguisher": Tower.Extinguisher(x, y)}
                new_tower = tower_dict[user_request]
                if model.money > new_tower.build_cost:
                    model.money -= new_tower.build_cost
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            #model.sound.play()


class Mute:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            #model.sound.play()

class Continue:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "continue":
            model._is_pause = False

class Pause:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "pause":
            model._is_pause = True
