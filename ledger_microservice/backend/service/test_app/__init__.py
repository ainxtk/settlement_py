from flask import Flask
from flask_cors import CORS
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,MetaData

test_app = Flask(__name__, instance_relative_config=True)
CORS(test_app)

#load defalut config
test_app.config.from_object('config.default')
test_app.config["JSON_SORT_KEYS"] = False
test_app.config.from_pyfile('config.py')

#Sqlalchemy ORM model
mtadta = MetaData()
DATABASE_URI = 'postgresql://root@localhost/circle_test'
engine = create_engine(DATABASE_URI)
mtadta.reflect(engine)
Base = automap_base(metadata=mtadta)
Base.prepare()
print(Base.classes.keys())
ledger = Base.classes.ledger

session = Session(engine)

#Import a module / component using its blueprint handler 
from test_app.webhook_receiver.controllers.webhook_receiver_controller import blueprint as webhook_receiver

#Register Blueprint
test_app.register_blueprint(webhook_receiver)


