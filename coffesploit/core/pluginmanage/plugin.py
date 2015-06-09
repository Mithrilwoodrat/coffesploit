# -*- coding: utf-8 -*-
from coffesploit.core.logmanager import logmanager


class Plugin(object):
    """
    This is the base class for ALL plugins, all plugins should inherit from it
    and implement the following method :
    status result  run """

    def __init__(self, plugin_name):
        self.plugin_name = plugin_name  # pass in plugin_name in super().__init__ function

    def run(self, status):
        logmanager.puttolog('using plugin:'+self.plugin_name)

    def status(self):
        logmanager.puttolog('plugin:' + self.plugin_name + 'status')

    def result(self):
        """ reslut should return a dictionary  """
        pass
