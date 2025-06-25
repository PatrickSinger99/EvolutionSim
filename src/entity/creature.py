from creature_block import *
from typing import List


class CreatureGrid:
    def __init__(self, max_size=9):
        self.grid = [[0]]
        self.offset_x = 0
        self.offset_y = 0

    def add(self, instance, coords: List[int, int]):
        self.grid[instance.coords.x][instance.coords.y] = instance


class Creature:
    def __init__(self):

        self.brain = Brain()

