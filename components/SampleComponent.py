from components.Component import Component


class SampleComponent(Component):
    ComponentType = "TST"

    def __init__(self) -> None:
        Component.__init__(self)
        self._samplePrivateMember = ""

    def doSomething(self) -> None:
        print("Sample Component Example")
