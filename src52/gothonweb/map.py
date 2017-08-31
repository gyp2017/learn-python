# -*- coding: utf-8 -*-
# 52 웹 게임 시작

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.path = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
페르칼 25번 행성의 고전족은 여러분의 우주선에 침략하고 모든 승무원을
죽였습니다.
"""
)

    
