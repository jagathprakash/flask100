import os

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy import create_engine
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

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
