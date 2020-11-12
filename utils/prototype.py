from abc import ABCMeta, abstractmethod
import copy


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def setSize(self, x):
        pass

    @abstractmethod
    def printSize():
        pass


class A(Prototype):
    def __init__(self, size):
        self.__size = size

    def clone(self):
        return copy.deepcopy(self)

    def setSize(self, size):
        self.__size = size

    def printSize(self):
        print("Size: " + str(self.__size))
