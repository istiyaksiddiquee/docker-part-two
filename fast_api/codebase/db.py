import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session



user_name = os.environ.get('DB_USER_NAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
database_name = os.environ.get('DB_NAME')
port=os.environ.get('DB_PORT')

DATABASE = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (
    user_name,
    password,
    host,
    port,
    database_name,
)


ENGINE = create_engine(
    DATABASE,
    echo=True
)


session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)


Base = declarative_base()
Base.query = session.query_property()