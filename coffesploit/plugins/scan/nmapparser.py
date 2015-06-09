# -*- coding: utf-8 -*-
from nmap import PortScanner  # use python nmap parse lib
from coffesploit.core.pluginmanage.scanplugin import ScanPlugin
from coffesploit.core.pluginmanage.resultplugin import ResultPlugin


class NmapParser(ScanPlugin):
    def __init__(self):
        self.tool_name = "nmap"
        super(NmapParser, self).__init__("nmap")
        self.nm = PortScanner()
        self.hosts = None
        self.ports = None
        self.arguments = "-sV"
        self.resultparser = ResultPlugin()
        
    def args_status(self):
        return {"hosts": self.hosts, "ports": self.ports, "arguments": self.arguments}
        
    def start_scan(self):
        if self.hosts is not None:
            self.nm.scan(self.hosts, arguments=self.arguments)
            if self.ports is not None:
                self.nm.scan(self.hosts, self.ports, arguments=self.arguments)
        else:
            print 'please set hosts'
            
    def scan_result(self):
        if self.hosts is not None and self.nm.all_hosts():
            return self.nm[self.hosts]
    
    def run(self, status):
        if status and len(status) == 3:
            self.hosts = status['hosts']
            self.ports = status['ports']
            self.arguments = status['arguments']
        super(NmapParser, self).run(status)
        print "scanning .................\n", "please wait!\n"
        self.start_scan()
        
    def status(self):
        return self.args_status()

    def result(self):
        if self.scan_result() is not None:
            self.resultparser.set_hostname(self.scan_result().hostname())
            self.resultparser.set_state(self.scan_result().state())
            self.resultparser.set_address(self.hosts)
            self.resultparser.set_openports(self.scan_result().all_tcp())
            if u'tcp' in self.scan_result():
                self.resultparser.set_servers(self.scan_result()[u'tcp'])
            self.resultparser.log_result()
        return self.scan_result()
