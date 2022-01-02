import components.Component as comp

class entity:
    """This is an example of a documentation string lateral access through __doc__"""
    # class attribute
    # accessed through __class__
    type = "entity"

    #instance attribute
    def __init__(self, name, life) -> None:
        self.name = name
        self.__life = life
        self.components = []

    def deductHealth(self, deduction) -> None:
        self.__life -= deduction

    def getHealth(self) -> float: # the -> operator means that the function is expecting a float return type
        return self.__life

    def addComponent(self, component: comp) -> None:
        self.components.append(component)
        component.SetOwner(self)

    def getComponentCount(self) -> int:
        return len(self.components)
