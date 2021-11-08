from objects.producer import Producer


from tkinter import *

import os  
import math

class Controller(Frame): 

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
        self.message_button = None
        self.stream_button = None
        self.get_button = None 
        self.listen_button = None
        self.test_button = None
        
        self.start_button = None 
        self.stop_button = None 
        self.close_button = None 

        # titles 
        self.broker_entry_l = None

        # entries 
        self.broker_entry = None

        # Controller Init 
        self.UIinit()

    def UIinit(self): 
        
        def init_input_frames(object): 
            print() 
        
        def init_button_frames(object):
            self.button_frame = Frame(self.root, borderwidth=2, border=1)
            self.button_frame.grid(row=0, column=1)
            
            self.message_button = Button(self.button_frame, text="Message", command= lambda:close(self), width=15)
            self.stream_button = Button(self.button_frame, text="Stream", command= lambda:close(self), width=15)
            self.get_button = Button(self.button_frame, text="Get", command= lambda:close(self), width=15) 
            self.listen_button = Button(self.button_frame, text="Listen", command= lambda:close(self), width=15)
            self.test_button = Button(self.button_frame, text="Test", command= lambda:close(self), width=15)
            
            self.start_button = Button(self.button_frame, text="Start/Send", command= lambda:close(self), width=15)
            self.stop_button = Button(self.button_frame, text="Stop", command= lambda:close(self), width=15)
            self.close_button = Button(self.button_frame, text="Close", command= lambda:close(self), width=15)
            
            self.message_button.grid(row=0, column=3)
            self.stream_button.grid(row=0, column=5)
            self.get_button.grid(row=2, column=3)            
            self.listen_button.grid(row=2, column=5)
            self.test_button.grid(row=0, column=7)
            
            self.start_button.grid(row=4, column=3)
            self.stop_button.grid(row=4, column=5)
            self.close_button.grid(row=2, column=7)
            
            
        def close(object):
            self._running = False
            os.sys.exit(0)

        #self.gri(side=RIGHT, expand=True)
        #self.pack_propagate(0)
        
        init_button_frames(self)

        status_str = "Broker IP: " + self.broker_host
        self.status_bar = Label(self.root, text=status_str, bd=1, relief = SUNKEN, anchor=W)
        self.status_bar.grid(row=10, columnspan=15)
        #self.status_bar.pack(side=BOTTOM, fill=X)
        #self.exit_button.pack(side=TOP)