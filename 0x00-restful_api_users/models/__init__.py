#!/usr/bin/python3
'''
Create an object called db_engine, an instance of a SQLAlchemy Engine object,
by using create_engine:
you must use the mysql+mysqldb engine
MySQL host, user, password and database
must be defined as environment variables:
host: HBNB_YELP_MYSQL_HOST
user: HBNB_YELP_MYSQL_USER
password: HBNB_YELP_MYSQL_PWD
database: HBNB_YELP_MYSQL_DB
If HBNB_YELP_ENV=test, drop all tables by using drop_all
Create all tables by using create_all
Create an object called db_session, an instance of SQLAlchemy Session,
by using scoped_session and sessionmaker:
bind option must be set to the db_engine object
expire_on_commit option must be set to False
'''

from sqlalchemy import create_engine
from sqlalchemy import schema
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import *

metadata = schema.MetaData()

db_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(os.environ.get('HBNB_YELP_MYSQL_USER'), os.environ.get('HBNB_YELP_MYSQL_PWD'), os.environ.get('HBNB_YELP_MYSQL_HOST'), os.environ.get('HBNB_YELP_MYSQL_DB')))
Base.metadata.bind = db_engine

if os.environ.get('HBNB_YELP_ENV') == 'test':
    drop_all()

Base.metadata.create_all()
db_session = scoped_session(sessionmaker(bind=db_engine, expire_on_commit=False))
