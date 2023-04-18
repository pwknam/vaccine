from flask import request, make_response, jsonify, session
from flask_restful import Resource
from models import Issuer, Patient, Vaccine, Vaccination, User
from config import app, db, api

class Signup(Resource):
    pass
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
        patient = Patient.query.filter(Patient.id == id).first()
        if not patient:
            return make_response(jsonify({'error': 'Patient not found.'}), 404)
        return make_response(jsonify(patient.to_dict()), 200)
    
api.add_resource(PatientByID, '/patients/<int:id>')
    
class Patients(Resource):
    def get(self):
        # make get patients only available to specific role
        patients = [p.to_dict() for p in Patients.query.all()]
        return make_response(jsonify(patients), 200)
    
api.add_resource(Patients, '/patients')
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
