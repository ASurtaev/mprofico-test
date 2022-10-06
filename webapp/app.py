from flask import request, Response
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import Employee, Department, Unit, User
from init import app, login_manager, db


@app.route('/api/employee', methods=['POST', 'GET'])
@login_required
def employee_endpoint():
    if request.method == 'POST':
        request_data = request.get_json()
        Employee.add_employee(request_data['name'], request_data['id_department'])
        return Response('Employee added', status=201, mimetype='application/json')
    elif request.method == 'GET':
        return {'Employees': Employee.get_all_employees(request.json.get('department'), request.json.get('unit'))}


@app.route('/api/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def employee_endpoint_id(id):
    if request.method == 'GET':
        return Employee.get_employee(id)
    elif request.method == 'PUT':
        request_data = request.get_json()
        Employee.update_employee(id, request_data['name'], request_data['id_department'])
        return Response('Employee updated', status=200, mimetype='application/json')
    elif request.method == 'DELETE':
        Employee.delete_employee(id)
        return Response('Employee deleted', status=200, mimetype='application/json')


@app.route('/api/department', methods=['POST', 'GET'])
@login_required
def add_department():
    if request.method == 'POST':
        request_data = request.get_json()
        Department.add_department(request_data['id_unit'])
        return Response('Department added', status=201, mimetype='application/json')
    elif request.method == 'GET':
        return {'Departments': Department.get_all_departments(request.json.get('unit'))}


@app.route('/api/department/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def get_department_by_id(id):
    if request.method == 'GET':
        return Department.get_department(id)
    elif request.method == 'PUT':
        request_data = request.get_json()
        Department.update_department(id, request_data['id_unit'])
        return Response('Department updated', status=200, mimetype='application/json')
    elif request.method == 'DELETE':
        Department.delete_department(id)
        return Response('Department deleted', status=200, mimetype='application/json')


@app.route('/api/unit', methods=['POST', 'GET'])
@login_required
def add_unit():
    if request.method == 'POST':
        Unit.add_unit()
        return Response('Unit added', status=201, mimetype='application/json')
    elif request.method == 'GET':
        return {'Units': Unit.get_all_units()}


@app.route('/api/unit/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def get_unit_by_id(id):
    if request.method == 'GET':
        return Unit.get_unit(id)
    elif request.method == 'PUT':
        Unit.update_unit(id)
        return Response('Unit is unupdateable', status=200, mimetype='application/json')
    elif request.method == 'DELETE':
        Unit.delete_unit(id)
        return Response('Unit deleted', status=200, mimetype='application/json')


# TODO: разнести энпоинты аутентификации и основные в разные файлы
@app.route('/api/login', methods=['POST'])
def login():
    request_data = request.get_json()
    user = User.get_user_by_email(request_data['email'])

    if not user or not check_password_hash(user.password, request_data['password']):
        return Response('No such user or wrong password', status=401, mimetype='application/json')
    login_user(user, remember=True)
    return Response('Login success', status=200, mimetype='application/json')


@app.route('/api/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    user = User.query.filter_by(email=request_data['email']).first()

    if user:
        return Response('User already exists', status=401, mimetype='application/json')
    User.add_user(request_data['email'], request_data['name'], generate_password_hash(request_data['password']))
    return Response('User added', status=200, mimetype='application/json')


@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return Response('Logout success', status=200, mimetype='application/json')


if __name__ == '__main__':
    db.create_all()
    login_manager.user_loader(User.get_user_by_id)
    app.run(host='0.0.0.0', port='5000')
