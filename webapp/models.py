from webapp import db

class Stand(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    destructivePower = db.Column(db.String(1))
    speed = db.Column(db.String(1))
    range = db.Column(db.String(1))
    persistence = db.Column(db.String(1))
    precision = db.Column(db.String(1))
    developmentPotential = db.Column(db.String(1))
    kind = db.Column(db.String(100), nullable=False)

    @staticmethod
    def getAttributesAsList():
        return ['id', 'name', 'destructivePower', 'speed', 'range', 'persistence', 'precision', 'developmentPotential', 'kind']

    def asDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'destructivePower': self.destructivePower,
            'speed': self.speed,
            'range': self.range,
            'persistence': self.persistence,
            'precision': self.precision,
            'developmentPotential': self.developmentPotential,
            'kind': self.kind
        }


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(26), nullable=False)
    lastName = db.Column(db.String(26), nullable=False)
    age = db.Column(db.Integer(), nullable=False)

    @staticmethod
    def getAttributesAsList():
        return ['id', 'firstName', 'lastName', 'age']

    def asDict(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'age': self.age
        }