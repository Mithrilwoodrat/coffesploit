# -*- coding: utf-8 -*-


class ResultPlugin(object):
    def __init__(self):
        self.address = None
        self.hostname = None
        self.state = None
        self.openports = []
        self.servers = {}

    def set_address(self, address):
        self.address = address

    @property
    def get_address(self):
        return self.address

    def set_openports(self, ports):
        self.openports = ports

    @property
    def get_openports(self):
        return self.openports

    def set_servers(self,servers):
        self.servers = servers

    @property
    def get_servers(self):
        return  self.servers

    def set_hostname(self,hostname):
        self.hostname = hostname

    @property
    def get_hostname(self):
        return self.hostname

    def set_state(self,state):
        self.state = state

    @property
    def get_state(self):
        return self.state
