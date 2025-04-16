from gui_gen.meta.meta import MetaTemplated
import shutil
import os
from jinja2 import Environment, FileSystemLoader
import eel
import bs4


class App(metaclass=MetaTemplated):
    template_html = "templates/app.jinja2"
    template_js = "templates/app_js.jinja2"

    def __init__(
        self,
        processes,
        name=None,
        doc=None,
        font='"Noto Sans Mono", monospace',
        gui_directory="GUI/",
        background_colour="#29335C",
        primary_colour="#E9A437",
        secondary_colour="rgba(255, 235, 205)",
        accent_colour="#DB2B39",
    ):
        self.processes = processes
        self.name = name
        self.doc = doc
        self.gui_directory = gui_directory
        self.background_colour = background_colour
        self.primary_colour = primary_colour
        self.secondary_colour = secondary_colour
        self.accent_colour = accent_colour
        self.font = font

    def build(self):
        # copy all templates to one directory
        for template in MetaTemplated.all_templates:
            # copy html template
            os.makedirs(
                os.path.dirname(self.gui_directory + template.template_html),
                exist_ok=True,
            )
            shutil.copy(
                template.abs_template_html, self.gui_directory + template.template_html
            )
            # copy extra templates
            if hasattr(template, "templates_extra"):
                for ate, te in template.templates_extra:
                    os.makedirs(os.path.dirname(self.gui_directory + te), exist_ok=True)
                    shutil.copy(ate, self.gui_directory + te)

        # generate gui
        environment = Environment(loader=FileSystemLoader(self.gui_directory))
        # html
        template = environment.get_template("templates/__main__.jinja2")
        rendered_gui = template.render(app=self)
        rendered_gui = bs4.BeautifulSoup(rendered_gui, "lxml").prettify()
        with open(self.gui_directory + "GUI.html", "w", encoding="utf-8") as gui:
            gui.write(rendered_gui)
        # css
        template = environment.get_template("templates/style.css")
        rendered_gui = template.render(app=self)
        with open(self.gui_directory + "style.css", "w", encoding="utf-8") as gui:
            gui.write(rendered_gui)

    def launch(self, remove_after_closed: bool = True):
        # run app
        eel.init(self.gui_directory)
        eel.start("GUI.html", mode="default")
        print("app stopped")

        # delete directory
        if remove_after_closed:
            shutil.rmtree(self.gui_directory)
