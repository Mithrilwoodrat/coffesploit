# -*- coding: utf-8 -*-
class Help(object):
    """class to print help infomations help users use the platform"""
    def help_show(self):
        print """Usage:show [target|<tool>]
        exp:show nmap"""
    def help_use(self):
        print """Usage:use <tool>
        exp:use nmap"""
    def help_set_tartget(self):
        print """Usage:target -u url |-r rhostaddress <target>
        exp: target -u http://www.baidu.com"""
    def main_help(self):
        print """Welcome to Coffesploit
        'help target' show help about target set
        'help show' show help about 'show' options
        'plugins' show plugins list
        or just type sh command to exec
        """
    def help_set(self):
        pass
