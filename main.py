# import math
# import sys  # system module where you can import python system functions
# import imp  # importer module that can be used to reload a specific module

# from app_config import config_main as m_config
# sys.path.append('/../objects')
# sys.path.append('/../app_config')

from objects.entity import entity
from components.SampleComponent import SampleComponent

myEntity = entity("Alson", 100.0)
print(f"Player Health -> {myEntity.life}")
print(f"Player ComponentCount -> {myEntity.getComponentCount()}")
# adding a sample component
tstComponent = SampleComponent()
myEntity.addComponent(tstComponent)
print(f"Player ComponentCount -> {myEntity.getComponentCount()}")
tstComponent.doSomething()

# setting health
myEntity.printLife()
myEntity.life = 200
myEntity.printLife()

# print(f"{sys.path}")
myList = [1, 2, 3, 4, 5]

for elem in myList:
    print(f"{elem}")

userInput = input("Enter a number: ")

print(f"You entered: {userInput}")


def doSomething(strSomething, intSomething):
    """Something"""
    print("")
    return strSomething


def somethingToImplement():
    pass


print(doSomething.__doc__)


# using *args is having no definite number of elements to be passed in as an argument
def greetPeople(*people):
    for person in people:
        print(f"Hell {person}")


greetPeople("Alson", "Ange", "Chippy")

mySampleGlobal = "sample"


def modifyGlobal(strOverride):
    global mySampleGlobal
    mySampleGlobal += strOverride


modifyGlobal("-override")
print(mySampleGlobal)


# m_config.cfg_1 = "override-sample_1"
# m_config.cfg_2 = "override-sample_2"


# print(dir(config_main))  # dir prints out the directory / content of the module

def sample_decorator(func):
    greeting = "Hello"

    def inner_func():
        # implementing other things here alongside the function parameter
        print("Start of inner...")
        # calling the function parameter
        func()
        print("end of inner....")

    return inner_func


# calling with the decorated function
@sample_decorator
def main_sample_func():
    print("main function ->>>>")


main_sample_func()


def main():
    pass


if __name__ == "__main__":
    main()
