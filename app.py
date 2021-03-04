from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True)
    email=db.Column(db.String(80),unique=True)

    def __repr__(self) -> str:

        return self



@app.route("/")
def home():

    user1=User(username="Jamshid",email="t1@gmail.com")
    user2=User(username="sherzod",email="t2@gmail.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    return "hello"

@app.route("/read")
def read():

    users=User.query.all()
    return f"{users[0].username}"


if __name__=="__main__":
    app.run(debug=True)