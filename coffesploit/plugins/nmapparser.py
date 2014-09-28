# -*- coding: utf-8 -*-
from nmap import PortScanner
from testplugin import TestPlugin

class NmapParser(TestPlugin):
    def __init__(self):
        self.tool_name = "nmap"
        super(NmapParser, self).__init__("nmap")
        self.nm = PortScanner()
        self.hosts = None
        self.ports = None
        self.argments = "-sV"
    def args_status(self):
        print "hosts:",self.hosts,"\n"
        print "ports:",self.ports,"\n"
        print "argments:",self.argments,"\n"
    def start_scan(self):
        if self.hosts != None:
            self.nm.scan(self.hosts, arguments=self.argments)
            if self.ports !=None:
                self.nm.scan(self.hosts, self.ports, arguments=self.argments)
        else:
            print 'please set hosts'
            exit(0)
    def scan_result(self):
        return self.nm[self.hosts]
    def run(self):
        self.start_scan()
    def status(self):
        self.args_status()
    def result(self):
        return self.scan_result()
    def set_arg(self,arg1,arg2):
        if arg1 == "hosts":
            self.hosts = arg2
        elif arg1 == "ports":
            self.ports = arg2
        elif arg1 == "argments":
            self.argments = arg2