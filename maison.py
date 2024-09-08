from app import app, db
from app.models import Role, User, Staff, Child, Adoption, AdoptedChild, MedicalRecord


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Staff=Staff, Child=Child,
                Adoption=Adoption, AdoptedChild=AdoptedChild, MedicalRecord=MedicalRecord)

if __name__ == "__main__":
    app.run(debug=1)


