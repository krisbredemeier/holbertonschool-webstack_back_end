#!/usr/bin/python3
from sqlalchemy import create_engine
db_engine = create_engine("mysql[+mysqldb]://HBNB_YELP_MYSQL_USER:HBNB_YELP_MYSQL_PWD@HBNB_YELP_MYSQL_HOST/HBNB_YELP_MYSQL_DB")
if HBNB_YELP_ENV=test:
    drop_all(bind=None, tables=None, checkfirst=True)
create_all(bind=None, tables=None, checkfirst=True)

db_session = sessionmaker(bind=db_engine, expire_on_commit=False)
