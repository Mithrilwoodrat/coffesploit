# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI
from initdb import Target


class DBManager(object):
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_target(self, host, plugin_name, result):
        new_target = Target(host=host, plugin_name=plugin_name, result=result)
        self.session.add(new_target)
        self.session.commit()

    def query_target(self, host):
        target = self.session.query(Target).filter_by(host=host).first()
        if target:
            return {target.host: (target.plugin_name,target.result)}
        else:
            return None

# instance
dbmanager = DBManager()