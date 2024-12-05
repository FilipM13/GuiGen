from typing import Callable
import inspect
from itertools import zip_longest
from typing import Any

from .argument import Argument

class Process:
    
    def __init__(self, function: Callable, name: str = None, version: str = None, description: str = None) -> None:
        spec = inspect.getfullargspec(function)
        
        self.function = function
        self.name = name if name else function.__name__
        self.pretty_name = self.name.replace('_', ' ').title()
        self.version = version
        self.description = description if description else inspect.getdoc(function)
        self.args = dict()
        
        if spec.args:
            defaults = spec.defaults if spec.defaults else list()
            args = reversed(list(zip_longest(
                reversed(spec.args), 
                reversed(defaults), 
                fillvalue=None
            )))
            for name, default in args:
                self.args[name] = Argument(name=name, default=default, arg_type=spec.annotations.get(name))
        pass
    
    def run(self, args: list[tuple[str, Any]]):
        kwargs = {a[0].removeprefix(f'{self.function.__name__}_'): a[1] for a in args}
        kwargs = {n: self.args[n].type_value(v) for n, v in kwargs.items()}
        rv = self.function(**kwargs)
        return rv
