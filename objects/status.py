from tkinter import * 

class Status(Frame): 
    def __init__(self, root, user): 
        self.user = user 
        super().__init__()
        self.root = root
        
        # status 
        self.status_bar = None
        self.broker_host = '0.0.0.0'
        
        
        # titles 
        self.host_title = None 
        self.port_title = None 

        
        # Controller Init 
        self.UIinit()
        
    def UIinit(self):         
        
        status_str = "Broker IP: " + self.broker_host
        self.status_bar = Label(self.root, text=status_str, bd=1, relief = SUNKEN, anchor=W)
        self.status_bar.grid(row=20, columnspan=15)
        #self.status_bar.pack(side=BOTTOM, fill=X)
        #self.exit_button.pack(side=TOP)