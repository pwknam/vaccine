from config import app
from models import db, Issuer, Patient, Validator, User, Vaccination
from random import randint

with app.app_context():

    i1 = Issuer(name='NYU', institution_type='Hospital', verified=True)
    i2 = Issuer(name='Nathan Littauer',
                institution_type='Hospital', verified=True)
    i3 = Issuer(name='Bellevue NYC Health',
                institution_type='Hospital', verified=True)
    issuers = [i1, i2, i3]
    db.session.add_all(issuers)
    db.session.commit()

    p1 = Patient(name='Ian', dl_number=randint(100000000, 999999999))
    p2 = Patient(name='Kyushik', dl_number=randint(100000000, 999999999))
    p3 = Patient(name='Michelle', dl_number=randint(100000000, 999999999))
    p4 = Patient(name='Sally', dl_number=randint(100000000, 999999999))
    p5 = Patient(name='Bill', dl_number=randint(100000000, 999999999))
    p6 = Patient(name='Anson', dl_number=randint(100000000, 999999999))
    p7 = Patient(name='Bobby', dl_number=randint(100000000, 999999999))
    p8 = Patient(name='Jack', dl_number=randint(100000000, 999999999))
    p9 = Patient(name='Chris C.', dl_number=randint(100000000, 999999999))
    p10 = Patient(name='Chris W.', dl_number=randint(100000000, 999999999))
    p11 = Patient(name='Brett', dl_number=randint(100000000, 999999999))
    p12 = Patient(name='Finn', dl_number=randint(100000000, 999999999))
    p13 = Patient(name='Min', dl_number=randint(100000000, 999999999))
    p14 = Patient(name='Jacob', dl_number=randint(100000000, 999999999))
    p15 = Patient(name='Nick', dl_number=randint(100000000, 999999999))
    p16 = Patient(name='Eshwar', dl_number=randint(100000000, 999999999))
    patients = [p1, p2, p3, p4, p5, p6, p7, p8,
                p9, p10, p11, p12, p13, p14, p15, p16]
    db.session.add_all(patients)
    db.session.commit()

    va1 = Validator(name='Route 66')
    va2 = Validator(name='MET')
    va3 = Validator(name='Columbia University')
    validators = [va1, va2, va3]
    db.session.add_all(validators)
    db.session.commit()

    # vac1= Vaccine(name="Covid")
    # vac2= Vaccine(name="Flu")
    # vac3= Vaccine(name="Tetanus")
    # vac4= Vaccine(name="Polio")
    # vac5= Vaccine(name="Smallpox")
    # vac6= Vaccine(name="Measles")
    # vaccines = [vac1,vac2,vac3,vac4,vac5,vac6]
    # db.session.add_all(vaccines)
    # db.session.commit()

    vacc1 = Vaccination(patient_id=p1.id, issuer_id=i1.id,
                        name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc2 = Vaccination(patient_id=p1.id, issuer_id=i1.id,
                        name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc3 = Vaccination(patient_id=p1.id, issuer_id=i1.id,
                        name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc4 = Vaccination(patient_id=p1.id, issuer_id=i1.id,
                        name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc5 = Vaccination(patient_id=p1.id, issuer_id=i1.id,
                        name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc6 = Vaccination(patient_id=p1.id, issuer_id=i1.id,
                        name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc7 = Vaccination(patient_id=p2.id, issuer_id=i2.id,
                        name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc8 = Vaccination(patient_id=p2.id, issuer_id=i2.id,
                        name='Flu', expiration_date='12/31/2025', visibility=False)
    vacc9 = Vaccination(patient_id=p2.id, issuer_id=i2.id,
                        name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc10 = Vaccination(patient_id=p2.id, issuer_id=i2.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc11 = Vaccination(patient_id=p2.id, issuer_id=i2.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc12 = Vaccination(patient_id=p2.id, issuer_id=i2.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc13 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc14 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc15 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc16 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc17 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc18 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc19 = Vaccination(patient_id=p3.id, issuer_id=i3.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc20 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc21 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc22 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc23 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc24 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc25 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc26 = Vaccination(patient_id=p4.id, issuer_id=i1.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc27 = Vaccination(patient_id=p5.id, issuer_id=i2.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc28 = Vaccination(patient_id=p5.id, issuer_id=i2.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc29 = Vaccination(patient_id=p5.id, issuer_id=i2.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc30 = Vaccination(patient_id=p5.id, issuer_id=i2.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc31 = Vaccination(patient_id=p5.id, issuer_id=i2.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc32 = Vaccination(patient_id=p5.id, issuer_id=i2.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc33 = Vaccination(patient_id=p6.id, issuer_id=i3.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc34 = Vaccination(patient_id=p6.id, issuer_id=i3.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc35 = Vaccination(patient_id=p6.id, issuer_id=i3.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc36 = Vaccination(patient_id=p6.id, issuer_id=i3.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc37 = Vaccination(patient_id=p6.id, issuer_id=i3.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc38 = Vaccination(patient_id=p6.id, issuer_id=i3.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc39 = Vaccination(patient_id=p7.id, issuer_id=i1.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc40 = Vaccination(patient_id=p7.id, issuer_id=i1.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc41 = Vaccination(patient_id=p7.id, issuer_id=i1.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc42 = Vaccination(patient_id=p7.id, issuer_id=i1.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc43 = Vaccination(patient_id=p7.id, issuer_id=i1.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc44 = Vaccination(patient_id=p7.id, issuer_id=i1.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc45 = Vaccination(patient_id=p8.id, issuer_id=i2.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc46 = Vaccination(patient_id=p8.id, issuer_id=i2.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc47 = Vaccination(patient_id=p8.id, issuer_id=i2.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc48 = Vaccination(patient_id=p8.id, issuer_id=i2.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc49 = Vaccination(patient_id=p9.id, issuer_id=i3.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc50 = Vaccination(patient_id=p9.id, issuer_id=i3.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc51 = Vaccination(patient_id=p9.id, issuer_id=i3.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc52 = Vaccination(patient_id=p9.id, issuer_id=i3.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc53 = Vaccination(patient_id=p9.id, issuer_id=i3.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc54 = Vaccination(patient_id=p9.id, issuer_id=i3.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc55 = Vaccination(patient_id=p10.id, issuer_id=i1.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc56 = Vaccination(patient_id=p10.id, issuer_id=i1.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc57 = Vaccination(patient_id=p10.id, issuer_id=i1.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc58 = Vaccination(patient_id=p10.id, issuer_id=i1.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc59 = Vaccination(patient_id=p10.id, issuer_id=i1.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc60 = Vaccination(patient_id=p10.id, issuer_id=i1.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc61 = Vaccination(patient_id=p11.id, issuer_id=i2.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc62 = Vaccination(patient_id=p11.id, issuer_id=i2.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc63 = Vaccination(patient_id=p11.id, issuer_id=i2.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc64 = Vaccination(patient_id=p11.id, issuer_id=i2.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc65 = Vaccination(patient_id=p11.id, issuer_id=i2.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc66 = Vaccination(patient_id=p11.id, issuer_id=i2.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc67 = Vaccination(patient_id=p12.id, issuer_id=i3.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc68 = Vaccination(patient_id=p12.id, issuer_id=i3.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc69 = Vaccination(patient_id=p12.id, issuer_id=i3.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc70 = Vaccination(patient_id=p12.id, issuer_id=i3.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc71 = Vaccination(patient_id=p12.id, issuer_id=i3.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc72 = Vaccination(patient_id=p12.id, issuer_id=i3.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc73 = Vaccination(patient_id=p13.id, issuer_id=i1.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc74 = Vaccination(patient_id=p13.id, issuer_id=i1.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc75 = Vaccination(patient_id=p13.id, issuer_id=i1.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc76 = Vaccination(patient_id=p13.id, issuer_id=i1.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc77 = Vaccination(patient_id=p13.id, issuer_id=i1.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc78 = Vaccination(patient_id=p13.id, issuer_id=i1.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc79 = Vaccination(patient_id=p14.id, issuer_id=i2.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc80 = Vaccination(patient_id=p14.id, issuer_id=i2.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc81 = Vaccination(patient_id=p14.id, issuer_id=i2.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc82 = Vaccination(patient_id=p14.id, issuer_id=i2.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc83 = Vaccination(patient_id=p14.id, issuer_id=i2.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc84 = Vaccination(patient_id=p14.id, issuer_id=i2.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc85 = Vaccination(patient_id=p15.id, issuer_id=i3.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc86 = Vaccination(patient_id=p15.id, issuer_id=i3.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc87 = Vaccination(patient_id=p15.id, issuer_id=i3.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc88 = Vaccination(patient_id=p15.id, issuer_id=i3.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc89 = Vaccination(patient_id=p15.id, issuer_id=i3.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc90 = Vaccination(patient_id=p15.id, issuer_id=i3.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vacc91 = Vaccination(patient_id=p16.id, issuer_id=i1.id,
                         name='Covid', expiration_date='12/31/2025', visibility=True)
    vacc92 = Vaccination(patient_id=p16.id, issuer_id=i1.id,
                         name='Flu', expiration_date='12/31/2025', visibility=True)
    vacc93 = Vaccination(patient_id=p16.id, issuer_id=i1.id,
                         name='Tetanus', expiration_date='12/31/2025', visibility=True)
    vacc94 = Vaccination(patient_id=p16.id, issuer_id=i1.id,
                         name='Polio', expiration_date='12/31/2025', visibility=True)
    vacc95 = Vaccination(patient_id=p16.id, issuer_id=i1.id,
                         name='Smallpox', expiration_date='12/31/2025', visibility=True)
    vacc96 = Vaccination(patient_id=p16.id, issuer_id=i1.id,
                         name='Measles', expiration_date='12/31/2025', visibility=True)
    vaccinations = [vacc1, vacc2, vacc3, vacc4, vacc5, vacc6, vacc7, vacc8, vacc9, vacc10, vacc11, vacc12, vacc13, vacc14, vacc15, vacc16, vacc17, vacc18, vacc19, vacc20, vacc21, vacc22, vacc23, vacc24, vacc25, vacc26, vacc27, vacc28, vacc29, vacc30, vacc31, vacc32, vacc33, vacc34, vacc35, vacc36, vacc37, vacc38, vacc39, vacc40, vacc41, vacc42, vacc43, vacc44, vacc45, vacc46, vacc47, vacc48,
                    vacc49, vacc50, vacc51, vacc52, vacc53, vacc54, vacc55, vacc56, vacc57, vacc58, vacc59, vacc60, vacc61, vacc62, vacc63, vacc64, vacc65, vacc66, vacc67, vacc68, vacc69, vacc70, vacc71, vacc72, vacc73, vacc74, vacc75, vacc76, vacc77, vacc78, vacc79, vacc80, vacc81, vacc82, vacc83, vacc84, vacc85, vacc86, vacc87, vacc88, vacc89, vacc90, vacc91, vacc92, vacc93, vacc94, vacc95, vacc96]
    db.session.add_all(vaccinations)
    db.session.commit()

    u1 = User(username='Ian', role="Patient")
    u2 = User(username='Kyushik', role="Patient")
    u3 = User(username='Michelle', role="Patient")
    u4 = User(username='Sally', role="Patient")
    u5 = User(username='Bill', role="Patient")
    u6 = User(username='Anson', role="Patient")
    u7 = User(username='Bobby', role="Patient")
    u8 = User(username='Jack', role="Patient")
    u9 = User(username='Chris C.', role="Patient")
    u10 = User(username='Chris W.', role="Patient")
    u11 = User(username='Brett', role="Patient")
    u12 = User(username='Finn', role="Patient")
    u13 = User(username='Min', role="Patient")
    u14 = User(username='Jacob', role="Patient")
    u15 = User(username='Nick', role="Patient")
    u16 = User(username='Eshwar', role="Patient")
    u17 = User(username='NYU', role="Issuer")
    u18 = User(username='Nathan Littauer', role="Issuer")
    u19 = User(username='Bellevue NYC Health', role="Issuer")
    u20 = User(username='Route 66', role="Validator")
    u21 = User(username='MET', role="Validator")
    u22 = User(username='Columbia University', role="Validator")
    u1.password_hash = 'test123'
    u2.password_hash = 'test123'
    u3.password_hash = 'test123'
    u4.password_hash = 'test123'
    u5.password_hash = 'test123'
    u6.password_hash = 'test123'
    u7.password_hash = 'test123'
    u8.password_hash = 'test123'
    u9.password_hash = 'test123'
    u10.password_hash = 'test123'
    u11.password_hash = 'test123'
    u12.password_hash = 'test123'
    u13.password_hash = 'test123'
    u14.password_hash = 'test123'
    u15.password_hash = 'test123'
    u16.password_hash = 'test123'
    u17.password_hash = 'test123'
    u18.password_hash = 'test123'
    u19.password_hash = 'test123'
    u20.password_hash = 'test123'
    u21.password_hash = 'test123'
    u22.password_hash = 'test123'
    users = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11,
             u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22]
    db.session.add_all(users)
    db.session.commit()

    p1.user_id = u1.id
    p2.user_id = u2.id
    p3.user_id = u3.id
    p4.user_id = u4.id
    p5.user_id = u5.id
    p6.user_id = u6.id
    p7.user_id = u7.id
    p8.user_id = u8.id
    p9.user_id = u9.id
    p10.user_id = u10.id
    p11.user_id = u11.id
    p12.user_id = u12.id
    p13.user_id = u13.id
    p14.user_id = u14.id
    p15.user_id = u15.id
    p16.user_id = u16.id
    i1.user_id = u17.id
    i2.user_id = u18.id
    i3.user_id = u19.id
    va1.user_id = u20.id
    va2.user_id = u21.id
    va3.user_id = u22.id
    db.session.add_all(patients)
    db.session.add_all(issuers)
    db.session.add_all(validators)
    db.session.commit()
