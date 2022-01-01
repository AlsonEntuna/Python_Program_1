class component:
    def __init__(self) -> None:
        self.owner = None

    def SetOwner(self, pOwner):
        self.owner = pOwner
        print ("Owner set to component...")

    def GetOwner(self):
        return self.owner