# -*- coding: utf-8 -*-

class Scene(object):
    pass

class Engine(object):

    def __init__(self, start_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter():
        pass

class CentralCorridor(Scene):

    def enter():
        pass

class LaserWeaponArmory(Scene):

    def enter():
        pass

class TheBridge(Scene):

    def enter():
        pass

class EscapePod(Scene):

    def enter():
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene():
        pass

    def opening_scene():
        pass

a_map = Map()
a_game = Engine(a_map)
a_game.play()
