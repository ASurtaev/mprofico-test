from flask import request, Response

from models import Employee, Department, Unit, app


@app.route('/api/employee', methods=['POST'])
def add_employee():
    request_data = request.get_json()
    Employee.add_employee(request_data['name'], request_data['id_department'])
    return Response('Employee added', status=201, mimetype='application/json')

@app.route('/api/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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

if __name__ == '__main__':
    app.run(port=1234, debug=True)
