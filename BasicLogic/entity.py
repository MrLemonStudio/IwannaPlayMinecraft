import storage,map
from typing import Self
class Entity:
    def __init__(self, name:str, picture:bytes):
        self.name = name
        self.health:float = 20
        self.damage:float = 1
        self.length:float = 1
        self.height:float = 1
        self.defence:float = 0
        self.can_be_tamed:bool = False
        self.picture = picture
    def attack(self, target:Self)->float:
        target.health -= self.damage*(1-target.defence)
        return target.health
    def heal(self, target:Self,healing_HP:float)->float:
        target.health += healing_HP
        return target.health

class Player(Entity,storage.Storage):
    def __init__(self, name: str, picture: bytes):
        super().__init__(name, picture)
        self.height:float=2

class AIEntity(Entity):
    def get_to(self,place:tuple)->bool:
        if map.map_now.get_position()==place:
            return True
        return False