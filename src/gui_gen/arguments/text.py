from .generic import Argument
import re


class TextBox(Argument):
    template_html = "templates/TextBox.jinja2"


class Regex(TextBox):
    pattern = r".*"

    def map(self, value):
        assert re.fullmatch(self.pattern, value)
        return super().map(value)
