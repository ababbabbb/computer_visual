# runner对象是代理，其被注入的规则应当侧重切面编程的实现，即注解/装饰器功能的提供
#            runner是一个创建对象的工厂——》
#            该工厂创建的是包裹对象的代理——》
#            该代理后续可作为切面编程为对象创建前后钩子方法——》
#            runner的外部主要使用方式还是在object、datasource(custom)文件中做切面注解——》
#            内部则在扮演创建工厂时构建对象与runner的联系，为外部注解提供基础
from Framework.agree import AgreeMeta


class Runner(metaclass=AgreeMeta):
    def __init__(self):
        ...
