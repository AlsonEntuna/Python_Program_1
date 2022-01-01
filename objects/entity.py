import components.component

class entity:
    """This is an example of a documentation string lateral access through __doc__"""
    # class attribute
    # accessed through __class__
    type = "entity"

    #instance attribute
    def __init__(self, pName, pLife) -> None:
        self.name = pName
        self.__life = pLife
        self.components = []

    def deductHealth(self, pDeduction) -> None:
        self.__life -= pDeduction

    def getHealth(self) -> float: # the -> operator means that the function is expecting a float return type
        return self.__life

    def addComponent(self, pComponent: components.component) -> None:
        self.components.append(pComponent)
        pComponent.SetOwner(self)

    def getComponentCount(self) -> int:
        return len(self.components)