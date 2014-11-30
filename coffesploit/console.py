# -*- coding: utf-8 -*-
import os
import sys
from coffesploit.core.coffesplot import Coffesploit


class Console(object):
    def __init__(self):
        self.main = Coffesploit()
        self.history = []
        self.cmd = None

    def get_input(self):
        sys.stdout.write(self.main.pluginmanager.current_plugin_type + "/" +
        self.main.pluginmanager.current_plugin_name + '>')
        self.cmd = sys.stdin.readline().strip()
        self.history.append(self.cmd)

    def start(self):
        self.banner()
        while 1:
            try:
                # show plugin name in shell
                if self.main.pluginmanager.current_plugin_name:
                    self.cmd = raw_input(self.main.pluginmanager.current_plugin_type + "/" +
                                         self.main.pluginmanager.current_plugin_name + '>')
                    self.history.append(self.cmd)
                else:
                    self.cmd = raw_input('>')
                    self.history.append(self.cmd)
                self.parsecmd(self.cmd)
            except EOFError:
                self.exit()
            except KeyboardInterrupt:
                print "\nKeyboardInterrupt"
                self.exit()

    def banner(self):
        print ("""

            Welcome to CoffeSploit :)


                   .:::::..        ..
             :jtii;;;,,,,::::::::.........
             ... :ii;,,,,,:::::::::::::,it
             ..................::::,,;ittf
             :................::::,,,;ittf
             :................::::,,,;ittfL;,::
             ::...............::::,,,;iitfiL  j:
              :.............::::::,,,;iitf.    i,
              :..............::::,,,;;iitL     j:
              ::.............::::,,,;;ittL     .:
              ::............:::::,,,;;itf      t:
              :.............:::::,,,;;itf      :;
               ::...........::::,,,;;;ijL     ,:
               ::...........:::::,,,;itj.    ,:j
            ,,,,::.........::::::,,;;itftttt::j
         ,,,,,;;:::........:::::,,,;itjGjf, :ftt
       ,;;;;;;;;,::::....::::::,,,;;ijLi,,,ijjti;;
       ;;;;;;;;;;,::::::::::::,,,;;itfDiiGfjjti;;,....
        i;;;;;;;ii,::::::::::,,,;;itfDDGLffjti;;;;:...
         ,i;;iiiiti,,,:::::,,,,;;itfGDDGLfjtii;:,,::::
         j   iiittjfi;,,,,,,;;;itjfGEDGLftti..tti;,,::
        ..:iji,     tEGfjtttjjfLGE#E;   .:jLGDGfji;,,:
       ..:,;tjGfjtiii;,,:::..::,,;iitjffLGKEEDGLfti;,:
       ..:,;itjfGDGGLffjjjjjjjjjffLLGDEWKKEEDGLfjti;,:
       ...:,,;itjfLDEfijGEKKKKKKDLLEWKEEEDGGLfftti;,::
         ..::,,;iitjffLGGDDDEEEDDDDDGGGLLLffjtii;,,::.
           ...::,,,;;iittjjjjjfffjjjjjjttii;;,,:::....



                                              """)

    def exit(self):
        print("\n good bye! \n")
        self.main.exit()
        exit(0)

    def parsecmd(self, cmd):
        if cmd == "help":
            self.main.main_help()
        elif cmd == "show":
            self.main.help("show")
        elif cmd == "exit":
            self.exit()
        elif cmd == "target":
            self.main.help("target")
        elif cmd == "version":
            print self.main.version()
        elif cmd == "use":
            self.main.help("use")
        elif cmd == "banner":
            self.banner()
        elif cmd == "run":
            print self.main.run()
        elif len(cmd.split(" ")) >= 2:
            args = cmd.split(" ")
            command = args[0]
            if command == "target" and len(args) == 3:
                if args[1] == "-u":
                    self.main.set_target(url=args[2])
                elif args[1] == "-r":
                    self.main.set_target(rhost=args[2])
                else:
                    print "error"
                    self.main.help("target")
            if command == "set":
                if len(args) == 3:
                    self.main.set(args[1], args[2])
                else:
                    print "error"
                    self.main.help("set")
            elif command == "help":
                self.main.help(args[1])
            elif command == "show":
                self.main.show(args[1])
            elif command == "use":
                #to load plugin
                self.main.use(args[1])
        else:
            os.system(cmd)


