from .basic import DataInterface, DataSuper


class Data1(DataSuper, DataInterface):
    def __init__(self, *args, **kwargs):
        ...

    def func_example(self, *args, **kwargs):
        pass
