from abc import ABC, abstractmethod


class Expression(ABC):

    def __init__(self, value):
        self.value = int(value)

    @abstractmethod
    def interpret(self):
        pass

