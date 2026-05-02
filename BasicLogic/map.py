import entity
class Map:
    def __init__(self,name:str,overview:str):
        self.name = name
        self.overview = overview
        self.length:float = 1
        self.height:float = 1
    def get_position(self,target:entity.Entity)->tuple:
        return 0,0
map_now=Map("now","")