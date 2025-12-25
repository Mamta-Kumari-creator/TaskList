from flask import Flask, render_template

app = Flask(__name__)

tasklist=[["clean room",False],["do laundry",True],["write code",False]]

@app.route("/")
def home():
    return render_template("index.html", TaskList=tasklist)

if __name__ == "__main__":
    app.run(debug=True)
