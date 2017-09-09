from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost/mydatabase/flasktest'
db = SQLAlchemy(app)

admin = Admin(app)

class User(db.ModeL):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique = True)
	
	def __init__(self, username, email):
		self.username = username
		self.email = email
	
	def __repr__(self):
		return '<User %r>' % self.username

admin.add_view(ModelView(Person, db.session))
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

@app.route("/rtwmaps/")
def rtwmaps():
    return render_template("rtwmaps.html")






if __name__ == "__main__":
    app.run(debug=True)
