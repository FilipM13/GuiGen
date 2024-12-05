from process import Process
from jinja2 import Environment, FileSystemLoader
import os
import eel
import template
from typing import Any
import traceback
from datetime import datetime
from time import sleep
import inspect

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
            gui.write(base.render(context))
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


if __name__ == '__main__':
    # example

    def function_one():
        '''
        Function one is doing some stuff for 15 seconds.
        '''
        sleep(15)
        return 'Should sleep for 15s.'

    def function_two(a: int = 123):
        """
        Takes some argument and print it's value in cmd + returns it.
        """
        print(a)
        return f'The value is {a}'

    def function_three(blabla: str = 'test'):
        """
        It's actually generator function that returns 5 values, each one after 2 seconds.
        """
        for i in range(5):
            sleep(2)
            yield f"{i} and {blabla}"

    def function_four(complex_name: str, b: bool = True):
        """
        This one has checkbox and complex_name as argument (to be formatted).
        Also has version.
        """
        b = "not " if not b else ""
        return f'You have {b}checked the box.'
    
    def stupid_process():
        """
        This process is using yield values as messages... what a stupid idea... I like it.
        """
        sleep(2)
        yield "waited 2s"
        sleep(10)
        yield "waited 10s... like I'm working on something"
        sleep(5)
        yield "yay process done, this is final message"

    app = App()
    app.add_process(Process(function_one))
    app.add_process(Process(function_two, name='this name overwrites function name function_two'))
    app.add_process(Process(function_three, description='This description overwrites docstring of function.'))
    app.add_process(Process(function_four, version="1.0.3"))
    app.add_process(Process(stupid_process, version="96"))

    app.launch()
