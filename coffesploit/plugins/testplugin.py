# -*- coding: utf-8 -*-

class TestPlugin(object):
    """
    This is the base class for ALL plugins, all plugins should inherit from it
    and implement the following method :
    status result  run """

    def __init__(self, plugin_name):
        self.plugin_name = plugin_name

    def run(self):
        pass

    def status(self):
        pass

    def result(self):
        pass
