import eel
import easygui  # type: ignore[import-untyped]

from gui_gen.process.process import Process


# expose ordering job
@eel.expose
def request_process(name, args):
    process = Process[name]
    process.execute_process(args)


# getting path to file
@eel.expose
def select_file():
    path = easygui.fileopenbox()
    return path
