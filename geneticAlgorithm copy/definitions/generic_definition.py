from abc import ABC, abstractmethod


class GenericDefinition(ABC):

    @abstractmethod
    def cmp(self, a, b):
        return NotImplemented

    @abstractmethod
    def random_define(self):
        return NotImplemented

    @abstractmethod
    def define(self, a):
        return NotImplemented

    @abstractmethod
    def mutate(self, gen):
        return NotImplemented

    @abstractmethod
    def divide(self, elm, n_element):
        return NotImplemented
