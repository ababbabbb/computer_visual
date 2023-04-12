from abc import abstractmethod

from .aop import DataInterfaceMeta


class DataInterface(metaclass=DataInterfaceMeta):

    @abstractmethod
    def func_example(self, *args, **kwargs):
        ...


class DataSuper:

    ...
