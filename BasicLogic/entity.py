class Mob:
    def __init__(self, name:str, picture:bytes, health:float=20, damage:float=0, length:float=1, height:float=1,can_tame:bool=False):
        self.name = name
        self.health = health
        self.damage = damage
        self.length = length
        self.height = height
        self.picture = picture
        self.can_tame = can_tame