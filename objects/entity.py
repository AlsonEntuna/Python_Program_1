import components.component


class entity:
    name = ""
    life = 0.0
    components = []

    def __init__(self) -> None:
        pass

    def __init__(self, pName, pLife) -> None:
        pass

    def deductHealth():
        pass

    def addComponent(self, pComponent):
        self.components.append(pComponent)
        component = components.component(pComponent)
        pComponent.SetOwner(self)