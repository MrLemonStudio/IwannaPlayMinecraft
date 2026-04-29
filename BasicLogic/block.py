class Block:
    def __init__(self,name:str,picture:bytes,length:float=1,height:float=1):
        self.name = name
        self.picture = picture
        self.length = length
        self.height = height