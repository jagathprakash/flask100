import os

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy import create_engine
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

MYSQL_USER_PASS="{username}:{password}".format(
        username="root",
        password=os.environ.get("MYSQL_PASSWORD", ""))

MYSQL_DATABASE="mydb"
MYSQL_HOST_PORT="127.0.0.1:3306"

engine = create_engine("mysql+mysqldb://{mysql_user_pass}@{mysql_host_port}/{mysql_database}".format(
        mysql_user_pass=MYSQL_USER_PASS,
        mysql_host_port=MYSQL_HOST_PORT,
        mysql_database=MYSQL_DATABASE))

conn = engine.connect()

Session = sessionmaker(bind=engine)
db_session = Session()


class Registration(Base):
    __tablename__ = 'Registration'
    email = Column(String, primary_key=True)
    FirstName = Column(String)
    FamilyName = Column(String)
    cost = Column(Integer)
    donation = Column(Integer)
    paid = Column(TINYINT)
    Address = Column(String)
    State = Column(String)
    members = relationship("Members")


class Members(Base):
    __tablename__ = 'Members'
    MemberFName = Column(String, primary_key=True)
    MemberLName = Column(String, primary_key=True)
    RegistrationEmail = Column(String, ForeignKey('Registration.email'), primary_key=True)
