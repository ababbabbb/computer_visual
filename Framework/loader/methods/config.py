import yaml


def config_normal(instance_fk, path_config_app):
    with open(path_config_app) as file_config:
        content = yaml.safe_load(file_config)

    instance_fk.type_work = content['App']['type_work']
    instance_fk.debug = content['App']['debug']

    # TODO: 目前到了读取对象(包括数据对象及客体对象)的时候，可以想到的有：
    #  1、数据对象需要和客体对象的创建过程进行区别(应该使用分派处理)；
    #  2、对象的管理应该精细化，至少可以做到针对每一个对象使用同样的接口注解与记录，同时不混淆，
    #   这可能会与将runner看作代理的设计相冲突

    # TODO:使用runner——》
    #            由于本实现在loader内部完成，故此过程由loader规则方法操作runner进行
    instance_fk.config_info_runner(content['App']['  data_source'], content['App']['  objects'])
