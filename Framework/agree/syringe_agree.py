

class _Syringe:
    @staticmethod
    def _injection_component(attrs):
        
        return attrs

    @staticmethod
    def _injection_lib(attrs):

        return attrs
    
    @staticmethod
    def _injection_loader(attrs):

        return attrs
    
    @staticmethod
    def _injection_logger(attrs):

        return attrs
    
    @staticmethod
    def _injection_monitor(attrs):

        return attrs
    
    @staticmethod
    def _injection_runner(attrs):

        return attrs
    
    @staticmethod
    def _injection_test(attrs):

        return attrs


def _injection(name_cls: str, attrs):
    """
    本函数起到的作用为分派，将参数依照name_cls传入到获取的不同静态方法中
    :param name_cls: 类名称
    :param instance_cls: 类
    :return: 元类的实例对象——类
    """

    return getattr(_Syringe, '_injection_' + name_cls.lower())(attrs)


class AgreeMeta(type):
    """
        本元类创建的目的是为了向各大类中注入规则

    """ 

    def __new__(mcs, name, bases, attrs):
        attrs["_instance"] = None

        return super().__new__(mcs, name, bases, _injection(name, attrs))

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)

        return self._instance
