import json
import collections


def ClassFactory(name, l):
    def default(self, obj):
        for cls, f in l:
            if isinstance(obj, cls):
                return f(obj)
        return json.JSONEncoder.default(self, obj)
    newclass = type(name, (json.JSONEncoder,), {"default": default})
    return newclass


class Moarjson(object):
    def __init__(self, name):
        self.name = name
        self.l = []

    def _register(self, cls, f):
        for index, i in enumerate(self.l):
            cls2, f2 = i
            if issubclass(cls, cls2):
                self.l.insert(index, (cls, f,))
                break
        else:
            self.l.append((cls, f,))
        return f

    def register(self, cls, f=None):
        def outer_wrapper(f):
            self._register(cls, f)
            return f
        if f:
            return outer_wrapper(f)
        return outer_wrapper

    def register_with_fields(self, cls, fields):
        @self.register(cls)
        def convert(obj):
            d = {}
            for field in fields:
                attr = getattr(obj, field)
                # Convert get value of callables
                d[field] = attr() if isinstance(attr, collections.Callable) else attr
            return d

    def __call__(self, *args, **kwargs):
        return ClassFactory(self.name, self.l)(*args, **kwargs)

    def dumps(self, *args, **kwargs):
        return json.dumps(*args, cls=self, **kwargs)

    def dump(self, *args, **kwargs):
        return json.dump(*args, cls=self, **kwargs)

    def loads(self, *args, **kwargs):
        return json.loads(*args, **kwargs)

    def load(self, *args, **kwargs):
        return json.load(*args, **kwargs)
