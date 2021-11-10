from tkinter import * 
from win32api import *

from objects.controller import Controller 
from objects.view import View
from objects.status import Status


import os 

class User(): 
    def __init__(self):
        
        # system elements 
        self.ip = '' 
        self.date_time = '' 
        self.resolution = [] 
        self.res_str = ''
        
        # gui elements 
        self.root = None
        self.controller = None 
        self.view = None 
        self.status_bar = None 
       
        # broker needs  
        self.broker_ip = '' 
        self.broker_port = 0 
        self.broker_id_str = '' 
        
        # consumer needs 
        self.consumer = None 
        self.consumers = [] 
        
        # producer needs 
        self.producer = None 
        self.consumers = []        
        
        
    # Set broker elements 
    def set_broker_info(self): 
        
        self.broker_ip = self.controller.host_entry.get() 
        self.broker_port = self.controller.port_entry.get() 
        self.broker_id_str = str(self.broker_ip) + ":" + str(self.broker_port)

    # Run tkinter systems         
    def run(self):
    
        def get_resolution(object): 
            w = int(GetSystemMetrics(0) * .6 )
            h = int(GetSystemMetrics(1) / 2  )

            size_str = str(w) + 'x' + str(h) 

            object.resolution = [(w/3), (h/2)]
            object.res_str = size_str
        
        def boot_status(object): 
            self.status_bar = Status(object.root, self) 
            
        def open_view(object): 
            self.view = View(object.root, self)
        
        def open_controller(object): 
            self.controller = Controller(object.root, self)
        
        def root_init(object): 
            object.root=Tk()
            object.root.attributes("-topmost", True)
            object.root.title('Kafka Communications')
            #object.root.geometry(object.res_str)
            
        get_resolution(self)
        root_init(self) 
        open_controller(self) 
        open_view(self) 
        boot_status(self)

        self.root.mainloop() 

    
        