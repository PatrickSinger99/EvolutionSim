from abc import ABC
from typing import List
from dataclasses import dataclass


class CreatureBlock(ABC):
    rotation: int  # 0: North, 1: East, 2: South, 3: West
    extendable: List[bool, bool, bool, bool]  # Can be build on? : N, E, S, W


class Brain(CreatureBlock):
    extendable = (True, True, True, True)
    block_id = 1

    def __init__(self):
        self.rotation = 0  # Brain does not have rotation

        self.block_id = Body.block_id
        self.extendable = Body.extendable


class Body(CreatureBlock):
    extendable = (True, True, True, True)
    block_id = 2

    def __init__(self):
        self.rotation = 0  # Body does not have rotation

        self.block_id = Body.block_id
        self.extendable = Body.extendable
