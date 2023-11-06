from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import  UserMixin,current_user
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Length



app = Flask(__name__)
app.config['SECRET_KEY'] ='my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_registration.db'
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)

with app.app_context():
    db.create_all()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])

@app.route('/users')
def display_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email= form.email.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created')
        return redirect(url_for('display_users'))
    return render_template('register.html', form=form)



if __name__=='__main__':
    app.run(debug=True)






