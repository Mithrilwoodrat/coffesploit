# -*- coding: utf-8 -*-
from nmap import PortScanner
#use python nmap parse lib
from testplugin import TestPlugin
from resultplugin import ResultPlugin

class NmapParser(TestPlugin):
    def __init__(self):
        self.tool_name = "nmap"
        super(NmapParser, self).__init__("nmap")
        self.nm = PortScanner()
        self.hosts = None
        self.ports = None
        self.argments = "-sV"
        self.resultparser = ResultPlugin()
        
    def args_status(self):
        print "hosts:", self.hosts, "\n"
        print "ports:", self.ports, "\n"
        print "argments:", self.argments, "\n"
        
    def start_scan(self):
        if self.hosts is not None:
            self.nm.scan(self.hosts, arguments=self.argments)
            if self.ports is not None:
                self.nm.scan(self.hosts, self.ports, arguments=self.argments)
        else:
            print 'please set hosts'
            
    def scan_result(self):
        if self.hosts is not None:
            return self.nm[self.hosts]
    
    def run(self):
        super(NmapParser, self).run()
        print "scanning .................\n", "please wait!\n"
        self.start_scan()
        
    def status(self):
        self.args_status()

    def result(self):
        if self.scan_result() is not None:
            self.resultparser.set_hostname(self.scan_result().hostname())
            self.resultparser.set_state(self.scan_result().state())
            self.resultparser.set_address(self.hosts)
            self.resultparser.set_openports(self.scan_result().all_tcp())
            if self.scan_result().has_key(u'tcp'):
                self.resultparser.set_servers(self.scan_result()[u'tcp'])

            print "hostname:", self.resultparser.get_hostname
            print "address:", self.resultparser.get_address
            print "state is :", self.resultparser.get_state
            print "open ports:", self.resultparser.get_openports
            print "servers:", self.resultparser.get_servers, "\n"
    
    def set_arg(self, arg1, arg2):
        if arg1 == "hosts":
            self.hosts = arg2
        elif arg1 == "ports":
            self.ports = arg2
        elif arg1 == "argments":
            self.argments = arg2
