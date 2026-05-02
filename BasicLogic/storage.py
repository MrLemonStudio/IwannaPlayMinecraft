class Storage:
    def __init__(self,name:str,picture:bytes):
        self.name = name
        self.picture = picture
        self.size:int = 1