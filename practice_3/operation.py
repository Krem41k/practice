from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def get_result(self, a, b):
        pass
