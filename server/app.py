from flask import request, make_response, jsonify, session
from flask_restful import Resource
from models import Issuer, Patient, Vaccination, User, Validator
from config import app, db, api
from butler import Client
from PIL import Image
import io
import base64
import smtplib
import ssl
from email.message import EmailMessage

app.secret_key = b'kyushikiscool'


class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            if session.get('user_role') == 'Issuer':
                issuer = user.issuer
                patients = []
                dl_numbers = set()
                for v in issuer.vaccinations:
                    if v.patients.dl_number not in dl_numbers:
                        patients.append({
                            'name': v.patients.name,
                            'dl_number': v.patients.dl_number,
                            'id': v.patients.id
                        })
                        dl_numbers.add(v.patients.dl_number)
                user.patients = patients
                user.issuer_id = issuer.id
                user.dl_number = session.get('dl_number')
                return make_response(jsonify(user.to_dict(rules=('patients', 'issuer_id', 'dl_number'))), 200)
            elif session.get('user_role') == 'Patient':
                return make_response(jsonify({'name': user.patient.name, 'dl_number': user.patient.dl_number, "role": "Patient"}), 200)
            elif session.get('user_role') == 'Validator':
                user.validator.role = user.validator.users.role
                user.validator.dl_number = session.get('dl_number')
                return make_response(jsonify(user.validator.to_dict(only=('name', 'id', 'role', 'dl_number'))), 200)
            return make_response(jsonify({'error': 'Invalid username or password.'}), 401)
        else:
            return {'error': 'Unauthorized'}, 401


api.add_resource(CheckSession, '/check_session')


class Logout(Resource):
    def post(self):
        session['user_id'] = None
        session['user_role'] = None
        return {}, 204


api.add_resource(Logout, '/logout')


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
            session['user_role'] = new_user.role
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}), 422)
        return make_response(jsonify({'name': new_user.patient.name, 'dl_number': new_user.patient.dl_number, "role": "Patient"}), 200)


api.add_resource(SignupPatient, '/signup_patient/<int:id>')


class SignupValidator(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_user = User(username=data['username'], role='Validator')
            new_user.password_hash = data['password']
            db.session.add(new_user)
            db.session.commit()
            new_validator = Validator(
                name=data['username'], user_id=new_user.id)
            db.session.add(new_validator)
            db.session.commit()
            session['user_id'] = new_user.id
            session['user_role'] = new_user.role
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
            new_user.patients = []
            db.session.add(new_user)
            db.session.commit()
            new_validator = Issuer(
                name=data['username'], user_id=new_user.id, institution_type='Medical', verified=False)
            db.session.add(new_validator)
            db.session.commit()
            new_user.issuer_id = new_validator.id
            session['user_id'] = new_user.id
            session['user_role'] = new_user.role
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}))
        return make_response(jsonify(new_user.to_dict(rules=('patients', 'issuer_id'))), 201)


api.add_resource(SignupIssuer, '/signup_issuer')


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.username == data['username']).first()
        if user.authenticate(data['password']):
            # print(user.role, 'line somethin')
            session['user_id'] = user.id
            session['user_role'] = user.role
            # print(session.get('user_role'), 'wpposadf')
            if user.role == 'Issuer':
                issuer = user.issuer
                patients = []
                dl_numbers = set()
                for v in issuer.vaccinations:
                    if v.patients.dl_number not in dl_numbers:
                        patients.append({
                            'name': v.patients.name,
                            'dl_number': v.patients.dl_number,
                            'id': v.patients.id
                        })
                        dl_numbers.add(v.patients.dl_number)
                user.patients = patients
                user.issuer_id = issuer.id

                return make_response(jsonify(user.to_dict(rules=('patients', 'issuer_id'))), 200)
            elif user.role == 'Patient':
                return make_response(jsonify({'name': user.patient.name, 'dl_number': user.patient.dl_number, "role": "Patient"}), 200)
            elif user.role == 'Validator':
                user.validator.role = user.validator.users.role
                return make_response(jsonify(user.validator.to_dict(only=('name', 'id', 'role'))), 200)
        return make_response(jsonify({'error': 'Invalid username or password.'}), 401)


api.add_resource(Login, '/login')


# class Vaccines(Resource):
#     def post(self):
#         data = request.get_json()
#         try:
#             vaccine = Vaccine(
#                 name=data['name'])
#             db.session.add(vaccine)
#             db.session.commit()
#         except ValueError as e:
#             return make_response(jsonify({'errors': [str(e)]}), 422)
#         return make_response(jsonify(vaccine.to_dict()), 201)


# api.add_resource(Vaccines, '/vaccines')


class Vaccinations(Resource):
    def post(self):

        data = request.get_json()

        if data['email'] != '':
            email_sender = 'info.vaccinerecords@gmail.com'
            email_password = 'hejneulmiryurccz'
            email_receiver = data['email']

            subject = 'Activate Vaccination Account'
            body = """
            Hello,
            
            Thank you for getting your {} vaccine today.

            Please click this link to activate your account and update the privacy settings of your vaccine records: TO ADD!
            """.format(data['name'])

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

        try:
            vaccination = Vaccination(
                name=data['name'], expiration_date=data['expiration_date'], patient_id=data['patient_id'], issuer_id=data['issuer_id'], visibility=False)
            db.session.add(vaccination)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}), 422)
        vaccination.issuer_name = vaccination.issuers.name
        return make_response(jsonify(vaccination.to_dict(only=('name', 'issuer_name', 'expiration_date'))), 201)


api.add_resource(Vaccinations, '/vaccinations')


class PatientByID(Resource):
    def get(self, id):
        patient = Patient.query.filter(Patient.dl_number == id).first()
        session['dl_number'] = id
        # print(f"user role: {session.get('user_role')}")
        # print(f"user id {session.get('user_id')}")
        if not patient:
            return make_response(jsonify({'error': 'Patient not found.'}), 404)
        if session.get('user_role') == 'Validator':
            patient.vaccinations = [v for v in Vaccination.query.filter(
                Vaccination.patient_id == patient.id) if v.visibility == True]
            for v in patient.vaccinations:
                v.expiration_date = v.expiration_date
                v.issuer_name = v.issuers.name
            return make_response(jsonify(patient.to_dict(only=('name', 'vaccinations.expiration_date', 'vaccinations.name', 'vaccinations.issuer_name', 'id'))), 200)
        elif session.get('user_role') == 'Patient':
            patient.vaccinations = [v for v in Vaccination.query.filter(
                Vaccination.patient_id == patient.id)]
            for v in patient.vaccinations:
                v.expiration_date = v.expiration_date
                v.issuer_name = v.issuers.name
                v.vaccination_id = v.id
            return make_response(jsonify(patient.to_dict(only=('name', 'vaccinations.expiration_date', 'vaccinations.name', 'vaccinations.issuer_name', 'vaccinations.visibility', 'vaccinations.id', 'id'))), 200)
        elif session.get('user_role') == 'Issuer':
            patient.vaccinations = [v for v in Vaccination.query.filter(
                Vaccination.patient_id == patient.id)]
            for v in patient.vaccinations:
                v.expiration_date = v.expiration_date
                v.issuer_name = v.issuers.name
                v.vaccination_id = v.id
            return make_response(jsonify(patient.to_dict(only=('name', 'vaccinations.expiration_date', 'vaccinations.name', 'id', 'vaccinations.issuer_name', 'vaccinations.id'))), 200)
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)


api.add_resource(PatientByID, '/patients/<int:id>')


class VaccinationByID(Resource):
    def patch(self, id):
        vaccination = Vaccination.query.filter(Vaccination.id == id).first()
        if not vaccination:
            return make_response(jsonify({'error': "Vaccination not found"}), 404)
        data = request.get_json()
        try:
            for attr in data:
                setattr(vaccination, attr, data[attr])
            db.session.add(vaccination)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}))
        vaccination.issuer_name = vaccination.issuers.name
        return make_response(jsonify(vaccination.to_dict(only=('expiration_date', 'id', 'issuer_id', 'name', 'issuer_name', 'visibility'))), 200)

    def get(self, id):
        vaccination = Vaccination.query.filter(Vaccination.id == id).first()
        if not vaccination:
            return make_response(jsonify({'error': 'Vaccination not found'}), 404)
        vaccination.issuer_name = vaccination.issuers.name
        return make_response(jsonify(vaccination.to_dict(only=('expiration_date', 'id', 'issuer_id', 'name', 'issuer_name', 'visibility'))), 200)


api.add_resource(VaccinationByID, '/vaccinations/<int:id>')


class Patients(Resource):
    def get(self):
        # make get patients only available to specific role
        patients = [p.to_dict() for p in Patient.query.all()]
        return make_response(jsonify(patients), 200)

    def post(self):
        data = request.get_json()
        if session.get('user_role') != "Issuer" or not session.get('user_role'):
            return make_response(jsonify({'error': 'Unauthorized access'}))
        try:
            patient = Patient(name=data['name'], dl_number=data['dl_number'])
            db.session.add(patient)
            db.session.commit()
        except ValueError as e:
            return make_response(jsonify({'errors': [str(e)]}), 422)
        return make_response(jsonify(patient.to_dict(only=('name', 'id', 'dl_number'))), 201)


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
        response = {"error": "No License found"} if not license else {
            "license": license}
        return make_response(response, 200)


api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
