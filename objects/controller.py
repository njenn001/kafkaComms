from objects.producer import Producer
from objects.tester import Tester 


from tkinter import *
import os  

class Controller(Frame): 

    def __init__(self, root, user):
        self.user = user
        super().__init__()
        self.root = root
        self.tester = None 
        
        
        # status 
        self.status_bar = None

        # frames 
        self.button_frame = None
        self.input_frame = None
    
        # buttons 
        self.topic_button = None 
        self.topics_button = None 
        self.message_button = None
        self.stream_button = None
        self.get_button = None 
        self.listen_button = None
        self.test_button = None
        self.start_button = None 
        self.stop_button = None 
        self.close_button = None 

        # titles 
        self.host_title = None 
        self.port_title = None 
        self.message_title = None 
        self.topic_title = None 

        # entries 
        self.host_entry = None
        self.port_entry = None 
        self.message_entry = None 
        self.topic_entry = None 

        # Controller Init 
        self.UIinit()
    
    def UIinit(self): 
        
        # REWRITE 
        # OS specific and shutdown TK 
        def close(object):
            object._running = False
            os.sys.exit(0)

        def reconfig(children, conf_str): 
            
            if conf_str == 'msg': 
                print()
            
            '''def enable(children): 
                for c in children: 
                    c.configure(state='normal')
            
            def disable(children): 
                for c in children: 
                    c.configure(state='disabled')'''
          
          
        
        # Begin Message Sequence 
        def msg_seq(object): 
            #reconfig(self.input_frame.winfo_children(), 'msg')
            print() 
            
        # performing tests before accessing other KAFKA elements 
        def test_seq(object): 
            
            object.tester = Tester(object.user)
            object.tester.run() 
            
            pass
        
        # Initialize input frame  
        def init_input_frames(object): 
                        
            object.input_frame = Frame(object.root)
            object.input_frame.grid(row=1, column=1, rowspan=15)
            
            object.host_title = Label(object.input_frame, text="HOST IP")
            object.port_title = Label(object.input_frame, text="PORT")
            object.topic_title = Label(object.input_frame, text="TOPIC")
            object.message_title = Label(object.input_frame, text="MESSAGE")
            
            
            object.host_entry = Entry(object.input_frame, foreground='grey')
            object.port_entry = Entry(object.input_frame, foreground='grey')
            object.topic_entry = Entry(object.input_frame, foreground='grey')
            object.message_entry = Entry(object.input_frame, foreground='grey')
            
            object.host_title.grid(row=0, column=0)
            object.host_entry.grid(row=0, column=1, columnspan=14)
            object.port_title.grid(row=1, column=0)
            object.port_entry.grid(row=1, column=1)
            object.topic_title.grid(row=2, column=0)
            object.topic_entry.grid(row=2, column=1)
            object.message_title.grid(row=3, column=0)
            object.message_entry.grid(row=3, column=1)
                        
            
        # Initialize button frame 
        def init_button_frames(object):
            object.button_frame = Frame(object.root, borderwidth=2, border=1)
            object.button_frame.grid(row=1, column=0, pady=50, padx=(50,25))
            
            object.topic_button = Button(object.button_frame, text="New Topic", command= lambda:msg_seq(object), width=15, state='disabled')
            object.topics_button = Button(object.button_frame, text="Topics", command= lambda:msg_seq(object), width=15, state='disabled')
            object.message_button = Button(object.button_frame, text="Message", command= lambda:msg_seq(object), width=15, state='disabled')
            object.stream_button = Button(object.button_frame, text="Stream", command= lambda:close(object), width=15, state='disabled')
            object.get_button = Button(object.button_frame, text="Get", command= lambda:close(object), width=15, state='disabled')
            object.listen_button = Button(object.button_frame, text="Listen", command= lambda:close(object), width=15, state='disabled')
            object.test_button = Button(object.button_frame, text="Test", command= lambda:test_seq(object), width=15, state='normal')
            object.start_button = Button(object.button_frame, text="Start/Send", command= lambda:close(object), width=15, state='disabled')
            object.stop_button = Button(object.button_frame, text="Stop", command= lambda:close(object), width=15, state='disabled')
            object.close_button = Button(object.button_frame, text="Close", command= lambda:close(object), width=15, state='normal')
            
            object.topic_button.grid(row=0, column=0)
            object.topics_button.grid(row=1, column=0)
            object.message_button.grid(row=2, column=0)
            object.stream_button.grid(row=3, column=0)
            object.get_button.grid(row=4, column=0)            
            object.listen_button.grid(row=5, column=0)
            object.test_button.grid(row=6, column=0)
            object.start_button.grid(row=7, column=0)
            object.stop_button.grid(row=8, column=0)
            object.close_button.grid(row=9, column=0)
            
        
        init_button_frames(self)
        init_input_frames(self)
        
        