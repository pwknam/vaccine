from flask import request, make_response, jsonify, session
from flask_restful import Resource
from models import Issuer, Patient, Vaccine, Vaccination, User, Validator
from config import app, db, api
from butler import Client
from PIL import Image
import io
import base64

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
                for v in issuer.vaccinations:
                    if v.to_dict(only=('patients.name', 'patients.dl_number')) not in patients:
                        patients.append(v.to_dict(only=('patients.name', 'patients.dl_number')))
                user.patients = patients
                return make_response(jsonify(user.to_dict(rules=('patients',))), 200)
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
        patient = Patient.query.filter(Patient.dl_number == id).first()
        if not patient:
            return make_response(jsonify({'error': 'Patient not found.'}), 404)
        return make_response(jsonify(patient.to_dict(only=('vaccinations.expiration_date', 'id', 'vaccinations.issuers.name', 'vaccinations.vaccines.name','vaccinations.visibility', 'vaccinations.id'))), 200)
    
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

class Upload(Resource):
    def post(self):
        image_data = request.get_json()
        # Write image data to file
        image_data = image_data['image'].split(",")[-1]
        decoded_data = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(decoded_data))
        # image.show()
        # print(image_data)
        with open('./storage/ocr_image.jpeg', 'wb') as f:
            f.write(decoded_data)

        
        # Make sure to first install the SDK using 'pip install butler-sdk'
 

        # Specify variables for use in script below
        api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjkxNDc5MTMzMjAzMDMzOTY2OSIsImVtYWlsIjoibWNob2k0MTk0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpYXQiOjE2ODE2NjkwNzU5OTZ9.zYaCZMVgMnUWurL7CGa0JGrR29CIolKRlSvgqDZjTTU'
        queue_id = '93c11f04-c119-4f78-a7b5-036b617fda49'

        # Specify the path to the file you would like to process
        file_location = './storage/ocr_image.jpeg'

        fileinfo = Client(api_key).extract_document(queue_id, file_location)
        formFields = fileinfo.to_dict()['formFields']
        for field in formFields:
            if field['fieldName'] == "Document Number":
                license = field['value']
        response = {"error": "No License found"} if not license else {"license": license}
        return make_response(response, 200)

api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
