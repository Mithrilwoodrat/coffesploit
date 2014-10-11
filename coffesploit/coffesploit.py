# -*- coding: utf-8 -*-
from coffesploit.console import Console
import config


def main():
    coffesploit = Console(config.__basedir)
    coffesploit.start()

if __name__ == "__main__":
    main()
