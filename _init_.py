
from flask import Flask, render_template
#this is what is needed for the app

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/affiliates/")
def affiliates():
    return render_template("affiliates.html")

@app.route("/volunteerism/")
def volunteerism():
    return render_template("volunteerism.html")
    
@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/alumap/")
def alumap():
    return render_template("alumap.html")

@app.route("/error404/")
def error404():
    return render_template("error404.html")






if __name__ == "__main__":
    app.run(debug=True)
