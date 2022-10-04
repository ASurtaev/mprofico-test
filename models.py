from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json

from settings import app


db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    id_department = db.Column(db.Integer, db.ForeignKey('department.id'))

    department = db.relationship('Department', foreign_keys=[id_department])

    def json(self):
        return json.dumps({'id': self.id, 'name': self.name, 'id_department': self.id_department})

    @staticmethod
    def add_employee(_name, _id_department):
        new_employee = Employee(name=_name, id_department=_id_department)
        db.session.add(new_employee)
        db.session.commit()

    @staticmethod
    def get_employee(_id):
        return Employee.json(Employee.query.filter_by(id=_id).first())

    @staticmethod
    def update_employee(_id, _name, _id_department):
        employee_to_update = Employee.query.filter_by(id=_id).first()
        employee_to_update.name = _name
        employee_to_update.id_department = _id_department
        db.session.commit()

    @staticmethod
    def delete_employee(_id):
        Employee.query.filter_by(id=_id).delete()
        db.session.commit()


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    id_unit = db.Column('id_unit', Integer, ForeignKey('Units.id_unit'))

    Unit = relationship('Unit', foreign_keys=[id_unit])

    def json(self):
        return json.dumps({'id': self.id, 'id_unit': self.id_unit})

    @staticmethod
    def add_department(_id_unit):
        new_department = Department(id_unit=_id_unit)
        db.session.add(new_department)
        db.session.commit()

    @staticmethod
    def get_department(_id):
        return Department.json(Department.query.filter_by(id=_id).first())

    @staticmethod
    def update_department(_id, _id_unit):
        department_to_update = Department.query.filter_by(id=_id).first()
        department_to_update.id_unit = _id_unit
        db.session.commit()

    @staticmethod
    def delete_department(_id):
        Department.query.filter_by(id=_id).delete()
        db.session.commit()


class Unit(db.Model):
    __tablename__ = 'unit'

    id = db.Column(db.Integer, primary_key=True)

    def json(self):
        return json.dumps({'id': self.id, 'id_unit': self.id_unit})

    @staticmethod
    def add_unit():
        new_unit = Unit()
        db.session.add(new_unit)
        db.session.commit()

    @staticmethod
    def get_unit(_id):
        return Unit.json(Unit.query.filter_by(id=_id).first())

    @staticmethod
    def update_unit(_id):
        pass

    @staticmethod
    def delete_unit(_id):
        Unit.query.filter_by(id=_id).delete()
        db.session.commit()
