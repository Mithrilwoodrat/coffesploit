#/usr/bin/python
import ftplib
from coffesploit.plugins.pluginmanage.scanplugin import ScanPlugin
from coffesploit.plugins.pluginmanage.resultplugin import ResultPlugin


class FtpAnonymousLogin(ScanPlugin):
    def __init__(self):
        self.tool_name = "FtpAnonymousLogin"
        super(FtpAnonymousLogin, self).__init__(self.tool_name)
        self.resultparser = ResultPlugin()
        self.host = None
        self.isvulnerable = False

    def status(self):
        print "host:", self.host

    def anonlogin(self, hostname):
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login('anonymous', 'me@your.com')
            ftp.quit()
            return True
        except Exception, e:
            return False

    def run(self):
        if self.anonlogin(self.host):
            self.isvulnerable = True

    def result(self):
        if self.isvulnerable:
            print '\n[+]' + str(self.host) + 'FTP Anonymous\
            Login Succeeded.'
        else:
            print '\n[-] ' + str(self.host) + 'FTP Anonymous\
            Login Failed. '

    def set_args(self, *args):
        if len(args) == 2:
            if args[0] == 'host':
                self.host = args[1]
