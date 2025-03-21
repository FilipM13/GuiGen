from .meta import MetaArg


class Argument(metaclass=MetaArg):
    maps_to = str
    template_html = 'templates/generic.jinja2'
    template_js = 'templates/generic_js.jinja2'

    @classmethod
    def map(cls, value):
        return cls.maps_to(value)
