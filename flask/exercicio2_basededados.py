from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'  
db = SQLAlchemy(app)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    employees = db.relationship('Employee', back_populates='department')

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    department = db.relationship('Department', back_populates='employees')

with app.app_context():
    db.create_all()

    hr = Department(name='HR')
    db.session.add(hr)
    db.session.commit()

    employee1 = Employee(name='John Doe', department=hr)
    employee2 = Employee(name='Jane Smith', department=hr)
    db.session.add_all([employee1, employee2])
    db.session.commit()

    # Query data
    department = Department.query.filter_by(name='HR').first()
    employees_in_hr = department.employees

    for employee in employees_in_hr:
        print(employee.name)

if __name__ == '__main__':
    app.run()