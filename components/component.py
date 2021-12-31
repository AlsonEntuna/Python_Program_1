from objects.entity import entity

class component:
    owner = None

    def __init__(self) -> None:
        pass

    def SetOwner(self, pOwner):
        self.owner = pOwner
        print ("Owner set to component...")

    def GetOwner(self):
        return self.owner