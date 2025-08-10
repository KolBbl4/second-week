class Paren:
    paramA = ''
    paramB = ''
    def __init__(self, paramA :str, paramB: str):
        self.paramA = paramA
        self.paramB = paramB

    def parenFunc ():
        print ("Paren")


class Children(Paren):
    def __init__(self, paramA, paramB):
        super().__init__(paramA, paramB)
    
    def pr(self):
        print (self.paramA)

