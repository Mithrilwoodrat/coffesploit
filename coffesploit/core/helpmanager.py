# -*- coding: utf-8 -*-
class HelpManager(object):
    """class to print help informations help users use coffesploit"""

    def __init__(self):
        self.help_list = {"show": self.help_show,
                          "use": self.help_use,
                          "target": self.help_set_tartget
        }

    def help_show(self):
        print """Usage:show [target|<tool>]
        exp:show nmap"""

    def help_use(self):
        print """Usage:use <tool>
        exp:use nmap"""

    def help_set_tartget(self):
        print """Usage:target target_address
        exp: target 192.168.1.2 """

    def main_help(self):
        print """Welcome to Coffesploit
        'help target' show help about target set
        'help show' show help about 'show' options
        'plugins' show plugins list
        or just type sh command to exec
        """

    def help_set(self):
        pass

    def gethelp(self, arg):
        if arg is None:
            self.main_help()
        if arg in self.help_list:
            self.help_list[arg]()
        else:
            print "no help info about",arg






