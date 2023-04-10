# runner对象是代理工厂，其被注入的规则应当侧重切面编程的实现，即注解/装饰器功能的提供
#            runner是一个创建对象代理的工厂——》
#            该工厂包裹的是对象的代理——》
#            该代理后续可作为切面编程为对象创建前后钩子方法——》
#            runner的外部主要使用方式还是在object、datasource(custom)文件中做切面注解——》
#            内部则在扮演创建工厂时构建对象与runner的联系，为外部注解提供基础——》
#            注意：外部使用时，是直接将runner实例化后到外部使用的（类装饰器形式）//参考flask上下文
# TODO: 切面编程目前考虑使用规则注入的方式实现 ->
#             目前想到的是将函数转为实例方法(types方案)去实现工厂注入代理规则(代理针对接口的装饰器函数)
from Framework.agree import AgreeMeta
from Framework.actuator.runner.container import DataContainer, ObjectContainer
from . import methods


class Runner(metaclass=AgreeMeta):      # TODO: 侧重工厂作用
    # TODO: 需要存在对象的存储映射-> Container对象即为映射容器
    def __init__(self, fk):
        self.fk = fk

        self._container_data = DataContainer()
        self._container_objs = ObjectContainer()

    def insert_info_data(self, info_data):
        getattr(methods, 'insert_info_data')(self._container_data, info_data)

    def insert_info_objects(self, info_objs):
        getattr(methods, 'insert_info_objects')(self._container_objs, info_objs)

    def objects_create(self, *args, **kwargs):
        # TODO：使用types.methodtype方法对代理进行装饰器函数绑定
        # TODO: 懒加载——除非获取对象时否则不创建对象
        # TODO: 这个时候再使用代理
        # TODO：需要声明的是，客体对象及数据源对象的规则描述文件本身就是个类文件
        ...
