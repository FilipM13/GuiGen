from gui_gen.meta.meta import MetaTemplated

class App(metaclass=MetaTemplated):
    template_html = 'templates/app.jinja2'
    template_js = 'templates/app_js.jinja2'

    def __init__(self, processes, name = None, doc = None):
        self.processes = processes
        self.name = name
        self.doc = doc
    
    def build(self):
        pass
