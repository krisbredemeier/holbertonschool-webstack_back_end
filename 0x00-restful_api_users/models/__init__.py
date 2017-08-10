#!/usr/bin/python3
from sqlalchemy import create_engine, case
db_engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(env['HBNB_YELP_MYSQL_USER'], env['HBNB_YELP_MYSQL_PWD'], env['HBNB_YELP_MYSQL_HOST'], env['HBNB_YELP_MYSQL_DB'])

if (env['HBNB_YELP_ENV'] == 'test'):
    drop_all(bind=None, tables=None, checkfirst=True)

create_all(bind=None, tables=None, checkfirst=True)
db_session = scope_session(sessionmaker(bind=db_engine, expire_on_commit=False))
