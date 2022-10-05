from flask import Blueprint, request, Response
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/api/login', methods=['POST'])
def login():
    request_data = request.get_json()
    user = User.get_user_by_email(request_data['email'])

    if not user or not check_password_hash(request_data['password'], user.password):
        return Response('No such user or wrong password', status=401, mimetype='application/json')
    login_user(user, remember=True)
    return Response('Login success', status=200, mimetype='application/json')


@auth.route('/api/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    user = User.query.filter_by(email=request_data['email']).first()

    if user:
        return Response('User already exists', status=401, mimetype='application/json')
    User.add_user(request_data['email'], request_data['name'], generate_password_hash(request_data['password']))


@auth.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return Response('Logout success', status=200, mimetype='application/json')
