from enum import Enum



class PokeType(Enum):

    WATER = 0
    FIRE = 1
    GRASS = 2


    def __eq__(self,other):
        return True if self.name == other.name else False
    
    def __ne__(self, other):
        return True if self.name != other.name else False
    
    def __lt__(self,other):
        if self.name == other.name:
            return False
        elif self.name == "GRASS" and other.name == "FIRE":
            return False
        elif self.name == "GRASS" and other.name == "WATER":
            return True
        elif self.name == "AQUA" and other.name == "GRASS":
            return True
        elif self.name == "AQUA" and other.name == "FIRE":
            return False
        elif self.name == "FIRE" and other.name == "AQUA":
            return True
        elif self.name == "FIRE" and other.name == "GRASS":
            return False
        
    def __gt__(self,other):

        if self.name == other.name:
            return False
        elif self.name == "GRASS" and other.name == "FIRE":
            return 
        elif self.name == "GRASS" and other.name == "WATER":
            return True
        elif self.name == "AQUA" and other.name == "GRASS":
            return False
        elif self.name == "AQUA" and other.name == "FIRE":
            return False
        elif self.name == "FIRE" and other.name == "AQUA":
            return True
        elif self.name == "FIRE" and other.name == "GRASS":
            return False
        