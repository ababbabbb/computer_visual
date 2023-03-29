from .loader.paser_config import Loader


class FK:
    def __init__(self, name_app: str):
        self.app = name_app
        self._config = Loader(self)

        self.type_work = None
        self.debug = True

        self.temp_object = {}
        self.temp_component = {}

    def config(self, path_config_app):
        self._config.config(path_config_app)

    def run(self):
        ...
