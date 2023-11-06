
from __future__ import annotations
from abc import ABC

from typing import List,Tuple


class Pokemon(ABC):
    def __init__(self, name, pokedexid, level, living_points,attacking_points,defensive_points, attack : List[Tuple[str,int]]):
        self.name = name
        self.pokedexid = pokedexid
        self.level = level
        self.living_points =  living_points
        self.attacking_points = attacking_points
        self.defensive_points = defensive_points
        self.attack = attack
        self.experience_points = 0
        self.fight_status = False
        self.alive = True
        self.type = None



    