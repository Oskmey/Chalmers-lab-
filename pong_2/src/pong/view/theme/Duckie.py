# package pong.view.theme

from pong.model.Ball import Ball
from pong.view.Assets import Assets
from pong.model.Pong import *
"""
   Specific theme

   *** Nothing to do here ***
"""


class Duckie(Assets):
    # ------------ Handling Images ------------------------

    background = Assets.get_image("duckieBg.jpg")

    Assets.bind(0, "duckieBall.png")
    Assets.bind(1, "coolbluepaddle.png")
    Assets.bind(2, "coolredpaddle.png")


    @classmethod
    def get_background(cls):
        return cls.background

    # -------------- Audio handling -----------------------------
