from . import db  
from datetime import datetime


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='role', lazy=True)
    staff = db.relationship('Staff', backref='role', lazy=True)

    def __repr__(self):
        return f"<User -- {self.name}>"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum("Male", "Female", name="gender_names"), nullable=False)
    address = db.Column(db.Text, nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    phone_num = db.Column(db.String(11), nullable=False)
    nin = db.Column(db.Integer, unique=True)
    marital_status = db.Column(db.String(20))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    child = db.relationship("Adoption", backref="user")

    def __repr__(self):
        return f"<User -- {self.first_name} {self.last_name}>"
    

class Staff(db.Model):
    __tablename__ = "staff"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(225), nullable=False)
    last_name = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(100))
    lga = db.Column(db.String(100))
    gender = db.Column(db.Enum("Male", "Female", name="gender_names"), nullable=False)
    phone_num = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100), nullable=False)
    nin = db.Column(db.Integer, unique=True, nullable=False)
    marital_status = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __repr__(self):
        return f"<Staff -- {self.first_name} {self.last_name}>"


class Child(db.Model):
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(225), nullable=False)
    middle = db.Column(db.String(100), nullable=True)
    last_name =db.Column(db.String(225), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    status = db.Enum("adopted", "unadopted", name="child_status")
    date_of_birth = db.Column(db.Date)
    date_admitted = db.Column(db.Date)
    medical_record = db.relationship("MedicalRecord", backref="child")
    adoption = db.relationship("Adoption", uselist=False,  backref="child")
    def __repr__(self):
        return f"<Child -- {self.first_name} {self.last_name}>"


class Adoption(db.Model):
    __table__name = "adoption"
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'))
    adoptive_parent_name = db.Column(db.String(255), nullable=False)
    adopter_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    adoption_date = db.Column(db.Date)
    
    def __repr__(self):
        return f"<Adoption -- {self.child_id}, {self.adopter_id}>"


class AdoptedChild(db.Model):
    __tablename__ ="adopted_child"
    id = db.Column(db.Integer, primary_key=True)
    firt_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum("Male", "Female", name="gender_names"), nullable=False)
    leave_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<AdoptedChild -- {self.first_name} {self.last_name}>"


class MedicalRecord(db.Model):
    __tablename__ = "medical_record"
    id = db.Column(db.Integer, primary_key=True)
    genotype = db.Column(db.String(100), nullable=True)
    blood_group = db.Column(db.String(100), nullable=True)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)

    def __repr__(self):
        return f"<Medical record -- Child ID {self.child_id}>" 
