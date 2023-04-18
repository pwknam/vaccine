from config import app
from models import db, Issuer, Patient, Validator, User, Vaccination, Vaccine

with app.app_context():

    i1 = Issuer(name='Ian', institution_type='Hospital', verified=True)
    db.session.add(i1)
    db.session.commit()
    p1 = Patient(name='Christ', id_number=12341234)
    db.session.add(p1)
    db.session.commit()
    va1= Validator(name='Jack')
    db.session.add(va1)
    db.session.commit()
    vac1= Vaccine(name="Covid")
    db.session.add(vac1)
    db.session.commit()
    vacc1= Vaccination(patient_id=p1.id, issuer_id=i1.id, vaccine_id=vac1.id, visibility=True)
    db.session.add(vacc1)
    db.session.commit()
    
    u1 = User(name='Ian Strom', username='ianstrom', role='Issuer')
    u1.password_hash = 'pooopopopopy'
    db.session.add(u1)
    db.session.commit()
    u2 = User(name='Jack Schliewe', username='jackschliewe', role='Validator')
    u2.password_hash = 'poopsafdkpo'
    db.session.add(u2)
    db.session.commit()
    u3 = User(name='Christ', username='jesus', role='Patient')
    u3.password_hash= 'asdfasdfadfsa'
    db.session.add(u3)
    db.session.commit()
    p1.user_id = u3.id
    va1.user_id= u2.id
    i1.user_id=u1.id
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.commit()