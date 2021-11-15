from tkinter import * 

class Status(Frame): 
    def __init__(self, root, user): 
        self.user = user 
        super().__init__()
        self.root = root
        
        # status 
        self.status_bar = None 
        self.connection_status = ''
        self.action_status = FALSE 
                
        # Status Bar Init 
        self.UIinit()

    # Show action status 
    def refresh_action(self, status): 
        if not status: 
            self.action_status = 'FALSE'
        else: 
            self.action_status = 'TRUE'
        
        self.status_bar.config(text= "Broker IP:    " + self.user.broker_ip + "            Broker Port:    " + str(self.user.broker_port) + "           Connection Status:  " + str(self.connection_status) + "           Action Status:  " + str(self.action_status))  

    # show connection status 
    def refresh_status(self, status): 
        if not status: 
            self.connection_status = 'FALSE'
        else: 
            self.connection_status = 'TRUE'
        
        self.status_bar.config(text= "Broker IP:    " + self.user.broker_ip + "            Broker Port:    " + str(self.user.broker_port) + "           Connection Status:  " + str(self.connection_status) + "           Action Status:  " + str(self.action_status))  
        
    # Init status bar 
    def UIinit(self):         
        
        status_str = "Broker IP:    " + self.user.broker_ip + "            Broker Port:    " + str(self.user.broker_port) + "           Connection Status:  " + str(self.connection_status) + "           Action Status:  " + str(self.action_status) 
        self.status_bar = Label(self.root, text=status_str, bd=1)
        self.status_bar.grid(row=20, columnspan=15)
        #self.status_bar.pack(side=BOTTOM, fill=X)
        #self.exit_button.pack(side=TOP)