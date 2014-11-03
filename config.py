import os


__basedir = os.path.abspath(os.path.dirname(__file__))
__dbname = "coffesploit.db"
DATABASE_URI = os.path.join(__basedir+"/coffesploit/db",__dbname)
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(__basedir+"/coffesploit/db",__dbname)
CSRF_ENABLE = True
SECRET_KEY = "coffesploit"