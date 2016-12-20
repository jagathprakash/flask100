import os

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

MYSQL_USER_PASS="{username}:{password}".format(
        username="root",
        password=os.environ.get("MYSQL_PASSWORD", ""))

engine = create_engine("mysql+mysqldb://{mysql_user_pass}@127.0.0.1:3306/GiftExchange".format(
        mysql_user_pass=MYSQL_USER_PASS))

conn = engine.connect()

Session = sessionmaker(bind=engine)
db_session = Session()


class SurveyResults(Base):
    __tablename__ = 'Participants'
    name = Column(String)
    email = Column(String, primary_key=True)
    address = Column(Text)
    gifts = Column(Text)
    charity = Column(Text)


    def __repr__(self):
        return "<Participants(name='%s')>" % (self.name)
