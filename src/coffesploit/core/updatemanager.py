import urllib2
import os
from config import EXP_FOLDER
from config import UPDATE_SERVER
from config import RESOURCES_URL
from config import DOWNLOAD_URL
from config import DES_KEY
from coffesploit.tools.des import DES
from coffesploit.core.logmanager import logmanager

class UpdateManager(object):
    def __init__(self):
        self.update_list = []
        self.file_list = os.listdir(EXP_FOLDER)
    @staticmethod
    def is_update_server_alive():
        try:
            if urllib2.urlopen(UPDATE_SERVER):
                return True
            else:
                return False
        except Exception, e:
            logmanager.puttolog('update server is not alive')

    def fetch_update_list(self):
        print 'fetching  list from update server'
        try:
            l = urllib2.urlopen(RESOURCES_URL)
            l = eval(l.read())
            self.update_list = l['list']
        except Exception, e:
            print e

    def get_update_list(self):
        return self.update_list

    def download_exps(self):
        if self.file_list == self.update_list:
            logmanager.puttolog('already the lasted version')
            return
        for exp in self.update_list:
            if exp not in self.file_list:
                download_url = DOWNLOAD_URL+exp+'/'
                try:
                    uri = urllib2.urlopen(download_url)
                    data = uri.read()
                    with open(EXP_FOLDER+exp, 'w') as f:
                        des = DES()
                        des.input_key(DES_KEY)
                        data= des.decode(data)
                        f.write(data)
                        f.close()
                    logmanager.puttolog('download exp '+exp)
                except Exception, e:
                    print e
                    logmanager.puttolog('download '+exp+' failed')


#if __name__ == "__main__":
#    um = UpdateManager()
#    um.fetch_update_list()
#    print um.get_update_list()
#    um.download_exps()