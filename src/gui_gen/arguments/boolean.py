from .generic import Argument


class Boolean(Argument):
    maps_to = bool
    template_html = "templates/Boolean.jinja2"

    def __init__(self, name, default):
        self.checked = default
        default = False
        super().__init__(name, default)
