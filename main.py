import math
import sys # system module where you can import python system functions
import imp # importer module that can be used to reload a specific module
import config.config_main as config_main # this custom module only executes only once on import
from objects.entity import entity
from components.sampleComponent import sampleComponent


myEntity = entity("Alson", 100.0)
print (f"Player Health -> {myEntity.getHealth()}")
print (f"Player ComponentCount -> {myEntity.getComponentCount()}")
# adding a sample component
tstComponent = sampleComponent()
myEntity.addComponent(tstComponent)
print (f"Player ComponentCount -> {myEntity.getComponentCount()}")


print (f"{sys.path}")
myList = [1, 2, 3, 4, 5]

for elem in myList:
    print (f"{elem}")

userInput = input("Enter a number: ")

print (f"You entered: {userInput}")

def doSomething(strSomething, intSomething):
    """Something"""
    print ("")
    return strSomething

def somethingToImplement():
    pass

print (doSomething.__doc__)


def greetPeople(*people):
    for person in people:
        print (f"Hell {person}")

greetPeople("Alson", "Ange", "Chippy")

mySampleGlobal = "sample"

def modifyGlobal(strOverride):
    global mySampleGlobal
    mySampleGlobal += strOverride

modifyGlobal("-override")
print (mySampleGlobal)

config_main.cfg_1 = "override-sample_1"
config_main.cfg_2 = "override-sample_2"

print (dir (config_main)) #dir prints out the directory / content of the module