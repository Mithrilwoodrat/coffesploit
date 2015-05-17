# -*- coding: utf-8 -*-
from coffesploit.core.target import Target
from coffesploit.core.helpmanager import HelpManager
from coffesploit.core.pluginmanager import PluginManager
from coffesploit.core.dbmanager import dbmanager
from coffesploit.core.logmanager import logmanager
from coffesploit.core.updatemanager import UpdateManager


__Version__ = "0.2test"


class Coffesploit(object):
    """Main Class"""

    def __init__(self):
        self.target = Target()
        self.tool = None
        self.pluginmanager = PluginManager()
        self.helper = HelpManager()
        self.plugin_list = self.get_plugin_list()
        self.updatemanager = UpdateManager()

    @staticmethod
    def version():
        return __Version__

    def config_from(self, basedir, db_uri):
        self.basedir = basedir
        self.db_uri = db_uri

    def set_target(self, rhost):
        self.target.setrhost(rhost)

    def set(self, arg1, arg2):
        self.pluginmanager.current_plugin.set_args(arg1, arg2)

    def show(self, arg):
        if arg == "target":
            if self.target.getrhost() is not None:
                print "ip:", self.target.getrhost(), dbmanager.query_target(self.target.getrhost())
        if arg == "status":
            if self.pluginmanager.current_plugin is not None:
                status = self.pluginmanager.plugin_status()
                for arg in status:
                    print arg, ":", status[arg]
        if arg == "version":
            print "Currnt Version:", self.version()
        if arg == "plugins":
            for plugin in self.plugin_list:
                print self.plugin_list[plugin][0], " : ", plugin

    def use(self, arg):
        if arg in self.plugin_list:
            self.pluginmanager.load_plugin(arg)
        else:
            print "plugin is not existed"

    def run(self):
        self.pluginmanager.plugin_run()
        logmanager.puttolog(self.pluginmanager.plugin_result())

    def get_result(self):
        result = ""
        while (not logmanager.log.empty()):
            result += '\n'+logmanager.getlog()
        return result

    def get_plugin_list(self):
        return self.pluginmanager.importer.get_plugins_list()

    def current_plugin_name(self):
        return self.pluginmanager.current_plugin_name

    def current_plugin_type(self):
        return self.pluginmanager.current_plugin_type

    def help(self, arg=None):
        """show help info of arg"""
        self.helper.gethelp(arg)

    def update(self):
        self.updatemanager.fetch_update_list()
        print 'get update list', self.updatemanager.get_update_list()
        if self.updatemanager.get_update_list() is not []:
            self.updatemanager.download_exps()
        else:
            print 'update failed'
            logmanager.puttolog('update failed')

    def exit(self):
        exit(0)

