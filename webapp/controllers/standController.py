from webapp import db
from webapp.models import Stand

class StandController:
    def getStand(self, id):
        return Stand.query.filter_by(id=id).first()
    
    def getStands(self, args=None):
        if (args):
            return Stand.query.filter_by(**args)
        return Stand.query.all()

    def createStand(self, params):
        newStand = Stand(id=params[0], name=params[1], destructivePower=params[2], speed=params[3], range=params[4], \
            persistence=params[5], precision=params[6], developmentPotential=params[7], kind=params[8], abilities=params[9])
        db.session.add(newStand)
        db.session.commit()
        return newStand

    def updateStand(self, id, params):
        stand = Stand.query.filter_by(id=id).first()
        if params.get('name'):
            stand.name = params['name']
        if params.get('destructivePower'):
            stand.destructivePower = params['destructivePower']
        if params.get('speed'):
            stand.speed = params['speed']
        if params.get('range'):
            stand.range = params['range']
        if params.get('persistence'):
            stand.persistence = params['persistence']
        if params.get('precision'):
            stand.precision = params['precision']
        if params.get('developmentPotential'):
            stand.developmentPotential = params['developmentPotential']
        if params.get('kind'):
            stand.kind = params['kind']
        if params.get('abilities'):
            stand.abilities = params['abilities']
        db.session.commit()
        return stand

    def deleteStand(self, id):
        stand = Stand.query.filter_by(id=id).first()
        db.session.delete(stand)
        db.session.commit()
        return {'result': 'success'}

standController = StandController()