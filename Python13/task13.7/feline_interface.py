from abc import ABC, abstractmethod


class FelineInterface(ABC):
    @abstractmethod
    def purr(self):
        pass

    @abstractmethod
    def scratch(self):
        pass
