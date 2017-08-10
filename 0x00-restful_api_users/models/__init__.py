#!/usr/bin/python3
from sqlalchemy import create_engine
import os

db_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(os.environ.get('HBNB_YELP_MYSQL_USER'), os.environ.get('HBNB_YELP_MYSQL_PWD'), os.environ.get('HBNB_YELP_MYSQL_HOST'), os.environ.get('HBNB_YELP_MYSQL_DB')))

if os.environ.get('HBNB_YELP_ENV') == 'test':
    drop_all(bind=None, tables=None, checkfirst=True)

create_all(bind=None, tables=None, checkfirst=True)
db_session = scope_session(sessionmaker(bind=db_engine, expire_on_commit=False))
