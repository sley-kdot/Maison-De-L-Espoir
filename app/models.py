from maison import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(100), unique=True)
    address = db.Column(db.Text)
    occupation = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User -- {self.first_name} {self.last_name}>"
    

class Staff(db.Model):
    __tablename__ = "staff"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(225), unique=True)
    last_name = db.Column(db.String(225), unique=True)
    email = db.Column(db.String(100), unique=True, index=True)

    def __repr__(self):
        return f"<Staff -- {self.first_name} {self.last_name}>"


class Child(db.Model):
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(225), unique=True)
    last_name =db.Column(db.String(225), unique=True)
    status = db.Enum("adopted", "unadopted")
    date_admitted = db.Column(db.Date)

    def __repr__(self):
        return f"<Child -- {self.first_name} {self.last_name}>"

# class Adoption(db.Model):
#     pass


# class AdoptiveP

# class MedicalRecord(db.Model):
#     __tablename__ = "medical record"
#     id = db.Column(db.Integer, unique=True)
#     genotype = db.Column(db.String(100), nullable=True)
#     blood_group = db.Column(db.String(100), nullable=True)

#     def __repr__(self):
#         return f"<Medical record -- {self.genotype}>" 
