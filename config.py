import os


__basedir = os.path.abspath(os.path.dirname(__file__))
__dbname = "coffesploit.db"
__pwdfilename = "pwd.txt"
DATABASE_URI = os.path.join(__basedir + "/coffesploit/db", __dbname)
PWDFILE_URI = os.path.join(__basedir + "/coffesploit/data", __pwdfilename)
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(__basedir+"/coffesploit/db",__dbname)
CSRF_ENABLE = True
SECRET_KEY = "coffesploit"