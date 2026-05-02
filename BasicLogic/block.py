class Block:
    def __init__(self,name:str,picture:bytes):
        self.name = name
        self.picture = picture
        self.length:float = 1
        self.height:float = 1