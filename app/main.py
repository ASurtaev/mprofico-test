from flask import Blueprint, request, Response
from flask_login import login_required

from models import Employee, Department, Unit, User

main = Blueprint('main', __name__)


@main.route('/api/employee', methods=['POST'])
@login_required
def add_employee():
    request_data = request.get_json()
    Employee.add_employee(request_data['name'], request_data['id_department'])
    return Response('Employee added', status=201, mimetype='application/json')


@main.route('/api/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def get_employee_by_id(id):
    if request.method == 'GET':
        return Employee.get_employee(id)
    elif request.method == 'PUT':
        request_data = request.get_json()
        Employee.update_employee(id, request_data['name'], request_data['id_department'])
        return Response('Employee updated', status=200, mimetype='application/json')
    elif request.method == 'DELETE':
        Employee.delete_employee(id)
        return Response('Employee deleted', status=200, mimetype='application/json')


@main.route('/api/department', methods=['POST'])
@login_required
def add_department():
    request_data = request.get_json()
    Department.add_department(request_data['id_unit'])
    return Response('Department added', status=201, mimetype='application/json')


@main.route('/api/department/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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


@main.route('/api/unit', methods=['POST'])
@login_required
def add_unit():
    Unit.add_unit()
    return Response('Unit added', status=201, mimetype='application/json')


@main.route('/api/unit/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
