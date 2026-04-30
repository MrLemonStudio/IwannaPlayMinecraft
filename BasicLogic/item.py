class Item:
    def __init__(self,name:str,picture:bytes,is_tool:bool=False,is_food:bool=False):
        self.name = name
        self.picture = picture
        self.is_tool = is_tool
        self.is_food = is_food