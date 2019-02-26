from flask import Flask
# importing our blueprint which is a definition
## of our view functions
from resources.shoes import shoes_api
from flask_cors import CORS
import models

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.register_blueprint(shoes_api, url_prefix='/api/v1')

@app.route('/')
def hello_world():
    return "Hello World"


## true to support credentials when localhost try to connect it saying its true
CORS(shoes_api, origin=["http://localhost:3000"], supports_credentials=True)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)