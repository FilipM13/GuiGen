import datetime as dt

from .generic import Argument


class Date(Argument):
    maps_to = dt.date
    template_html = "templates/Date.jinja2"

    def map(self, value):
        rv = dt.datetime.strptime(value, "%Y-%m-%d").date()
        return rv

    def format_default(self):
        return self.default.strftime("%Y-%m-%d")


class DateTime(Argument):
    maps_to = dt.datetime
    template_html = "templates/DateTime.jinja2"

    def map(self, value):
        rv = dt.datetime.strptime(value, "%Y-%m-%dT%H:%M")
        return rv

    def format_default(self):
        return self.default.strftime("%Y-%m-%dT%H:%M")
