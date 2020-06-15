from flask import redirect, render_template, request, Response, make_response, jsonify
from webapp import app

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)