class Mob:
    def __init__(self, name:str, picture:bytes, health:float=20, damage:float=0, length:float=1, height:float=1):
        self.name = name
        self.health = health
        self.damage = damage
        self.length = length
        self.height = height
        self.picture = picture