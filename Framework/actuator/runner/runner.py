# runner是对象工厂
#            该工厂包裹的是对象的容器

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
        # TODO: 懒加载——除非获取对象时否则不创建对象
        # TODO：需要声明的是，客体对象及数据源对象的规则描述文件本身就是个类文件
        ...
