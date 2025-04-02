from .generic import Argument


class Int(Argument):
    maps_to: type = int
    template_html = "templates/Int.jinja2"


class Float(Argument):
    template_html = "templates/Float.jinja2"
    maps_to: type = float
