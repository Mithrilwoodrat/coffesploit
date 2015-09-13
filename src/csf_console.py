# -*- coding: utf-8 -*-
from coffesploit.console import Console
from config import __basedir
from config import SQLALCHEMY_DATABASE_URI
from config import DATABASE_URI
import sqlite3
from os import path


def main():
    coffesploit = Console()
    coffesploit.main.config_from(__basedir, SQLALCHEMY_DATABASE_URI)  # config for sqlalchemy usage
    # when coffesploit run
    # check db file
    # if db not exists then create db
    if not path.exists(DATABASE_URI):
        db = sqlite3.connect(DATABASE_URI)
        db.close()
    coffesploit.start()

if __name__ == "__main__":
    main()
