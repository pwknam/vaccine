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
            new_validator = Issuer(name=data['username'], user_id=new_user.id, institution_type='Medical', verified=False)
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
            if user.role == 'Issuer':
                issuer = user.issuer
                patients = []
                dl_numbers = set()
                for v in issuer.vaccinations:
                    if v.patients.dl_number not in dl_numbers:
                        patients.append({
                            'name' : v.patients.name,
                            'dl_number' : v.patients.dl_number
                        })
                        dl_numbers.add(v.patients.dl_number)
                user.patients = patients
                return make_response(jsonify(user.to_dict(rules=('patients',))), 200)
        return make_response(jsonify({'error': 'Invalid username or password.'}), 401)

api.add_resource(Login, '/login')
class Vaccines(Resource):
    def post(self):
        data = request.get_json()
        try:
            vaccine = Vaccine(name=data['name'])
            db.session.add(vaccine)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}),422)
        return make_response(jsonify(vaccine.to_dict()), 201)
    
api.add_resource(Vaccines, '/vaccines')

class PatientByID(Resource):
    def get(self, id):
        patient = Patient.query.filter(Patient.dl_number == id).first()
        if not patient:
            return make_response(jsonify({'error': 'Patient not found.'}), 404)
        
        # if session['role'] == 'Validator':
        patient.vaccinations = [v for v in Vaccination.query.filter(Vaccination.patient_id == patient.id) if v.visibility == True]
        for v in patient.vaccinations:
            v.expiration_date = v.expiration_date
            v.issuer_name = v.issuers.name
            v.vaccine_name = v.vaccines.name
        return make_response(jsonify(patient.to_dict(only=('name','vaccinations.expiration_date', 'vaccinations.vaccine_name', 'vaccinations.issuer_name'))), 200)
        # elif session['role'] == 'Patient':
        #     patient.vaccinations = [v for v in Vaccination.query.filter(Vaccination.patient_id == patient.id)]
        #     for v in patient.vaccinations:
        #         v.expiration_date = v.expiration_date
        #         v.issuer_name = v.issuers.name
        #         v.vaccine_name = v.vaccines.name
        #     return make_response(jsonify(patient.to_dict(only=('name','vaccinations.expiration_date', 'vaccinations.vaccine_name', 'vaccinations.issuer_name', 'v.visibility'))), 200)
        # return make_response(jsonify({'error': 'Unauthorized access'}), 401)

api.add_resource(PatientByID, '/patients/<int:id>')
    
class Patients(Resource):
    def get(self):
        # make get patients only available to specific role
        patients = [p.to_dict() for p in Patients.query.all()]
        return make_response(jsonify(patients), 200)
    
    def post(self):
        data = request.get_json()
        try:
            patient = Patient(name=data['name'], id_number=data['dl_number'])
            db.session.add(patient)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}),422)
        return make_response(jsonify(patient.to_dict()), 201)
    
api.add_resource(Patients, '/patients')
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
