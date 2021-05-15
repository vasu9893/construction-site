from flask import Flask, render_template, request , session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import os
 
app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/m.g.r'
db = SQLAlchemy(app)

           
@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("/portfolio.html")

@app.route("/service")
def service():
    return render_template("/service.html")

class Contacts(db.Model):
    sno = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(15), nullable=False)
    Message = db.Column(db.String(10), nullable=False)
    Subject = db.Column(db.String(15), nullable=False)
    date = db.Column(db.String(150), nullable=True)
    Email = db.Column(db.String(15), nullable=False)

@app.route("/contact" , methods= ['GET','POST'])
def contact():
        if(request.method=='POST'):
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message') 
            subject = request.form.get('subject')
            entry = Contacts(Name=name, Subject= subject ,Message = message, date= datetime.now(),Email = email )
            db.session.add(entry)
            db.session.commit()
        return render_template("/contact.html")


@app.route("/about")
def about():
    return render_template("/about.html")

app.run(debug=True)

