# package pong.model


#import pong.event.ModelEvent
#import pong.event.EventBus
import pygame
from pong.model.Paddle import Paddle
from pong.model.Ball import Ball
from pong.model.Config import GAME_HEIGHT, GAME_WIDTH

class Pong:
    """
     * Logic for the Pong Game
     * Model class representing the "whole" game
     * Nothing visual here
    """
    # TODO More attributes
    points_left  = 0
    points_right = 0

    ball = Ball(GAME_WIDTH/2, GAME_HEIGHT/2) 
    paddle_1 = Paddle(50, (GAME_HEIGHT/2))
    paddle_2 = Paddle(GAME_WIDTH - 50, GAME_HEIGHT / 2)
        

    # --------  Game Logic -------------

    timeForLastHit = 0         # To avoid multiple collisions

    @classmethod
    def update(cls):
        cls.paddle_1.move()
        cls.paddle_2.move()

    # --- Used by GUI  ------------------------
    @classmethod
    def get_all_items_with_position(cls):
        drawables = [cls.paddle_1, cls.ball , cls.paddle_2]
        return drawables

    @classmethod
    def get_points_left(cls):
        return cls.points_left

    @classmethod
    def get_points_right(cls):
        return cls.points_right

    @classmethod
    def set_speed_right_paddle(cls, dy):
        cls.paddle_1.set_dy(dy)

    @classmethod
    def set_speed_left_paddle(cls, dy):
        cls.paddle_2.set_dy(dy)
    @classmethod
    def quit_game(cls):
        pygame.quit()

