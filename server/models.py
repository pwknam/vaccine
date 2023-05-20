from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt, db


class Vaccination(db.Model, SerializerMixin):
    __tablename__ = 'vaccinations'

    serialize_rules = ('-patient', '-issuer',
                       '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    issuer_id = db.Column(db.Integer, db.ForeignKey('issuers.id'))
    name = db.Column(db.String)
    expiration_date = db.Column(db.String)
    visibility = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    serialize_rules = ('-created_at', '-updated_at', '-vaccinations', '-user')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dl_number = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    vaccinations = db.relationship('Vaccination', backref='patients')
    issuers = association_proxy('vaccinations', 'issuer')


class Issuer(db.Model, SerializerMixin):
    __tablename__ = 'issuers'

    serialize_rules = ('-vaccinations', '-created_at', '-updated_at', '-user')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    institution_type = db.Column(db.String)
    verified = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    vaccinations = db.relationship('Vaccination', backref='issuers')
    patients = association_proxy('vaccinations', 'patient')

class Validator(db.Model, SerializerMixin):
    __tablename__ = 'validators'

    serialize_rules = ('-created_at', '-updated_at', '-user')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-patient', '-issuer', '-validator',
                       '-created_at', '-updated_at', '-_password_hash',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    patient = db.relationship('Patient', backref='users', uselist=False)
    issuer = db.relationship('Issuer', backref='users',  uselist=False)
    validator = db.relationship('Validator', backref='users',  uselist=False)

    @validates('username')
    def validates_username(self, key, username):
        usernames = [u.username for u in User.query.all()]
        if username in usernames:
            raise ValueError('Username is taken.')
        return username

    @validates('role')
    def validates_role(self, key, role):
        if role not in ['Validator', 'Patient', 'Issuer']:
            raise ValueError("Role must be Validator, Patient, or Issuer")
        return role

    @hybrid_property
    def password_hash(self):
        raise Exception("Password hashes may not be viewed")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
