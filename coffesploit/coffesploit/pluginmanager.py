# -*- coding: utf-8 -*-
from plugins.importplugin import ImportPlugin
import  importlib
import os


class PluginManager(object):
    def __init__(self):
        self.current_plugin_name = None
        self.current_plugin_file = None
        self.current_plugin_class = None
        self.current_plugin = None
        self.importer = ImportPlugin()

    def set_current_plugin_name(self,plugin_name):
        # if plugin name is in config file set plugin name
        plugin_list = self.importer.get_plugins_list()
        if plugin_name in plugin_list:
            self.current_plugin_name = plugin_name
            self.current_plugin_file, self.current_plugin_class = plugin_list[plugin_name]
        else:
            print 'no such plugin'

    def load_plugin(self):
        #set path to load plugin
        if not "plugins" in os.getcwd():
            path = "coffesploit.plugins."
            importfile = path+self.current_plugin_file[0:-3].lower()
        else:
            importfile = self.current_plugin_file[0:-3].lower()
        mode = importlib.import_module(importfile)
        plugin_class = getattr(mode,self.current_plugin_class)
        self.current_plugin = plugin_class()

