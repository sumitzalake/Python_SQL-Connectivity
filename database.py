from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Correctly encoded password
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Sumit%40123@localhost:3306/Sumit_DB"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
