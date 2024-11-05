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

## Additional Best Practices

- **HTML in Routes**: For larger projects, use templates instead of hard-coding HTML in route functions.
- **Error Handling**: Implement proper error handling using Flask's `@app.errorhandler`.
- **Security**: Never use `debug=True` in a production environment, as it can expose sensitive information.
