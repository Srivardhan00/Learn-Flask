# Flask Basic Setup and Routing Tutorial

## Overview

This tutorial covers how to set up a basic Flask application, use multiple routes, handle path parameters, and specify parameter types.

## Setting Up a Virtual Environment

### Why Use a Virtual Environment?

A virtual environment is used to create an isolated Python environment for the project, allowing for better dependency management and preventing version conflicts with globally installed packages.

### Steps to Set Up

1. **Create a Virtual Environment**:
   ```bash
   python -m venv <Directory Name>
   ```
2. **Activate the Virtual Environment**:
   ```bash
   # Windows
   <Directory Name>\Scripts\activate
   ```
3. **Deactivate the Virtual Environment**:
   ```bash
   deactivate
   ```

## Initializing a Flask App

### Basic Flask Setup

```python
from flask import Flask
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)
```

### Setting the Home Page with Multiple Routes

```python
@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to home page</h1>"
```

### Handling Path Parameters

- Path parameters let you capture values from the URL and use them in the function.
- **Note**: Avoid reusing function names for different routes.

```python
@app.route("/place/<location>")
def located(location):
    return f"It is {location}"
```

**Specifying Types of Parameters**

- By default, path parameters are treated as strings. You can specify types (e.g., `int`) for validation.

```python
@app.route("/number/<int:num>")
def numberCheck(num):
    return f"{num} is gt 100" if num > 100 else f"{num} is lt or eq to 100"
```

### Using Multiple Parameters

- You can pass multiple parameters in the URL and handle them in your route function.

```python
@app.route("/add/<int:num1>/<int:num2>")
def addNumbers(num1, num2):
    return f"<h3>Sum is {num1 + num2}</h3>"
```
### URL Redirection
- We use redirect method from flask to redirect from 1 page to another
```python
from flask import Flask, redirect

@app.route("/student/pass")
def passed():
    return f"<h1>You have passed the exam</h1>"

@app.route("/student/fail")
def failed():
    return f"<h1>You have failed the exam</h1>"

@app.route("/check/<int:num>")
def check(num):
    if num >= 35:
        return redirect('http://127.0.0.1:5000/student/pass')
    else:
        return redirect('http://127.0.0.1:5000/student/fail')
```
### Using url_for method in redirection
- Generate a URL to the given endpoint with the given values.
- Here the endpoint passed is the function for which url_for provides the respective url.
```python
from flask import Flask, redirect, url_for
@app.route("/check/<int:num>")
def check(num):
    if num>=35:
        return redirect(url_for("passed"))
    return redirect(url_for("failed"))
```

### Passing parameters through url_for
```python
@app.route("/pass/<name>/<int:marks>")
def passed(name, marks):
    return f"{name.title()} passed with {marks} marks"

@app.route("/fail/<name>/<int:marks>")
def failed(name, marks):
    return f"{name.title()} failed with {marks} marks"

@app.route("/check/<name>/<int:num>")
def check(name, num):
    if num>=35:
        return redirect(url_for("passed", name= name,marks= num))
    return redirect(url_for("failed", name= name,marks= num))
```
## Additional Best Practices

- **HTML in Routes**: For larger projects, use templates instead of hard-coding HTML in route functions.
- **Error Handling**: Implement proper error handling using Flask's `@app.errorhandler`.
- **Security**: Never use `debug=True` in a production environment, as it can expose sensitive information.
