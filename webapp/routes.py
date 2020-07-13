from flask import redirect, render_template, request, Response, make_response, jsonify
from webapp import app
from .controllers import standController, userController
from .models import Stand, User

standParams = Stand.getAttributesAsList()
userParams = User.getAttributesAsList()

def parseParams(expectedParamList):
    params = []
    if not request:
        return None

    for param in request.form:
        if param not in expectedParamList:
            return None

    for param in expectedParamList:
        if not request.form[param]:
            return None
        params.append(request.form[param])

    return params

def parseOptionalParams(potentialParamList):
    fieldsToUpdate = []
    params = []

    # if a param that is allowed is in the request then it will marked as a field to update for the request
    for param in potentialParamList:
        if request.form.get(param):
            fieldsToUpdate.append(param)
            params.append(request.form[param])

    # return which fields should be changed and the new values for said fields
    return dict(zip(fieldsToUpdate, params))

def parseArgs(argsList):
    queryFields = []
    argumentValues = []

    for arg in argsList:
        if request.args.get(arg):
            queryFields.append(arg)
            argumentValues.append(request.args[arg])

    return dict(zip(queryFields, argumentValues))

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/stando/api/v1.0', methods=['GET'])
def root():
    return jsonify({'Welcome': 'This is the home page'})

@app.route('/stando/api/v1.0/users/<int:id>', methods=['GET'])
def getUser(id):
    return jsonify(userController.getUser(id).asDict())

@app.route('/stando/api/v1.0/users', methods=['GET'])
def getUsers():
    args = parseArgs(User.getAttributesAsList())
    if len(args) > 0:
        return jsonify(users=[user.asDict() for user in userController.getUsers(args)])
    return jsonify(users=[user.asDict() for user in userController.getUsers()])

@app.route('/stando/api/v1.0/users', methods=['POST'])
def createUser():
    params = parseParams(userParams)
    return jsonify(userController.createUser(params).asDict())

@app.route('/stando/api/v1.0/users/<int:id>', methods=['PUT'])
def updateUser(id):
    params = parseOptionalParams(userParams)
    return jsonify(userController.updateUser(id, params).asDict())

@app.route('/stando/api/v1.0/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    return jsonify(userController.deleteUser(id))

@app.route('/stando/api/v1.0/stands/<int:id>', methods=['GET'])
def getStand(id):
    return jsonify(standController.getStand(id).asDict())

@app.route('/stando/api/v1.0/stands', methods=['GET'])
def getStands():
    args = parseArgs(Stand.getAttributesAsList())
    if len(args) > 0:
        return jsonify(stands=[stand.asDict() for stand in standController.getStands(args)])
    return jsonify(stands=[stand.asDict() for stand in standController.getStands()])

@app.route('/stando/api/v1.0/stands', methods=['POST'])
def createStand():
    params = parseParams(standParams)
    return jsonify(standController.createStand(params).asDict())

@app.route('/stando/api/v1.0/stands/<int:id>', methods=['PUT'])
def updateStand(id):
    params = parseOptionalParams(standParams)
    return jsonify(standController.updateStand(id, params).asDict())

@app.route('/stando/api/v1.0/stands/<int:id>', methods=['DELETE'])
def deleteStand(id):
    return jsonify(standController.deleteStand(id))