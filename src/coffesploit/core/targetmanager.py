class TargetManager(object):
    def __init__(self, rhost=None):
        self.rhost = rhost

    def set_rhost(self, rhost):
        self.rhost = rhost

    def get_rhost(self):
        return self.rhost
