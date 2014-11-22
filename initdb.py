# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from config import __basedir
from config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()
class Target(Base):
    __tablename__ = 'targets'

    host = Column(String,primary_key=True)
    result = Column(String)

    def __repr__(self):
        return "<Target(host='%s', result='%s')>" % (
                             self.host,self.result)
Base.metadata.create_all(engine)