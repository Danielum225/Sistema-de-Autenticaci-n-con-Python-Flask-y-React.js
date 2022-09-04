"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])
def login():
    data = request.json()
    print(data)

    user = User.query.filter_by(email = data['email'], password = data['password']).first()
    if not user:
        return jsonify({"message":"Email o contraseña incorrectos"}), 400
    access_token = create_access_token(identity=user)

    return jsonify({"token": access_token}), 200

@api.route('/user/<int:id>', methods=['GET'])
@jwt_required()
def get_user():
    user = User.query.get(id)
    return jsonify(user.serialize())


    return jsonify({"token": access_token}), 200