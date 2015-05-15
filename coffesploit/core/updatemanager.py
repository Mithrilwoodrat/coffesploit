import urllib2
from config import EXP_FOLDER
from config import UPDATE_SERVER
from config import RESOURCES_URL
from config import DOWNLOAD_URL


class UpdateManager(object):
    def __init__(self):
        self.update_list = self.fetch_update_list()

    @staticmethod
    def is_update_server_alive():
        try:
            urllib2.urlopen(UPDATE_SERVER)
        except Exception, e:
            print e
            print 'update server is not alive'

    @staticmethod
    def fetch_update_list():
        l = urllib2.urlopen(RESOURCES_URL)
        l = eval(l.read())
        update_list = l['list']
        return update_list

    def get_update_list(self):
        return self.update_list

    def download_exps(self):
        for exp in self.update_list:
            download_url = DOWNLOAD_URL+exp+'/'
            try:
                uri = urllib2.urlopen(download_url)
                data = uri.read()
                with open(EXP_FOLDER+exp, 'w') as f:
                    f.write(data)
            except Exception, e:
                print e


if __name__ == "__main__":
    um = UpdateManager()
    print um.get_update_list()
    um.download_exps()
