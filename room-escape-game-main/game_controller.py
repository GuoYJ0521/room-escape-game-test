import pygame


# controller
class GameController:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0,
                       "pause": False
                       }


        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.model.get_request(self.events)
        pass


    # def update_user_request(self):
    #     self.request = self.model.get_request(self.events)
    #     self.model.user_request(self.request)
    #     self.model.call_menu()

    # 在 game loop 裡跑的
    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None,
                       "pause": False
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # 叫出選單
                    self.events["keyboard key"] = pygame.K_ESCAPE
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

        if self.model.is_pause:
            self.events["pause"] = True
        else:
            self.events["pause"] = False

    def update_view(self):
        # render background
        self.view.draw_bg()
        # TODO : 各房間的場景切換
        if not self.model.investigation:
            self.view.draw_room(self.model.cur_room, self.model.wall)
        else:
            self.view.draw_item(self.model.investigation_item)
            pass




    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def is_pause(self):
        return self.events["pause"]