from .loader.paser_config import Loader
from .actuator.runner import Runner
from Framework.actuator.meta_aop import InterfaceMeta


class FK:
    def __init__(self, name_app: str):
        self.app = name_app
        self._config = Loader(self)
        self._runner = Runner(self)

        self.type_work = None
        self.debug = True

        self.temp_object = {}
        self.temp_component = {}

    def config(self, path_config_app):
        self._config.config(path_config_app)

    def config_info_runner(self, info_data, info_objs):
        self._runner.insert_info_data(info_data)
        self._runner.insert_info_objects(info_objs)

    def run(self):
        ...


__all__ = [
    'FK',
    'InterfaceMeta'
]
