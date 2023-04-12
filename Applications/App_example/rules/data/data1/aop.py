from Framework import InterfaceMeta


class _Aop:
    names_interface = [
        'func_example'
    ]

    class _FuncExample:

        @staticmethod
        def before(self, *args, **kwargs):
            ...

        @staticmethod
        def arbiter_around(self, *args, **kwargs) -> bool:
            ...

        @staticmethod
        def around(self, *args, **kwargs):
            ...

        @staticmethod
        def after(self, *args, **kwargs):
            ...

        @staticmethod
        def after_throwing(e, self, *args, **kwargs):
            ...


class DataInterfaceMeta(InterfaceMeta):
    aop_this = _Aop


__all__ = [
    'DataInterfaceMeta'
]
