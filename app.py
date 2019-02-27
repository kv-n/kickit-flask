from flask import Flask
# importing our blueprint which is a definition
## of our view functions
from resources.shoes import shoes_api
from resources.users import users_api
from flask_cors import CORS
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
login_manager = LoginManager()

import models

import config

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

CORS(users_api, origin=["http://localhost:3000"], supports_credentials=True)
CORS(shoes_api, origin=["http://localhost:3000"], supports_credentials=True)

app.register_blueprint(shoes_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

@app.route('/')
def hello_world():
    return "Hello World"


if __name__ == '__main__':
    models.initialize()

    app.run(debug=DEBUG, port=PORT)

<<<<<<< HEAD
    # try:
    #     models.User.create_user(
    #         username='apple',
    #         email='apple@apple',
    #         password='apple'
    #     )
    # except ValueError:
    #     pass

app.run(debug=DEBUG, port=PORT)
=======
>>>>>>> 829ac8ea082290506ab18533a78c6cc7e239b1cc
