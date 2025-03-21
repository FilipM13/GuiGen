import inspect
from itertools import zip_longest
from collections.abc import Callable

from gui_gen.arguments.meta import MetaArg
from gui_gen.arguments.generic import Argument


class Process:
    template_html = 'templates/process.jinja2'

    def __init__(self, func: Callable, name = None, doc = None):
        self.func = func
        self.args: dict[str, MetaArg] = dict()
        self.name = name if name else func.__name__
        self.doc = doc if doc else func.__doc__
        self.read_function()
        print(f'Process {self.name} registered successfully.')

    def read_function(self):
        spec = inspect.getfullargspec(self.func)
        if spec.args:
            defaults = spec.defaults if spec.defaults else list()
            args = reversed(list(zip_longest(
                reversed(spec.args), 
                reversed(defaults), 
                fillvalue=None
            )))
            for name, default in args:
                type_hint = spec.annotations.get(name)
                self.args[name] = (
                    type_hint if type_hint else Argument, 
                    default
                )
        pass

    def execute_process(self, args):
        values = dict()
        for name, val in args.items():
            values[name] = self.args[name][0].map(val)
        rv = self.func(**values)
        return rv
