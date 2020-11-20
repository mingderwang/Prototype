from abc import ABCMeta, abstractmethod
import copy


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def setSize(self, x) -> None:
        pass

    @abstractmethod
    def printSize() -> None:
        pass


class A(Prototype):
    def __init__(self, size: int) -> None:
        self.__size = size

    def clone(self) -> Prototype:
        return copy.deepcopy(self)

    def setSize(self, size) -> None:
        self.__size = size

    def printSize(self) -> None:
        print("Size: " + str(self.__size))
