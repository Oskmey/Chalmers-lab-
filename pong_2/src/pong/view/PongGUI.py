# package pong.view

import pygame


from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler
from pong.model.Ball import Ball
from pong.model.Pong import *
#from pong.view.theme.Cool import Cool
#from pong.view.theme.Duckie import Duckie
from pong.model.Paddle import Paddle
from pong.model.Config import *
from pong.view.Assets import *
from pong.view.theme.Duckie import *
from pong.view.theme.Cool import *
class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """


    running = True  # Is game running?
    pygame.init()
    screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
    pygame.display.set_caption("PONG")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    points_font = pygame.font.SysFont("dengxian", 20)
    game_over_font = pygame.font.SysFont("dengxian", 72)
    clock = pygame.time.Clock()
#    ball_img = Assets.get_image("Ball.png").convert_alpha()
#    ball_img_height = (ball_img.get_height()/2)
#    ball_img_width = (ball_img.get_width()/2)
#    paddle_1_img = Assets.get_image("coolbluepaddle.png").convert()
#    paddle_2_img = Assets.get_image("coolredpaddle.png").convert()
    
    theme = "Duckie"
    assets = None  # Please choose the theme! (assets will update)

 

    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.key == pygame.K_UP:
                Pong.set_speed_left_paddle(-Paddle.PADDLE_SPEED)
        elif event.key == pygame.K_DOWN:
                Pong.set_speed_left_paddle(Paddle.PADDLE_SPEED)
        elif event.key == pygame.K_q:
            Pong.set_speed_right_paddle(-Paddle.PADDLE_SPEED)
        elif event.key == pygame.K_a:
            Pong.set_speed_right_paddle(Paddle.PADDLE_SPEED)
        elif event.key == pygame.K_ESCAPE:
            Pong.quit_game()

    @classmethod
    def key_released(cls, event):
        if not cls.running: #interval
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Pong.set_speed_left_paddle(0)
            elif event.key == pygame.K_DOWN:
                Pong.set_speed_left_paddle(0)
            elif event.key == pygame.K_q:
                Pong.set_speed_right_paddle(0)
            elif event.key == pygame.K_a:
                Pong.set_speed_right_paddle(0)
                pass

    # ---- Menu handling (except themes) -----------------

    # TODO Optional

    @classmethod
    def new_game(cls):
        pass


    # -------- Event handling (events sent from model to GUI) ------------

    class ModelEventHandler(EventHandler):
        def on_model_event(self, evt: ModelEvent):
            if evt.event_type == ModelEvent.EventType.NEW_BALL:
                # TODO Optional
                pass
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_PADDLE:
                PongGUI.assets.ball_hit_paddle_sound.play()
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_WALL_CEILING:
                # TODO Optional
                pass

    # ################## Nothing to do below ############################

    # ---------- Theme handling ------------------------------



    @classmethod
    def handle_theme(cls):
          # ((MenuItem) menu_event.getSource()).getText()
        last_theme = cls.assets
        try:
           if cls.theme == "Cool":
               cls.assets = Cool()
           elif cls.theme == "Duckie":
               cls.assets = Duckie()
           else:
               raise ValueError("No such assets ")
        except IOError as ioe:
            cls.assets = last_theme

    # ---------- Rendering -----------------
    
    @classmethod
    def render(cls):
        cls.draw_background()
        cls.draw_obj()
        cls.paste_score_on_surface()

    @classmethod
    def draw_obj(cls):
        objects_to_draw = Pong.get_all_items_with_position()
        for object in objects_to_draw:
            img = Assets.get(objects_to_draw.index(object))
            img = pygame.transform.smoothscale(img, (object.get_width(), object.get_height()))
            if not object == Pong.ball:
                cls.screen.blit(img, ((object.get_x()), (object.get_y())))
            elif object == Pong.ball:
                cls.screen.blit(img, (object.get_max_x(), object.get_max_y()))


    @classmethod
    def paste_score_on_surface(cls):
        score_player_1, score_player_2 = cls.draw_score_img()
        rect_1 = score_player_1.get_rect()
        rect_1.topleft = (5, 10)
        cls.screen.blit(score_player_1, rect_1)
        rect_2 = score_player_2.get_rect()
        rect_2.topright = (GAME_WIDTH - 5, 10)
        cls.screen.blit(score_player_2, rect_2)

#    @classmethod
#    def render_texture_pong(cls):
#        cls.screen.blit(cls.paddle_1_img, (Pong.paddle_1.get_x(), Pong.paddle_1.get_y()))
#        cls.screen.blit(cls.paddle_2_img, (Pong.paddle_2.get_x(), Pong.paddle_2.get_y()))
#        cls.screen.blit(cls.ball_img,(Pong.ball.get_x() - cls.ball_img_width - 11, Pong.ball.get_y()- cls.ball_img_height - 11))


    @classmethod
    def draw_background(cls):
        img_bg = cls.assets.get_background()
        img_bg = pygame.transform.scale(img_bg, DEFAULT_IMAGE_SIZE)
        cls.screen.blit(img_bg, (0,0))

    @classmethod
    def draw_score_img(cls):
        player_1_points = Pong.get_points_left()
        player_2_points = Pong.get_points_right()
        text_1 = f"Player 1 points: {player_1_points}"
        text_2 = f"Player 2 points: {player_2_points}"
        score_player_1 = cls.points_font.render(text_1, True, cls.WHITE)
        score_player_2 = cls.points_font.render(text_2, True, cls.WHITE)
        return score_player_1, score_player_2

    # ---------- Game loop ----------------

    @classmethod
    def run(cls):
        running = True
        cls.handle_theme()
        while running:
            cls.clock.tick(60)
            cls.handle_events()
            Pong.update()
            cls.render()
            pygame.display.flip()
            
    @classmethod
    def update(cls):
        # TODO
        pass

    @classmethod
    def handle_events(cls):
        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.KEYDOWN:
                cls.key_pressed(event)
            elif event.type == pygame.KEYUP:
                cls.key_pressed(event)
            elif event.type == pygame.QUIT:
                pygame.quit()

