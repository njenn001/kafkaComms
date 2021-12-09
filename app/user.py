import matplotlib
matplotlib.use('Agg')

from tkinter import * 
import os 

from controller import Controller 
from view import View
from status import Status


class User(): 
    def __init__(self):
        
        # Comm elements  
        self.root = None
        self.controller = None 
        self.view = None 
        self.status_bar = None 
       
        # broker needs  
        self.broker_ip = '' 
        self.broker_port = ''
        self.broker_id_str = '' 
        
        # consumer needs 
        self.consumer = None 
        self.consumers = [] 
        
        # producer needs 
        self.producer = None 
        self.producers = []  
        
    
    # GET / SET root 
    # GET / SET controller 
    # GET / SET view
    # GET / SET status bar 
    # GET / SET broker ip 
    # GET / SET broker port
    # GET / SET broker id string 
    # GET / SET consumer 
    # GET / SET consumers
    # GET / SET producer 
    # GET / SET producers
    

    # Throw exception 
    def throw_exec(self, msg): 
        if msg == 'p_args': 
            raise Exception("Missing production arguments")
        elif msg == 'c_args': 
            raise Exception("Missing consumption arguments")
        elif msg == 'gui': 
            raise Exception("Ensure display element")
                  
        
    # Set broker elements 
    def set_broker_info(self): 
        
        self.broker_ip = self.controller.host_entry.get() 
        self.broker_port = self.controller.port_entry.get() 
        self.broker_id_str = str(self.broker_ip) + ":" + str(self.broker_port)

    # Run tkinter systems         
    def run(self):
        
        # Boot status bar  
        def boot_status(object): 
            self.status_bar = Status(object.root, self) 
            
        # Open message view 
        def open_view(object): 
            self.view = View(object.root, self)
        
        # Open comms controller 
        def open_controller(object): 
            self.controller = Controller(object.root, self)
        
        # Init Tk 
        def root_init(object): 
            
            if os.environ.get('DISPLAY','') == '':
                print('no display found. Using :0.0')
                os.environ.__setitem__('DISPLAY', ':0.0')
                
            object.root=Tk()
            object.root.attributes("-topmost", True)
            object.root.title('Kafka Communications')
            
        root_init(self) 
        open_controller(self) 
        open_view(self) 
        boot_status(self)

        self.root.mainloop() 

        