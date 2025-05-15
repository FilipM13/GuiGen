import inspect
from itertools import zip_longest
from collections.abc import Callable
from typing import Any
import eel
from datetime import datetime

from gui_gen.meta.meta import MetaArg, MetaTemplated
from gui_gen.arguments.generic import Argument


class MappingException(Exception):
    pass


class Process(metaclass=MetaTemplated):
    template_html = "templates/process.jinja2"
    process_registry: dict[str, "Process"] = dict()

    def __init__(self, func: Callable, name=None, doc=None):
        self.func = func
        self.args: dict[str, MetaArg] = dict()
        self.name = name if name else func.__name__
        self.doc = doc if doc else func.__doc__
        self.read_function()
        self.process_registry[self.func.__name__] = self
        print(f"Process {self.name} registered successfully.")

    def read_function(self):
        spec = inspect.getfullargspec(self.func)
        if spec.args:
            defaults = spec.defaults if spec.defaults else list()
            args = reversed(
                list(
                    zip_longest(reversed(spec.args), reversed(defaults), fillvalue=None)
                )
            )
            for name, default in args:
                type_hint = spec.annotations.get(name, Argument)
                self.args[name] = type_hint(name=name, default=default)
        pass

    def execute_process(self, args):
        try:
            values = dict()
            spec = inspect.getfullargspec(self.func)
            args = {a["name"]: a["value"] for a in args}
            for name, val in args.items():
                try:
                    values[name] = self.args[name].map(val)
                except:
                    raise MappingException(f"MappingException for {name}: {val}")
            for name in spec.args:
                if name not in args.keys():
                    values[name] = self.args[name].default
            rv = self.func(**values)
        except Exception as e:
            rv = e.__str__()
        eel.receive_msg(
            self.func.__name__, datetime.now().strftime("%Y/%m/%d %H:%M:%S"), str(rv)
        )

    @classmethod
    def __class_getitem__(cls, key):
        return cls.process_registry[key]
