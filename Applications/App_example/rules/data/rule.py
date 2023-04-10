from Framework.template import Data


class Data1(Data):
    class _Interface:
        def func_1(self, *args, **kwargs):
            ...

    def func_1(self, *args, **kwargs):
        ...
