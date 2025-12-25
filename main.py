from flask import Flask, render_template, request, redirect, url_for
from db import addtask, getTaskList
app = Flask(__name__)



@app.route("/")
def home():
    tasklist= getTaskList()
    return render_template("index.html", TaskList=tasklist)

@app.route("/add", methods=["POST"])
def add():
    taskname=request.form['task_name']
    due_date=request.form['due_date']
    addtask(taskname, due_date)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
