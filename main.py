from flask import Flask, render_template, request, redirect, url_for
from db import addtask, deletetask, getTaskList, updatetask
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

@app.route("/update" , methods=["POST"])
def update():
    updatedtaskname=request.form['updateTask']
    id=request.form['id']
    button=request.form["save_or_delete"]
    if button=="save":
        updatetask(updatedtaskname, id)
    elif button=="delete":
        deletetask(id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
