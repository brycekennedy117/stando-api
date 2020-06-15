from flask import Flask

app = Flask(__name__, template_folder='view')

from webapp import routes