# gui_automation

Are you lazy programmer who wants to have GUIs for his apps but does not want to create one for each app individually?
Don't worry so am I. That's why I've spent couple of hours working on automatic GUI generator, instead of creating basic copy-paste GUI in 30 minutes.

The rules are simple:
1. Make one function for each process you want to have.
2. Register this function as `Process` class.
3. Register all instances of `Process` in `App` class instance.
4. Use `app.launch()` and after a little bit of waiting a GUI will pop up!

Is it slow? Perhaps.<br>
Does it work for complex apps? Nope.<br>
Will it fail you once upon a time? Maybe.<br>
Was it "tHorOUgHly TEstEd"? Hell nah. <br>
Is it easy to use? Can it gather all your small scripts in one elegant GUI? Will it save you from going insane while trying to center a div? Very much yes, sir!<br>

## How to...
### ... create App?
```python
app = App()
# or
app = App(
    name="my awesome app",
    version="2.1.37",
    description="This is my app, like for real dude man.",
    path="some/where"  # where to generate GUI.html file
)
```
### ... add Process?
```python
def my_func():
    """
    You will see this is GUI.
    """
    pass

proc = Process(my_func)
# or
proc = Process(
    function=my_func,
    name="my awesome process",
    version="1.0.0",
    description="It does stuff.",
)
# and then
app.add_process(proc)
```
### ... hint types for Process?
```python
def sample_function(
    a1: int,
    a2: float,
    a3: str,
    a4: bool,
    # more will be added later
)
```

### ... add custom massages in Process?
It might be stupid but you can create custom messages in process by turning it into generator function like this:
```python
def f_with_messages():
    # do some stuff
    x = 1
    yield f'the value of x is {x}'
    sleep(15)  # very time consuming process
    yield 'That was a lot of work.'
    yield f'Anyway that\'s the result: {x + 1}'
```

### ... launch App?
```python
app.launch()
```
