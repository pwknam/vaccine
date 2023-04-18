from flask import request, make_response, jsonify, session
from flask_restful import Resource
from models import Issuer, Patient, Vaccine, Vaccination, User, Validator
from config import app, db, api

class SignupPatient(Resource):
    def post(self, id):
        data = request.get_json()
        try:
            patient = Patient.query.filter(Patient.dl_number == id).first()
            new_user = User(username=data['username'], role='Patient')
            new_user.password_hash = data['password']
            db.session.add(new_user)
            db.session.commit()
            patient.user_id = new_user.id
            db.session.add(patient)
            db.session.commit()
            session['user_id'] = new_user.id
            session['role'] = new_user.role
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}), 422)
        return make_response(jsonify(new_user.to_dict()), 201)
    
api.add_resource(SignupPatient, '/signup_patient/<int:id>')
    
class SignupValidator(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_user = User(username=data['username'], role='Validator')
            new_user.password_hash = data['password']
            db.session.add(new_user)
            db.session.commit()
            new_validator = Validator(name=data['username'], user_id=new_user.id)
            db.session.add(new_validator)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}))
        return make_response(jsonify(new_user.to_dict()), 201)
    
api.add_resource(SignupValidator, '/signup_validator')

class SignupIssuer(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_user = User(username=data['username'], role='Issuer')
            new_user.password_hash = data['password']
            db.session.add(new_user)
            db.session.commit()
            new_validator = Issuer(name=data['username'], user_id=new_user.id, institution_type=data['institution_type'], verified=False)
            db.session.add(new_validator)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}))
        return make_response(jsonify(new_user.to_dict()), 201)
    
api.add_resource(SignupIssuer, '/signup_issuer')


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.username == data['username']).first()
        if user.authenticate(data['password']):
            session['user_id'] = user.id
            session['user_role'] = user.role
            return user.to_dict(), 200
        return make_response(jsonify({'error': 'Invalid username or password.'}), 401)

api.add_resource(Login, '/login')
class Vaccines(Resource):
    def post(self):
        data = request.get_json()
        try:
            v1 = Vaccine(name=data['name'])
            db.session.add(v1)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}),422)
        return make_response(jsonify(v1.to_dict()), 201)
    
api.add_resource(Vaccines, '/vaccines')

class PatientByID(Resource):
    def get(self, id):
        patient = Patient.query.filter(Patient.id_number == id).first()
        if not patient:
            return make_response(jsonify({'error': 'Patient not found.'}), 404)
        return make_response(jsonify(patient.to_dict(rules=('vaccinations', ))), 200)
    
api.add_resource(PatientByID, '/patients/<int:id>')
    
class Patients(Resource):
    def get(self):
        # make get patients only available to specific role
        patients = [p.to_dict() for p in Patients.query.all()]
        return make_response(jsonify(patients), 200)
    
    def post(self):
        data = request.get_json()
        try:
            patient = Patient(name=data['name'], id_number=data['id_number'])
            db.session.add(patient)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}),422)
        return make_response(jsonify(patient.to_dict()), 201)
    
api.add_resource(Patients, '/patients')
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
