# package pong.view
import pygame

from pong.model import *
from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler
from pong.model.Ball import Ball
from pong.model.Pong import Pong
#from pong.view.theme.Cool import Cool
#from pong.view.theme.Duckie import Duckie
from pong.model.Paddle import Paddle
from pong.model.Config import *
from pong.view.Assets import *


class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """


    running = False  # Is game running?
    pygame.init()
    screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    points_font = pygame.font.SysFont("dengxian", 20)
    game_over_font = pygame.font.SysFont("dengxian", 72)
    clock = pygame.time.Clock()
    ball = Ball(GAME_WIDTH/2, GAME_HEIGHT/2) 
    paddle_1 = Paddle(50, (GAME_HEIGHT/2))
    paddle_2 = Paddle(GAME_WIDTH - 50, GAME_HEIGHT / 2)
    ball_img = Assets.get_image("Ball.png").convert_alpha()
    ball_img_height = (ball_img.get_height()/2)
    ball_img_width = (ball_img.get_width()/2)
    paddle_1_img = Assets.get_image("coolbluepaddle.png").convert()
    paddle_2_img = Assets.get_image("coolredpaddle.png").convert()

    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Pong.set_speed_right_paddle(0, Paddle.MAX_DY)
            elif event.key == pygame.K_DOWN:
                Pong.set_speed_right_paddle(0, -Paddle.MAX_DY)
            elif event.key == pygame.K_q:
                # TODO
                pass
            elif event.key == pygame.K_a:
                # TODO
                pass

    @classmethod
    def key_released(cls, event):
        if not cls.running: #interval
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                # TODO
                pass
            elif event.key == pygame.K_q:
                # TODO
                pass
            elif event.key == pygame.K_a:
                # TODO
                pass

    # ---- Menu handling (except themes) -----------------

    # TODO Optional

    @classmethod
    def new_game(cls):
        pong = Pong(cls.paddle_1, cls.paddle_2, cls.ball)
        #    keep_going &= self.__check_for_quit(event)
        return cls.running

    @classmethod
    def kill_game(cls):
        cls.running = False
        # TODO kill all aspects of game

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

#    assets = None

#    @classmethod
#    def handle_theme(cls, menu_event):
#        s = "Cool"  # ((MenuItem) menu_event.getSource()).getText()
#        last_theme = cls.assets
#        try:
#            if s == "Cool":
#                cls.assets = Cool()
#            elif s == "Duckie":
#                cls.assets = Duckie()
#            else:
#                raise ValueError("No such assets " + s)
#        except IOError as ioe:
#            cls.assets = last_theme

    # ---------- Rendering -----------------
    @classmethod
    def render(cls):
        cls.draw_background()
        cls.paste_score_on_surface()
        pygame.draw.circle(cls.screen, cls.WHITE, (cls.ball.get_center_x(), cls.ball.get_center_y()), (cls.ball.get_width()/2))
        pygame.draw.rect(cls.screen, cls.WHITE, (cls.paddle_1.get_x(), cls.paddle_1.get_y() , cls.paddle_1.get_width(), cls.paddle_1.get_height()))
        pygame.draw.rect(cls.screen, cls.WHITE, (cls.paddle_2.get_x(), cls.paddle_2.get_y(), cls.paddle_2.get_width(), cls.paddle_2.get_height()))
        cls.render_texture_pong()
    

    @classmethod
    def paste_score_on_surface(cls):
        score_player_1, score_player_2 = cls.draw_score_img()
        rect_1 = score_player_1.get_rect()
        rect_1.topleft = (5, 10)
        cls.screen.blit(score_player_1, rect_1)
        rect_2 = score_player_2.get_rect()
        rect_2.topright = (GAME_WIDTH - 5, 10)
        cls.screen.blit(score_player_2, rect_2)

    @classmethod
    def render_texture_pong(cls):
        cls.screen.blit(cls.paddle_1_img, (cls.paddle_1.get_x(), cls.paddle_1.get_y()))
        cls.screen.blit(cls.paddle_2_img, (cls.paddle_2.get_x(), cls.paddle_2.get_y()))
        cls.screen.blit(cls.ball_img,(cls.ball.get_x() - cls.ball_img_width - 11, cls.ball.get_y()-cls.ball_img_height - 11))


    @classmethod
    def draw_background(cls):
        cls.screen.fill(cls.BLACK)

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
        while running:
            cls.clock.tick(60)
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
            
        pass
