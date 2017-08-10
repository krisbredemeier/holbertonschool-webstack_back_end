#!/usr/bin/python3
from sqlalchemy import create_engine
# from sqlalchemy import drop_all
# from sqlalchemy import create_all
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os


db_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(os.environ.get('HBNB_YELP_MYSQL_USER'), os.environ.get('HBNB_YELP_MYSQL_PWD'), os.environ.get('HBNB_YELP_MYSQL_HOST'), os.environ.get('HBNB_YELP_MYSQL_DB')))


if os.environ.get('HBNB_YELP_ENV') == 'test':
    metadata.drop_all(db_engine)

metadata.create_all(db_engine)
db_session = scoped_session(sessionmaker(bind=db_engine, expire_on_commit=False))
