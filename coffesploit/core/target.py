# -*- coding: utf-8 -*-

class Target(object):
    """set Target or get Target info"""
    def __init__ (self, rhost=None, url=None):
        self.rhost = rhost
        self.url = url
    def parseurl(self,url):
        pass
    def setrhost(self,rhost):
        self.rhost = rhost
    def getrhost(self):
        return  self.rhost
    def seturl(self,url):
        self.url = url


