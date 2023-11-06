from typing import List, Tuple
from pokemon import Pokemon
from pokemontype import PokeType

class grasspokemon(Pokemon):
    def __init__(self, name, pokedexid, level, living_points, attacking_points, defensive_points, attack: List[Tuple[str, int]]):
        super().__init__(name, pokedexid, level, living_points, attacking_points, defensive_points, attack)
        self.type = PokeType(2)

    def lvlup(self):
        pass