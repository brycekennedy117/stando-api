from webapp import db
from sqlalchemy_utils import ScalarListType

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
    classification = db.Column(db.String(100), nullable=False)
    sentient = db.Column(db.Boolean(), default=False, nullable=False)
    abilities = db.Column(ScalarListType(str))

    @staticmethod
    def getAttributesAsList():
        return ['id', 'name', 'destructivePower', 'speed', 'range', 'persistence', 'precision', \
            'developmentPotential', 'kind', 'classification', 'sentient', 'abilities']

    def asDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'parameters': {
                'destructivePower': self.destructivePower,
                'speed': self.speed,
                'range': self.range,
                'persistence': self.persistence,
                'precision': self.precision,
                'developmentPotential': self.developmentPotential
            },
            'kind': self.kind,
            'classification': self.classification,
            'sentient': self.sentient,
            'abilities': self.abilities
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