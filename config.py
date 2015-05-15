import os


__basedir = os.path.abspath(os.path.dirname(__file__))
__dbname = "coffesploit.db"
__pwdfilename = "pwd.txt"
EXP_FOLDER = os.path.join(__basedir+"/coffesploit/exps/")
DATABASE_URI = os.path.join(__basedir + "/coffesploit/db", __dbname)
PWDFILE_URI = os.path.join(__basedir + "/coffesploit/data", __pwdfilename)
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(__basedir+"/coffesploit/db",__dbname)
CSRF_ENABLE = True
SECRET_KEY = "coffesploit"
UPLOAD_FOLDER = os.path.join(__basedir + "/coffesploit/plugins/")
ALLOWED_EXTENSIONS = set(['py'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

UPDATE_SERVER = "http://127.0.0.1:5000/"
RESOURCES_URL = UPDATE_SERVER+'resources'
DOWNLOAD_URL = UPDATE_SERVER+'download/'