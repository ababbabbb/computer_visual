from Framework.agree import AgreeMeta
from . import methods


class Loader(metaclass=AgreeMeta):      # TODO： 本对象的设计需要参考flask的上下文进行设计
    def __init__(self, fk=None):
        self.fk = fk

    def init_fk(self, fk):
        self.fk = fk

    def config(self, path_config_app):
        getattr(methods, 'config_normal')(self.fk, path_config_app)
