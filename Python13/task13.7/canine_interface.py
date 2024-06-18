from abc import ABC, abstractmethod


class CanineInterface(ABC):
    @abstractmethod
    def bark(self):
        pass

    @abstractmethod
    def fetch(self):
        pass
