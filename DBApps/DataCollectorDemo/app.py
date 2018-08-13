from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app=Flask(__name__)
#   app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:atcbtra1@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://joqmajvadzjree:c1bb3208402d2eea8e8ece5745fa89794877a15709495378f5f7763171a96b64@ec2-54-235-94-36.compute-1.amazonaws.com:5432/d1h850607u0cmq?sslmode=require
'

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email=email_
        self.height=height_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email==email).count()==0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height,1)
            print(average_height)
            count=db.session.query(Data.height).count()
            send_email(email,height,average_height,count)
            return render_template("success.html")
    return render_template('index.html',text="Looks like email id already being used.")


if __name__=='__main__':
    app.debug=True
    app.run()
