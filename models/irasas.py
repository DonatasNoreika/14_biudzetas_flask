from main import db

class Irasas(db.Model):
    __tablename__ = 'Irasas'
    id = db.Column(db.Integer, primary_key=True)
    suma = db.Column("Suma", db.Float)
    info = db.Column("Info", db.String(120))

    def __init__(self, suma, info):
        self.suma = suma
        self.info = info

    def __repr__(self):
        return f'{self.id}: suma - {self.suma}, info - {self.info}'

db.create_all()