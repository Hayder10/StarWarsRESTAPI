import email
from enum import unique
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref="user")  # One to One

    def serialize(self):
        return{
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def serialize_with_favorites(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorites": self.get_favorites()
        }

    def get_favorites(self):
        return list(map(lambda favorite:{'id': favorite.id, "planet_id": favorite.planet_id, "character_id": favorite.character_id, "vehicle_id": favorite.vehicle_id},self.favorites))


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
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))  # Foreign Key of Planets Table
    planets = db.relationship('Planets', backref='favorites',secondary='planets')  # One to Many
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))  # Foreign Key of Characters Table
    characters = db.relationship('Characters', backref='favorites', secondary='characters')  # One to Many
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))  # Foreign Key of Vehicles Table
    vehicles = db.relationship('Vehicles', backref='favorites', secondary='vehicles')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign Key of User Table

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    gravity = db.Column(db.String(255))
    terrain = db.Column(db.String(255))
    population = db.Column(db.Integer)

    def serialize(self):
        return{
            "id" :  self.id,
            "name" : self.name,
            "gravity" : self.gravity,
            "terrain" : self.terrain,
            "population" : self.population
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    height = db.Column(db.String(255))
    mass = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    # Foreign Key of Vehicles Table , ONE TO MANY
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    char_vehicles = db.relationship('Vehicles', backref='characters')

    def serialize(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "height" : self.height,
            "mass" : self.mass,
            "gender" : self.gender,
            "vehicle_id" : self.vehicle_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    max_speed = db.Column(db.Integer)
    pilots = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()