from abc import ABCMeta, abstractmethod


class Container(metaclass=ABCMeta):

    @abstractmethod
    def config_info(self, *args, **kwargs):
        ...


class DataContainer(Container):

    def config_info(self, *args, **kwargs):
        pass


class ObjectContainer(Container):

    def config_info(self, *args, **kwargs):
        pass


class InterfaceContainer(Container):
    
    def config_info(self, *args, **kwargs):
        pass
