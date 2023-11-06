from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase11.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
# Create the database
with app.app_context():
    db.create_all()

# Login Manager Configuration
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define the is_valid_password function
def is_valid_password(password):
    return bool(re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).{8,}$', password))



# Define a form for creating new posts
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])


# Implement Registration Form Validation (Flask-WTF)
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

    def validate_password(self, field):
        if not is_valid_password(field.data):
            flash('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.', 'danger')
            raise ValidationError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.')


# Implement Login Validation (Flask-WTF) 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])


@app.route('/')
def index():
    # Retrieve all blog posts from the database
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='scrypt')
        #hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# Handle the ValidationError exception manually
@app.errorhandler(ValidationError)
def handle_validation_error(e):
    flash(str(e), 'danger')
    return redirect(url_for('register'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user_posts=current_user.posts)



@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Create a new blog post and save it to the database
        new_post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    print("trying to access 1")
    post = Post.query.get_or_404(post_id)
    # Check if the current user is the author of the post
    if post.author != current_user:
        flash('You do not have permission to edit this post.', 'danger')
        return redirect(url_for('dashboard'))
    form = PostForm()  # Bind the form with the post data
    if form.validate_on_submit():
        print("trying to access 2")
        # Update the post's title and content
        post.title = form.title.data
        post.content = form.content.data
        try:
            db.session.commit()  # Save changes to the database
            flash('Your post has been updated!', 'success')
            print("Post successfully updated")  # Add this line for debugging
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()  # Rollback changes on database error
            flash('An error occurred while updating the post. Please try again.', 'danger')
            print(f"Error: {str(e)}")  # Add this line for debugging
    return render_template('edit_post.html', form=form, post=post)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash('You do not have permission to delete this post.', 'danger')
        return redirect(url_for('dashboard'))
    db.session.delete(post)
    db.session.commit()
    flash('Blog post deleted!', 'success')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug = True)