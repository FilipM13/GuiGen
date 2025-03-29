from .generic import Argument


class File(Argument):
    maps_to = str
    template_html = "templates/File.jinja2"
