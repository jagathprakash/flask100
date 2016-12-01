import os

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

MYSQL_USER_PASS="{username}:{password}".format(
        username="root",
        password=os.environ.get("MYSQL_PASSWORD", ""))

engine = create_engine("mysql+mysqldb://{mysql_user_pass}@127.0.0.1:3306/ArchiveSurvey".format(
        mysql_user_pass=MYSQL_USER_PASS))

conn = engine.connect()

Session = sessionmaker(bind=engine)
db_session = Session()


class SurveyResults(Base):
    __tablename__ = 'SurveyResults'
    id = Column(Integer, primary_key=True)
    slack = Column(String)
    choice1 = Column(Integer)
    choice2 = Column(Integer)
    choice3 = Column(Integer)
    choice4 = Column(Integer)
    choice5 = Column(Integer)
    general = Column(String)

    def __repr__(self):
        return "<SurveyResult(user='%s')>" % (self.slack)
