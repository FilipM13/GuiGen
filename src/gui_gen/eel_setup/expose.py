import eel

from gui_gen.process.process import Process


# expose ordering job
@eel.expose
def request_process(name, args):
    process = Process[name]
    process.execute_process(args)
