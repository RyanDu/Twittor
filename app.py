from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Ryan"
    rows = [
        {'name':'Alice','age':'16'},
        {'name':'Alice','age':'16'},
        {'name':'Alice','age':'16'},
        {'name':'Alice','age':'16'},
        {'name':'Alice','age':'16'},
        {'name':'Alice','age':'16'},
        {'name':'Alice','age':'16'}
    ]
    return render_template("index.html",name=name,rows=rows)


if __name__ == "_main_":
    app.run(host='0.0.0.0')