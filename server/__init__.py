# -*- coding: utf-8 -*-
import os
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from config import __basedir
from coffesploit.core.coffesplot import Coffesploit


csfserver = Flask(__name__)
csfserver.config.from_object('config')
main = Coffesploit()


from server import views, models
