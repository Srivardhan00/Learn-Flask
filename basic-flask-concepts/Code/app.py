from flask import Flask, redirect, url_for

# Create an instance of the Flask class
app = Flask(__name__)  # __name__ ensures that the app runs in the current module

@app.route('/')
@app.route('/home')
def home():
    # Return a simple HTML response
    return "<h1>Welcome to home page</h1>"

@app.route("/place/<location>")
def located(location):
    # Capture a string parameter from the URL
    return f"It is {location}"

@app.route("/number/<int:num>")
def numberCheck(num):
    # Check if the integer is greater than 100
    return f"{num} is gt 100" if num > 100 else f"{num} is lt or eq to 100"

@app.route("/add/<int:num1>/<int:num2>")
def addNumbers(num1, num2):
    # Return the sum of the two numbers
    return f"<h3>Sum is {num1 + num2}</h3>"

# with parameters 

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

# without url_for

# @app.route("/student/pass")
# def passed():
#     return f"<h1>You have passed the exam</h1>"

# @app.route("/student/fail")
# def failed():
#   return f"<h1>You have failed the exam</h1>"

# @app.route("/check/<int:num>")
# def check(num):
#     if num >= 35:
#         return redirect('http://127.0.0.1:5000/student/pass')
#     else:
#         return redirect('http://127.0.0.1:5000/student/fail')

# with url_for

# @app.route("/check/<int:num>")
# def check(num):
#     if num>=35:
#         return redirect(url_for("passed"))
#     return redirect(url_for("failed"))

if __name__ == "__main__":
    # Start the Flask app in debug mode to enable hot-reloading
    app.run(debug=True)  # Do not use debug=True in production
