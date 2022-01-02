import objects.entity as entity


class Component:
    def __init__(self) -> None:
        self.owner = None

    def SetOwner(self, pOwner: entity) -> None:
        self.owner = pOwner
        print("Owner set to component...")

    def GetOwner(self) -> entity:
        return self.owner
