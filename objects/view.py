from tkinter import *
import os  

import math

class View(Frame): 

    def __init__(self, root, user):
        self.user = user
        super().__init__(width=self.user.resolution[0], height=(self.user.resolution[1]), borderwidth=1)
        self.root = root
        
        
        # status 
        self.status_bar = None
        self.broker_host = '0.0.0.0'

        # frames 
        self.button_frame = None


        # buttons 
        self.start_button = None 
        self.stop_button = None 
        self.close_button = None 
        self.exit_button = None 

        # titles 
        self.broker_entry_l = None

        # entries 
        self.broker_entry = None

        # Controller Init 
        self.UIinit()

    def UIinit(self): 
        def close(object):
            self._running = False
            os.sys.exit(0)

        self.pack(side=RIGHT, expand=True)
        self.pack_propagate(0)

        status_str = "Broker IP: " + self.broker_host
        self.status_bar = Label(self, text=status_str, bd=1, relief = SUNKEN, anchor=W)

        self.status_bar.pack(side=BOTTOM, fill=X)