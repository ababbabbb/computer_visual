import traceback
from functools import wraps


class InterfaceMeta(type):
    # TODO: 实现切面编程，无需添加到框架内，
    #             该实现通过向类附加接口切面拦截器的方式融入到整个项目
    # TODO: 本实现仅为对接口进行统一编程
    aop_this = None

    def __new__(mcs, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value) and key in mcs.aop_this.names_interface:
                attrs[key] = mcs.aop(value)

        return super().__new__(mcs, name, bases, attrs)

    @classmethod
    def aop(mcs, func):

        return mcs.decorator(mcs, func)

    @staticmethod
    def decorator(cls_used, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            proxy_aop = getattr(cls_used.aop_this, '_' + func.__name__.raplace('_', '').title())
            try:
                proxy_aop.before(*args, **kwargs)
                if proxy_aop.arbiter_around(*args, **kwargs):
                    ret = proxy_aop.around(*args, **kwargs)
                else:
                    ret = func(*args, **kwargs)
                proxy_aop.after(*args, **kwargs)
            except Exception:
                ret = proxy_aop.after_throwing(traceback.format_exc(), *args, **kwargs)

            return ret
        return wrapper
