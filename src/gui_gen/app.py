from jinja2 import Environment, FileSystemLoader
import os
import eel
import template
from typing import Any
import traceback
from datetime import datetime
import inspect
from bs4 import BeautifulSoup as bs

from .process import Process


TEMPLATE = os.sep.join(template.__file__.split(os.sep)[0:-1])


class App:
    apps = dict()
    
    def __init__(self, name: str = None, version: str = None, description: str = None, path: str = '.'):
        self.name = name
        self.version = version
        self.description = description
        self.processes = list()
        self.path = path
        self.__id__ = str(id(self))
        self.apps[self.__id__] = self
    
    def add_process(self, process: Process):
        self.processes.append(process)
    
    def generate_gui(self):
        context = {
            "app": self
        }
        env = Environment(loader=FileSystemLoader(TEMPLATE))
        base = env.get_template('base.html')
        with open(os.sep.join([self.path, 'GUI.html']), 'w') as gui:
            soup = bs(base.render(context))
            prettyHTML = soup.prettify()
            gui.write(prettyHTML)
        pass
    
    def launch(self):
        self.generate_gui()
        eel.init(self.path)
        eel.start('GUI.html')
        pass


@eel.expose
def order_process(
    app: str,
    process: str,
    args: list[tuple[str, Any]]
):
    app = App.apps[app]
    processes = list(filter(lambda p: p.function.__name__==process, app.processes))
    try:
        assert len(processes) > 0, f"Process {process} not found."
        assert len(processes) < 2, f"Too many processes ({len(processes)}) found for {process}."
        process = processes[0]
        eel.receive_msg(
            process.name, 
            datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
            f'Starting with arguments: {args}'
        )
        rv = process.run(args)
        if rv:
            if inspect.isgenerator(rv):
                for rv_n in rv:
                    eel.receive_msg(
                        process.name, 
                        datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
                        str(rv_n)
                    )
            else:
                eel.receive_msg(
                    process.name, 
                    datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
                    str(rv)
                )
        eel.receive_msg(
            process.name, 
            datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
            'Done!'
        )
    except Exception as e:
        rv = f'Exception in process {process}: {e}.\n{traceback.format_exc()}'
        print(rv)
        eel.receive_msg(
            process.name, 
            datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
            str(rv)
        )
