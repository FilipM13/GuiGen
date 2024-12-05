

class Argument:
    
    def __init__(self, name, default, arg_type) -> None:
        self.name = name
        self.pretty_name = self.name.replace('_', ' ').title()
        self.default = default
        self.arg_type = arg_type
    
    @property
    def html_type(self):
        mapping_py_to_html = {
            int: 'number',
            float: 'number',
            str: 'text',
            bool: 'checkbox',
        }
        return mapping_py_to_html.get(self.arg_type, 'text')
    
    def type_value(self, value):
        if value is None:
            return None
        if value == '' and self.arg_type is None:
            return None
        if self.arg_type:
            return self.arg_type(value)
        else:
            return value


class IntArgument(Argument):
    pass


class FloatArgument(Argument):
    pass


class BoolArgument(Argument):
    pass


class StrArgument(Argument):
    pass


class DateArgument(Argument):
    pass


class DateTimeArgument(Argument):
    pass