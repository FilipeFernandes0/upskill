from pokemon import Pokemon
from waterpokemon import watertype
from grasspokemon import grasspokemon


squirtle = watertype("Squirtle", "002", 5, 40, 20,10,[("tackle", 40)])
print(squirtle.type.name)

Bulbasaur = grasspokemon("Bulbasaur", "006", 10, 50, 30,20,[("Vine whip", 40)])
print(Bulbasaur.type.name)


fight = Bulbasaur.type.name < squirtle.type.name
print(fight)