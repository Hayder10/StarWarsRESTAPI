from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
 
db.init_app(app)
Migrate(app,db)
CORS(app)

@app.route('/')
def root():
    return jsonify({"msg" : "API REST FLASK"},200)

if __name__ == '__main__':
    app.run()