# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import Column, Integer, String
from config import __basedir
from config import SQLALCHEMY_DATABASE_URI
from config import DATABASE_URI
import sqlite3
from os import path


class DBManager(object):
    def __init__(self):
        pass
