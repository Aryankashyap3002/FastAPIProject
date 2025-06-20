import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# create_engine connects SQLAlchemy to the MySQL database using credentials from the .env file.
# SessionLocal creates DB sessions, and Base is the base class for defining models.


# In SQLAlchemy, the engine is the starting point for any SQLAlchemy application.
# It manages the database connection and allows execution of SQL queries.
# The create_engine() function in SQLAlchemy is used to create an Engine instance.
# It establishes the connection details to the database using a connection URL.

metadata = MetaData() # Create a SQLalchemy MetaData object

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a SQLalchemy sessionmaker object

Base = declarative_base() # create a base object
