# package pong.view
import pygame
import pong
from pong.model import *
from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler
from pong.model.Pong import Pong
from pong.view.theme.Cool import Cool
from pong.view.theme.Duckie import Duckie


from pong.model.Paddle import PADDLE_SPEED, Paddle
from pong.model.Config import *
class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """

    running = False    # Is game running?
    screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    points_font = pygame.font.SysFont(None, 20)
    game_over_font = pygame.font.SysFont(None, 72)
    clock = pygame.time.Clock()
    Paddle_1 = Paddle
    
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
    def render(cls):
        cls.screen.fill(cls.BLACK)
        player_1_points = 0
        player_2_points = 0
        text_1 = f"Player 1 points: {player_1_points}"
        text_2 = f"Player 2 points: {player_2_points}"
        img_1 = cls.points_font.render(text_1, True, cls.WHITE)
        img_2 = cls.points_font.render(text_2, True, cls.WHITE)
        rect_1 = img_1.get_rect()
        rect_2 = img_2.get_rect()
        rect_1.topleft (10, 10)
        rect_2.topright (10, 10)
        cls.screen.blit(img_1, rect_1)
        cls.screen.blit(img_2, rect_2)
        pygame.draw.rect(cls.screen, cls.WHITE, )
    # ---------- Game loop ----------------

    @classmethod
    def run(cls):
        # TODO
        pass

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
