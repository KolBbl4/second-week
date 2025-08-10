class DataBase:
    stingConnect = ''
    typeDataBasle = ''
    def __init__(self, stingConnect:str, typeDataBasle:str ):
        
        self.stingConnect = stingConnect
        self.typeDataBasle = typeDataBasle

    def selevrData(self):
        conectDb = self.stingConnect
        result = "SELECT * FROM USER"


class Users:
    name = ''
    age = ''
    secondName = ''
    def __init__(self,name:str,age:int, secondName:str):
        self.name = name
        self.age = age 
        self.secondName = secondName

