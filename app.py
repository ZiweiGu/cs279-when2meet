from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
 

app = Flask(__name__) # Initiate the web app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # Initiate the database, which is necessary to store data

class User(db.Model):
    '''
    A database model for todo items. Include 7 fields:
    id: Integer, primary field
    name: String, name of the user
    availability_(1-5): Integer, 0 means not available, 1 means maybe, 2 means available
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    availability_1 = db.Column(db.Integer)
    availability_2 = db.Column(db.Integer)
    availability_3 = db.Column(db.Integer)
    availability_4 = db.Column(db.Integer)
    availability_5 = db.Column(db.Integer)

@app.route('/')
def index():
    user_list = User.query.all()
    return render_template('base.html', user_list=user_list)


@app.route('/add', methods=['POST'])
def add():
    user_name = request.form.get("user_name") # Get data from form input
    availability_1 = request.form.get("availability_1")
    availability_2 = request.form.get("availability_2")
    availability_3 = request.form.get("availability_3")
    availability_4 = request.form.get("availability_4")
    availability_5 = request.form.get("availability_5")
    db.session.add(User(name=user_name, availability_1=availability_1, availability_2=availability_2, availability_3=availability_3, availability_4=availability_4, availability_5=availability_5))
    db.session.commit()
    return redirect(url_for("index")) # refresh the page after an addition


if __name__ == "__main__":
    db.drop_all() # Make sure initial db is clean
    db.create_all() # Initialize all tables
    db.session.add(User(name="Alice", availability_1=2, availability_2=2, availability_3=2, availability_4=0, availability_5=0))
    db.session.add(User(name="Bob", availability_1=2, availability_2=1, availability_3=0, availability_4=2, availability_5=2))
    db.session.add(User(name="Claire", availability_1=2, availability_2=0, availability_3=1, availability_4=1, availability_5=2))
    db.session.commit()
    app.run()