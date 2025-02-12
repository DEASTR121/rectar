from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)


#TODO Cambiar el link de postgresql según el panel (linea 11)
#TODO Cambiar el secretkey (linea 15)s
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://rodha_user:WS71CSttlUYiTQDR6LcBqdXWBfUTWtmh@dpg-culu9n9u0jms73bgv7vg-a/rodha'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'secretKey'

CORS(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')
ma = Marshmallow(app)

@app.after_request
def apply_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response