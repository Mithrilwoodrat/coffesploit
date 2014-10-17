# -*- coding: utf-8 -*-
import os


class ImportPlugin(object):
    def __init__(self):
        self.plugins_list = {}
        self.path = ""
        self.config_path()
        self.parse_config()

    def config_path(self):
        if not "plugins" in os.getcwd():
            self.path = os.getcwd()+"/coffesploit/plugins/"
        else:
            self.path = os.getcwd()

    def getpath(self):
        return self.path

    #read config.ini file load plugins in config
    def parse_config(self):
        try:
            filename = self.path+"config.ini"
            conf = open(filename, "r")
            for line in conf.readlines():
                plugin_name, plugin_file, plugin_class = line.split(",")
                self.plugins_list[plugin_name] = plugin_file, plugin_class
        except IOError:
            print ("must have config file")
            print self.path
            exit(0)

    def get_plugins_list(self):
        return self.plugins_list
