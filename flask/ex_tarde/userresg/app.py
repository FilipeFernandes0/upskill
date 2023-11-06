from flask import Flask ,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SECRET_KEY"] = "random string"
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)


# @app.route("/register",methods=["GET","POST"])


# def register():
    

#     if request.method == "POST":

#         username = request.form["username"]
#         email = request.form["email"]

#         user = User(username=username,email=email)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("registered_users"))
#     return render_template("register.html")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Register")



@app.route("/register",methods=["GET","POST"])


def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data

        user = User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        flash("Registration sucessful","success")
        return redirect(url_for("registered_users"))
    return render_template("register.html",form=form)


@app.route("/users")
def registered_users():
    users=User.query.all()
    return render_template("users.html",users=users)



if __name__ == "__main__":
   
     with app.app_context():
        db.create_all()
     app.run(debug=True)

    