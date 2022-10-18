# package pong.model

from pong.model.Config import GAME_WIDTH, GAME_HEIGHT

"""
 * A Ball for the Pong game
 * A model class
"""


class Ball:
    WIDTH = 20
    HEIGHT = 20

    def __init__(self, x, y, width=20, height=20, dx=0, dy=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy


    def stop(self):
        self.dx = self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_max_x(self):
        return self.x - self.width / 2

    def get_max_y(self):
        return self.y - self.height / 2

    def get_center_x(self):
        return self.x - self.width / 2

    def get_center_y(self):
        return self.y - self.height / 2