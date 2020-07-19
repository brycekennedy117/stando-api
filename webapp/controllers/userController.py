from webapp import db
from webapp.models import User

class UserController:
    def getUser(self, id):
        return User.query.filter_by(id=id).first()
    
    def getUsers(self, args=None):
        if (args):
            return User.query.filter_by(**args)
        return User.query.all()

    def createUser(self, params):
        newUser = User(id=params[0], firstName=params[1], lastName=params[2], age=params[3])
        db.session.add(newUser)
        db.session.commit()
        return newUser

    def updateUser(self, id, params):
        user = User.query.filter_by(id=id).first()
        if params.get('firstName'):
            user.firstName = params['firstName']
        if params.get('lastName'):
            user.lastName = params['lastName']
        if params.get('age'):
            user.age = params['age']
        db.session.commit()
        return user

    def deleteUser(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return {'result': 'success'}

userController = UserController()