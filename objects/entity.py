import components.Component as comp

# TODO: change this to proper naming
class entity:
    """This is an example of a documentation string lateral access through __doc__"""
    # class attribute
    # accessed through __class__
    type = "entity"

    #instance attribute
    def __init__(self, name, life) -> None:
        self.name = name
        self._life = life
        self.components = []

    def deductHealth(self, deduction) -> None:
        self.__life -= deduction

    @property
    def life(self) -> float:
        return self._life

    @life.setter
    def life(self, value: float) -> None:
        self._life = float(value)

    def printLife(self) -> None:
        print(f"Current Health {self._life}")

    def addComponent(self, component: comp) -> None:
        self.components.append(component)
        component.SetOwner(self)

    def getComponentCount(self) -> int:
        return len(self.components)
