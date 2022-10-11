# package pong.view
import pygame

from pong.model import *
from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler
from pong.model.Pong import Pong
from pong.view.theme.Cool import Cool
from pong.view.theme.Duckie import Duckie
from pong.model.Paddle import Paddle
from pong.model.Config import *
from pong.assets import get_image

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


    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYDOWN:
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

    @classmethod
    def key_released(cls, event):
        if not cls.running:
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
        # TODO rebuild OO model as needed
        pass

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

    assets = None

    @classmethod
    def handle_theme(cls, menu_event):
        s = "Cool"  # ((MenuItem) menu_event.getSource()).getText()
        last_theme = cls.assets
        try:
            if s == "Cool":
                cls.assets = Cool()
            elif s == "Duckie":
                cls.assets = Duckie()
            else:
                raise ValueError("No such assets " + s)
        except IOError as ioe:
            cls.assets = last_theme

    # ---------- Rendering -----------------
    @classmethod
    def render(cls, assets):
        score_player_1, score_player_2 = cls.draw_score_img()
        rect_1 = score_player_1.get_rect()
        rect_1.topleft = (5, 10)
        cls.screen.blit(score_player_1, rect_1)
        rect_2 = score_player_2.get_rect()
        rect_2.topright = (GAME_WIDTH-5, 10)
        cls.screen.blit(score_player_2, rect_2)
        paddle_1 = Paddle(50, GAME_HEIGHT / 2)
        paddle_2 = Paddle(GAME_WIDTH - 50, GAME_HEIGHT / 2)
        paddle_1_img = get_image(C:\Users\Oskarme\PycharmProjects\pong\pong\assets\img)
        cls.screen.blit(paddle_1_img)
        pygame.draw.rect(cls.screen, cls.WHITE, (paddle_1.get_x(), paddle_1.get_y(), paddle_1.get_width(), paddle_1.get_height()))
        pygame.draw.rect(cls.screen, cls.WHITE, (paddle_2.get_x(), paddle_2.get_y(), paddle_2.get_width(), paddle_2.get_height()))

    @classmethod
    def draw_background(cls):
        cls.screen.fill(cls.BLACK)

    @classmethod
    def draw_score_img(cls):
        player_1_points = 0
        player_2_points = 0
        text_1 = f"Player 1 points: {player_1_points}"
        text_2 = f"Player 2 points: {player_2_points}"
        score_player_1 = cls.points_font.render(text_1, True, cls.WHITE)
        score_player_2 = cls.points_font.render(text_2, True, cls.WHITE)
        return score_player_1, score_player_2

    # ---------- Game loop ----------------

    @classmethod
    def run(cls):
        cls.draw_background()
        running = True
        while running:
            cls.clock.tick(3)
            cls.render()
            pygame.display.flip()

    @classmethod
    def update(cls):
        # TODO
        pass

    @classmethod
    def handle_events(cls):
        # TODO
        pass


if __name__ == "__main__":
    PongGUI.run()
