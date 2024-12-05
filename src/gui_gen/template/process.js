// function to execute {{process.name}}
function {{process.function.__name__}}(){
    args = [];
    {% for arg in process.args.values() %}
    inp = document.getElementById("{{process.function.__name__}}_{{arg.name}}");
    args.push([
        inp.id,
        {% if arg.html_type == 'checkbox' %}
        inp.checked
        {% else %}
        inp.value
        {% endif %}
    ]);
    {% endfor %}
    table = document.getElementById("orders");
    row = table.insertRow(0);
    c1 = row.insertCell(0);
    c1.innerHTML = "{{process.pretty_name}}";
    c2 = row.insertCell(1);
    _a = [];
    for(const a of args){
        _a.push(`${a[0]}: ${a[1]}`);
    }
    _a = _a.join('<br>')
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
        app="{{app.__id__}}",
        process="{{process.function.__name__}}",
        args=args
    )();  
};
