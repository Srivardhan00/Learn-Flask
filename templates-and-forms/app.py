from flask import Flask, render_template
from emp_data import employees_data

# We pass another variable template_folder, which is "templates" by default
app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html")

@app.route('/')
def home():
    return render_template("home.html", day = 7)

@app.route("/child1")
def child1():
    return render_template("child1.html", title="Child 1")

@app.route("/eval/<int:num>")
def eval(num):
    return render_template("child2.html", title="Evaluator", num = num)

@app.route("/emps")
def employees():
    return render_template("employees.html", title="Employees", info=employees_data)

@app.route("/emps/<position>")
def employees_filtered(position):
    return render_template("employees_filtered.html", title="Employees", info=employees_data, position=position)


if __name__ =="__main__":
    app.run(debug=True)