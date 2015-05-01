# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import Sequence
from config import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()

class Target(Base):
    __tablename__ = 'targets'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    host = Column(String)
    result = Column(String)

    def __repr__(self):
        return "<Target(host='%s', result='%s')>" % (
                             self.host,self.result)

Base.metadata.create_all(engine)