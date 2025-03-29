from .generic import Argument


class Choice(Argument):
    maps_to = str
    template_html = "templates/Choice.jinja2"

    def get_options(self):
        if self.default:
            return self.default
        else:
            return list()
