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
    ):
    pass
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

## Full Example
Python:
```python
from gui_gen import App, Process

def sample_function(
        a1: int,
        a2: float,
        a3: str,
        a4: bool,
        # more will be added later
    ):
    pass

def f_with_messages():
    # do some stuff
    x = 1
    yield f'the value of x is {x}'
    sleep(15)  # very time consuming process
    yield 'That was a lot of work.'
    yield f'Anyway that\'s the result: {x + 1}'

app = App()
app.add_process(Process(sample_function))
app.add_process(Process(f_with_messages))

app.launch()
```

HTML:
```html
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>
 <head>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <title>
   My App
  </title>
  <meta content="" name="description"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link href="" rel="stylesheet"/>
  <script src="/eel.js" type="text/javascript">
  </script>
  <script async="" defer="">
   eel.expose(receive_msg);
            function receive_msg(process, ts, msg){
                output = document.getElementById("output_"+process);
                output.innerHTML += '<span class="timestamp">' + ts + ': </span>' + msg + '<br>';
            }

            
                // function to execute sample_function
function sample_function(){
    args = [];
    
    inp = document.getElementById("sample_function_a1");
    args.push([
        inp.id,
        
        inp.value
        
    ]);
    
    inp = document.getElementById("sample_function_a2");
    args.push([
        inp.id,
        
        inp.value
        
    ]);
    
    inp = document.getElementById("sample_function_a3");
    args.push([
        inp.id,
        
        inp.value
        
    ]);
    
    inp = document.getElementById("sample_function_a4");
    args.push([
        inp.id,
        
        inp.checked
        
    ]);
    
    table = document.getElementById("orders");
    row = table.insertRow(0);
    c1 = row.insertCell(0);
    c1.innerHTML = "Sample Function";
    c2 = row.insertCell(1);
    _a = [];
    for(const a of args){
        _a.push(`"${a[1]}"`);
    }
    c2.innerHTML = _a;
    c3 = row.insertCell(2);
    var now = new Date();
    [y, M, d, h, m, s] = [
        now.getFullYear(),
        now.getMonth(),
        now.getDay(),
        now.getHours(),
        now.getMinutes(),
        now.getSeconds(),
    ];
    c3.innerHTML = `${y}/${M}/${d} ${h}:${m}:${s}`;
    // c3.innerHTML = now.toString();
    eel.order_process(
        app="2229739300992",
        process="sample_function",
        args=args
    )();  
};
            
                // function to execute f_with_messages
function f_with_messages(){
    args = [];
    
    table = document.getElementById("orders");
    row = table.insertRow(0);
    c1 = row.insertCell(0);
    c1.innerHTML = "F With Messages";
    c2 = row.insertCell(1);
    _a = [];
    for(const a of args){
        _a.push(`"${a[1]}"`);
    }
    c2.innerHTML = _a;
    c3 = row.insertCell(2);
    var now = new Date();
    [y, M, d, h, m, s] = [
        now.getFullYear(),
        now.getMonth(),
        now.getDay(),
        now.getHours(),
        now.getMinutes(),
        now.getSeconds(),
    ];
    c3.innerHTML = `${y}/${M}/${d} ${h}:${m}:${s}`;
    // c3.innerHTML = now.toString();
    eel.order_process(
        app="2229739300992",
        process="f_with_messages",
        args=args
    )();  
};
  </script>
  <style>
   /*YES I COULD HAVE USED BOOTSTRAP...*/
:root{
    background-color: #29335C;
    font-family: Arial, sans-serif;
}
.app_name, .order_header{
    color: white;
    text-align: center;
}
.output{
    font-family: "Consolas";
    background-color: rgb(99, 99, 99);
    color: white;
    padding: 5px;
    margin: 5px;
    border-radius: 3px;
}
.timestamp{
    font-weight: lighter;
    color: greenyellow;
}
.process_tab{
    background-color: rgba(255, 235, 205);
    padding: 5px;
    margin: 5px;
}
.process_tab h2{
    background-color: #E9A437;
    color:#DB2B39;
    text-align: center;
}
.process_tab h2 .process_version{
    color:#29335C;
}
.process_tab .run{
    font-weight: bold;
    padding: 2px;
}
.order_table {
    width: 100%;
    border-collapse: collapse;
    background-color: rgba(255, 235, 205, 1); /* Light background color */
    font-size: 14px;
    text-align: left;
}

.order_table th, td {
    border: 1px solid #ccc; /* Light border color for readability */
    padding: 8px;
}

.order_table th {
    background-color: #E9A437; /* Header row color */
    color: #DB2B39; /* Header text color */
    text-transform: uppercase;
}

.order_table tr:nth-child(even) {
    background-color: rgba(255, 235, 205, 0.85); /* Slightly lighter for even rows */
}
  </style>
 </head>
 <body>
  <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="#">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
  <h1 class="app_name">
   My App
  </h1>
  <div class="process_tab">
   <h2>
    Sample Function
   </h2>
   <form>
    <h3>
     Input:
    </h3>
    <label for="sample_function_a1">
     A1
    </label>
    <input id="sample_function_a1" placeholder="&lt;class 'int'&gt; (number)" type="number"/>
    <br/>
    <label for="sample_function_a2">
     A2
    </label>
    <input id="sample_function_a2" placeholder="&lt;class 'float'&gt; (number)" type="number"/>
    <br/>
    <label for="sample_function_a3">
     A3
    </label>
    <input id="sample_function_a3" placeholder="&lt;class 'str'&gt; (text)" type="text"/>
    <br/>
    <label for="sample_function_a4">
     A4
    </label>
    <input id="sample_function_a4" placeholder="&lt;class 'bool'&gt; (checkbox)" type="checkbox"/>
    <br/>
    <input class="run" onclick="sample_function()" type="button" value="Run"/>
   </form>
   <h3>
    Output:
   </h3>
   <p class="output" id="output_sample_function">
   </p>
  </div>
  <div class="process_tab">
   <h2>
    F With Messages
   </h2>
   <form>
    <input class="run" onclick="f_with_messages()" type="button" value="Run"/>
   </form>
   <h3>
    Output:
   </h3>
   <p class="output" id="output_f_with_messages">
   </p>
  </div>
  <h2 class="order_header">
   Ordered jobs
  </h2>
  <table class="order_table">
   <thead>
    <tr>
     <th>
      Job
     </th>
     <th>
      Arguments
     </th>
     <th>
      Time Stamp
     </th>
    </tr>
   </thead>
   <tbody id="orders">
   </tbody>
  </table>
 </body>
</html>
```