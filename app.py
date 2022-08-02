from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Characters, Planets, User

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
 
db.init_app(app)
Migrate(app,db)
CORS(app)

#Root Route
@app.route('/', methods=['GET'])
def root():
    return jsonify({"msg" : "API REST FLASK"},200)

#Get ALL Characters
@app.route('/people', methods=['GET'])
def get_people():
    characters = Characters.query.all()
    characters = list(map(lambda character: character.serialize(),characters))

    return jsonify(characters),200

#Get ONE Character by ID
@app.route('/people/<int:id>', methods=['GET'])
def get_people_by_id(id):
    character = Characters.query.get(id)
    return jsonify(character.serialize()),200

#Get ALL Planets
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    planets = list(map(lambda planet: planet.serialize(),planets))
    return jsonify(planets),200

#Get ONE Planet by ID
@app.route('/planets/<int:id>', methods=['GET'])
def get_planet_by_id(id):
    planet = Planets.query.get(id)
    return jsonify(planet.serialize()),200

#Get ALL Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_with_favorites(),users))
    return jsonify(users),200


if __name__ == '__main__':
    app.run()