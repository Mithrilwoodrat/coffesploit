# -*- coding: utf-8 -*-
from coffesploit.core.target import Target
from coffesploit.core.help import Help
from coffesploit.core.pluginmanager import PluginManager
from coffesploit.core.dbmanager import DBManager

__Version__ = "0.2test"


class Coffesploit(object):
    """Main Class"""
    def __init__(self):
        self.target = Target()
        self.tool = None
        self.pluginmanager = PluginManager()
        self.helper = Help()
        self.plugin_list = self.get_plugin_list()
        self.dbmanager = DBManager()

    def config_from(self,basedir,db_uri):
        self.basedir = basedir
        self.db_uri = db_uri
        
    def set_target(self,rhost=None,url=None):
        if url is not None:
            self.target.seturl(url)
        if rhost is not None:
            self.target.setrhost(rhost)
    def set(self, arg1, arg2):
        self.pluginmanager.current_plugin.set_args(arg1,arg2)
    def show(self,arg):
        if arg == "target":
            if self.target.getrhost() is not None:
                print "ip:",self.target.getrhost(),self.dbmanager.query_target(self.target.getrhost())
        if arg == "status":
            if self.pluginmanager.current_plugin is not None:
                status = self.pluginmanager.plugin_status()
                for arg in status:
                    print arg,":",status[arg]
        if arg == "version":
            print "Currnt Version:",self.version()
        if arg == "plugins":
            for plugin in self.plugin_list:
                print self.plugin_list[plugin][0], " : ",plugin
                
    def use(self,arg):
        self.pluginmanager.load_plugin(arg)
        
    def run(self):
        self.pluginmanager.plugin_run()
        return self.pluginmanager.plugin_result()

    def main_help(self):
        return self.helper.main_help()

    def get_plugin_list(self):
        return self.pluginmanager.importer.get_plugins_list()

    def current_plugin_name(self):
        return self.pluginmanager.current_plugin_name

    def current_plugin_type(self):
        return self.pluginmanager.current_plugin_type

    def help(self,arg):
        """show help info of t"""
        if arg == "target":
            self.helper.help_set_tartget()
        if arg == "show":
            self.helper.help_show()
        if arg == "use":
            self.helper.help_use()

    def exit(self):
        exit(0)
    def version(self):
        return __Version__
