from flask import Flask
from flask_cors import CORS
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,MetaData

app = Flask(__name__, instance_relative_config=True)
CORS(app)

#load defalut config
app.config.from_object('config.default')
app.config["JSON_SORT_KEYS"] = False
app.config.from_pyfile('config.py')

#Sqlalchemy ORM model
mtadta = MetaData()
#DATABASE_URI = 'postgres+psycopg2://postgres:tatha1234@database-2.ccxp9suofmqw.us-east-2.rds.amazonaws.com:5432'
DATABASE_URL = 'postgresql://root@localhost/circle_test'

engine = create_engine(DATABASE_URL)
mtadta.reflect(engine)
Base = automap_base(metadata=mtadta)
Base.prepare()
print(Base.classes.keys())
ledger = Base.classes.ledger
session = Session(engine)

#Import a module / component using its blueprint handler 
from app.webhook_receiver.controllers.webhook_receiver_controller import blueprint as webhook_receiver

#Register Blueprint
app.register_blueprint(webhook_receiver)


