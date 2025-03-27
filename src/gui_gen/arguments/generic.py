from gui_gen.meta.meta import MetaArg


class Argument(metaclass=MetaArg):
    maps_to = str
    template_html = "templates/generic.jinja2"

    def __init__(self, name, default):
        self.name = name
        self.default = default

    def map(self, value):
        try:
            return self.maps_to(value)
        except Exception as e:
            return self.default
