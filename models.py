import email
from enum import unique
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True,nullable=False)
    favorites = db.relationship('Favorites', backref="user", uselist=False) # One to One

    def serialize(self):
        return{
            "id" : self.id,
            "username" : self.username,
            "email" : self.email
        }

    def serialize_with_favorites(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorites": self.get_favorites()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer,primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id')) # Foreign Key of Planets Table
    planets = db.relationship('Planets',backref= 'favorites') #  One to Many
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id')) # Foreign Key of Characters Table
    characters = db.relationship('Characters',backref= 'favorites')#  One to Many
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id')) # Foreign Key of Vehicles Table
    vehicles = db.relationship('Vehicles',backref='favorites')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Foreign Key of User Table

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    gravity = db.Column(db.String(255))
    terrain = db.Column(db.String(255))
    population = db.Column(db.Integer)

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    height = db.Column(db.String(255))
    mass = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))# Foreign Key of Vehicles Table , ONE TO MANY
    char_vehicles = db.relationship('Vehicles',backref='characters')

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    max_speed = db.Column(db.Integer)
    pilots = db.Column(db.Integer)




