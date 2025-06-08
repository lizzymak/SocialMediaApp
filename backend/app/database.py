from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

#sets up connection to db
engine = create_engine(DATABASE_URL)
#used to interact w/ db in routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#base class all sql models will inherit
Base = declarative_base()