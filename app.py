from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

db=SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True)
    email=db.Column(db.String(80),unique=True)




@app.route("/")
def hi():

    return "hello"

if __name__=="__main__":
    app.run(debug=True)