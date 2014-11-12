# -*- coding: utf-8 -*-
import os


class DataManager(object):
    """  this class is designed to keep data,such as password dictionary"""
    def __init__(self):
        self.path = None
        self.pwdfile = None
        self.config_path()

    def config_path(self):
        if not "plugins" in os.getcwd():
            self.path = os.getcwd()+"/coffesploit/data/"
        else:
            self.path = os.getcwd()

    def get_file(self, filetype):
        if filetype == "password":
            self.pwdfile = self.path + "pwd.txt"
            if os.path.isfile(self.pwdfile):
                return self.pwdfile
            else:
                return None
        else:
            return None


