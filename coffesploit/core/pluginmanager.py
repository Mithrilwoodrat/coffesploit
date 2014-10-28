# -*- coding: utf-8 -*-
import importlib
import sys
from coffesploit.plugins.pluginmanage.importplugin import ImportPlugin



class PluginManager(object):
    """该类负责加载插件,提供插件运行和插件结果函数.
    The Class is designed to load plugin at runtime,
    and give api to run the plugin ,get the result of the plugin.
    """
    def __init__(self):
        self.current_plugin_name = None
        self.current_plugin_file = None
        self.current_plugin_class = None
        self.current_plugin_type = None
        self.current_plugin = None
        self.importer = ImportPlugin()

    def set_current_plugin_name(self, plugin_name):
        """if plugin name is in config file set plugin name
        调用importer的函数从配置文件中读取插件名称
        """
        plugin_list = self.importer.get_plugins_list()
        if plugin_name in plugin_list:
            self.current_plugin_name = plugin_name
            self.current_plugin_type, self.current_plugin_file, self.current_plugin_class = plugin_list[plugin_name]
        else:
            print 'no such plugin'

    def load_plugin(self,plugin):
        """set path to load plugin
        从importplugin 中获取插件所在绝对路径,使用import_moudle加载
        """
        if len(plugin.split("/")) == 1:
            plugin_name = plugin
        elif len(plugin.split("/")) == 2:
            plugin_name = plugin.split("/")[1]
        else:
            print "no such plugin!"
            exit(1)
        self.set_current_plugin_name(plugin_name)
        if sys.argv[0] != self.importer.getpath():
            importfile = "coffesploit.plugins." + self.current_plugin_type\
                         + "." +self.current_plugin_file[0:-3].lower()
        else:
            importfile = self.current_plugin_type + "." +self.current_plugin_file[0:-3].lower()
        try:
            mode = importlib.import_module(importfile)
        except ImportError:
            print "can't import : ",importfile
            exit(1)
        plugin_class = getattr(mode, self.current_plugin_class)
        self.current_plugin = plugin_class()

    def plugin_run(self):
        """run current plugin"""
        if self.current_plugin is not None:
            self.current_plugin.run()

    def plugin_result(self):
        """get the result of the plugin"""
        if self.current_plugin is not None:
            self.current_plugin.result()

    def plugin_status(self):
        self.current_plugin.status()
