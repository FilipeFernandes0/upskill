from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db =SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cities = db.relationship('City', backref='country',lazy=True)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    country_id=db.Column(db.Integer,db.ForeignKey('country.id'),nullable=False)


with app.app_context():
    db.create_all()


    usa = Country(name='United States')
    nyc = City(name='New York', country=usa)
    la = City(name='Los Angeles', country=usa)
    chicago = City(name='Chicago', country=usa)

    db.session.add(usa)
    db.session.commit()

    # Query data
    usa = Country.query.filter_by(name='United States').first()
    cities_in_usa = usa.cities

    for city in cities_in_usa:
        print(city.name)

if __name__ == '__main__':
    app.run()  