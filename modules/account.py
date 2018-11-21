from abc import ABC, abstractmethod, abstractproperty
balance = [0]


class Account(ABC):
    @abstractproperty
    def prompt(self):
        pass

    @classmethod
    @abstractmethod
    def transact(cls):
        pass
