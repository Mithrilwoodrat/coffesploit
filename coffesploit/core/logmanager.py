# -*- coding: utf-8 -*-
from Queue import Queue


class LogManager(object):
    def __init__(self):
        self.log = Queue()

    def puttolog(self,message):
        self.log.put(message)

    def getlog(self):
        return self.log.get()