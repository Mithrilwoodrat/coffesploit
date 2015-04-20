# -*- coding: utf-8 -*-
from Queue import Queue


class LogManager(object):
    def __init__(self):
        self.log = Queue()

    def puttolog(self,message):
        self.log.put_nowait(message)

    def getlog(self):
        if self.log:
            return self.log.get_nowait()
        else:
            return None

#instance
logmanager = LogManager()