# package pong.view.theme

from pong.model.Ball import Ball
from pong.model.Pong import *
from pong.view.Assets import Assets

"""
   Specific theme

   *** Nothing to do here ***
"""


class Cool(Assets):
    # ------------ Handling Images ------------------------

    background = Assets.get_image("coolBg.png")

    Assets.bind(0, "coolBall.png")
    Assets.bind(1, "coolbluepaddle.png")
    Assets.bind(2, "coolredpaddle.png")
    @classmethod
    def get_background(cls):
        return cls.background

    # -------------- Audio handling -----------------------------
