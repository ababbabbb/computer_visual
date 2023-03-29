import yaml

from Framework.agree import AgreeMeta


class Loader(metaclass=AgreeMeta):
    def __init__(self, fk=None):
        self.fk = fk

    def init_fk(self, fk):
        self.fk = fk

    def config(self, path_config_app):
        with open(path_config_app) as file_config:
            content = yaml.safe_load(file_config)

        self.fk.type_work = content['App']['type_work']
        self.fk.debug = content['App']['debug']

        # TODO:创建对象——》
        #            使用runner——》
        #            runner是一个创建对象的工厂——》
        #            该工厂创建的是包裹对象的代理——》
        #            该代理后续可作为切面编程为对象创建前后钩子方法——》
        #            由于本实现在loader内部完成，故此过程由loader规则方法操作runner进行
