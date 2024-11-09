## Custom Templates

### We use render_template function to render templates based on path which we need, rather than using html in app.py

```python
from flask import render_template
@app.route('/')
def home():
    return render_template("home.html")
```

## Jinja

- We use placeholders with {{ }} in html
- We pass required info as parameters, within render_template function

```python
@app.route('/')
def home():
    return render_template("home.html", day = 7)
```

```html
<h2>This is the home page, and today is {{day}}</h2>
```

## Template Inheritance

#### Key Concepts

1. Base Template: The initial template that defines the structure and blocks ( placeholders ) for child templates to inherit from.
2. Child Template: A template that extends the base template, overriding specific blocks with its own content.
3. Blocks: Named sections in the base template that can be overridden by child templates

#### When you render child1.html, Jinja will:

1. Load the base template (base.html).
2. Override the blocks with the value from child.html.
3. Render the resulting HTML document.

**Parent Layout**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}My App{% endblock %}</title>
  </head>
  <body>
    <h3>This page is {{ title }} page</h3>
    {% block content %} {% endblock content %}
  </body>
</html>
```

- We can change title block, content block at children, and the title is passed through params.
- We should definitely end any block we started, it can be with {% end<> %} or {% end<> `<block name>`}.

**Child Layout**

```html
{% extends "parent.html" %} {% block title %} Child 1 Title {% endblock %} {%
block content %}
<h1>Welcome to child 1</h1>
{% endblock %}
```

## Using Conditional

```html
{% extends "parent.html" %} {% block content %}
<h3>The Entered Number is {{num}}</h3>
<div>
  {% if num==0 %}
  <p>The number is zero</p>
  {% elif num>100 %}
  <p>The number is greater than 100</p>
  {% else %}
  <p>The number is less than or equal to 100</p>
  {% endif %}
</div>
{% endblock %}
```

## Using for loop

```html
<table>
  {% for emp_no, emp_data in info.items() %}
  <tr>
    <td>Name : {{emp_data['name']}}</td>
    <td>Position : {{emp_data['position']}}</td>
    <td>Age : {{emp_data['age']}}</td>
  </tr>
  {% endfor %}
</table>
```


## Handling Multiple Blocks

You can have multiple blocks in a template and override them in child templates as needed.

**Base Template with Multiple Blocks**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Title{% endblock %}</title>
</head>
<body>
    {% block header %}<h1>Default Header</h1>{% endblock %}
    {% block content %}Content goes here{% endblock %}
    {% block footer %}<p>Default Footer</p>{% endblock %}
</body>
</html>
```

**Child Template Overriding Multiple Blocks**

```html
{% extends "base.html" %}

{% block title %}Employees List{% endblock %}
{% block header %}<h2>Employee Directory</h2>{% endblock %}
{% block content %}
<h3>All {{ position.title() }}s</h3>
<table>
    {% for emps, emp_info in info.items() %}
        {% if emp_info['position'].lower() == position.lower() %}
            <tr>
                <td>{{ emp_info['name'] }}</td>
                <td>{{ emp_info['age'] }}</td>
            </tr>
        {% endif %}
    {% endfor %}
</table>
{% endblock %}
```


### Routing in HTML

```html
<ul>
  <li><a href="{{ url_for('child1') }}">Child 1</a></li>
  <li><a href="{{ url_for('eval', num = 0) }}">Evaluate 0</a></li>
</ul>
```
