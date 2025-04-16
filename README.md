# GUI Generator

Are you lazy programmer who wants to have GUIs for his apps but does not want to create one for each app individually?
Don't worry so am I. That's why I've spent couple of hours working on automatic GUI generator, instead of creating basic copy-paste GUI in 30 minutes.

The rules are simple:
1. Make one function for each process you want to have.
2. Register this function as `Process` class.
3. Register all instances of `Process` in `App` class instance.
4. Use `app.build()` and after a little bit of waiting a GUI will pop up!

Is it slow? Perhaps.<br>
Does it work for complex apps? Nope.<br>
Will it fail you once upon a time? Maybe.<br>
Was it "tHorOUgHly TEstEd"? Hell nah. <br>
Is it easy to use? Can it gather all your small scripts in one elegant GUI? Will it save you from going insane while trying to center a div? Very much yes, sir!<br>

## Example use case 1
```python
from gui_gen import App, Process, arguments
from time import sleep
from datetime import datetime


def my_proc(
    a1: arguments.Argument,
    a2: arguments.Float,
    a3: arguments.Int,
    a4 = 1
):
    sleep(10)
    return datetime.now()

pr = Process(
    my_proc
)

class CustomRegex(arguments.Regex):
    pattern = r'[\d]*'

def my_proc2(
    a1: arguments.Argument,
    a2: arguments.Float,
    text: CustomRegex,
    ch1: arguments.Choice,
    ch2: arguments.Choice = [1, 2, 3],
    d: arguments.Date = datetime(2021, 3, 7).date(),
    dt: arguments.DateTime = datetime(2021, 1, 12, 10, 21),
    a3: arguments.Int = 2,
    a4: arguments.Boolean = False,
    a5: arguments.Boolean = True
):
    '''
    stuff
    '''
    print(ch1)
    print(ch2)
    return datetime.now()

pr2 = Process(
    my_proc2,
    name='Custom name!'
)

a = App(
    processes=[pr, pr2],
    primary_colour='navy',
    secondary_colour='darkgray',
    accent_colour='lime',
    background_colour='black'
)

a.build()
a.launch()
```

### HTML:
[Preview](https://html-preview.github.io/?url=https://github.com/FilipM13/GuiGen/blob/main/readme_data/GUI.html)<br>
[File itself](https://github.com/FilipM13/GuiGen/blob/main/readme_data/GUI.html)

## Example use case 2 (creating custom jinja template)
Python:
```
from gui_gen import App, Process, arguments
from datetime import datetime

class CustomRegex(arguments.Regex):
    pattern = r'[\d]*'
    template_html = 'CustomRegex.jinja2'  # path must be in the same location as class definition:
    # folder/
    #    my_code_with_class.py  # <- template_html = 'template.jinja2'
    #    template.jinja2
    # or
    # folder/
    #    my_code_with_class.py  # <- template_html = 'stuff/template.jinja2'
    #    stuff/
    #       template.jinja2

def my_proc2(
    text: CustomRegex,
    ch1: arguments.Choice = [1,2,3,4],
):
    '''
    stuff
    '''
    return datetime.now()

pr2 = Process(
    my_proc2,
    name='Custom name!'
)

a = App(
    processes=[pr2],
    primary_colour='navy',
    secondary_colour='darkgray',
    accent_colour='lime',
    background_colour='black'
)

a.build()
a.launch()
```
Jinja template:
```Jinja
{% extends "templates/generic.jinja2" %}
{% block input %}
<input
name={{argument.name}}
type="text"
placeholder="THIS IS CUSTOMIZATION FOR {{argument.__class__.__name__}}"
>
{% endblock %}
```

### HTML:
[Preview](https://html-preview.github.io/?url=https://github.com/FilipM13/GuiGen/blob/main/readme_data/GUI_2.html)<br>
[File itself](https://github.com/FilipM13/GuiGen/blob/main/readme_data/GUI_2.html)