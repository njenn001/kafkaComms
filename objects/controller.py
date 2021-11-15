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
        self.rep_fac_title = None
        self.part_title = None

        # entries 
        self.host_entry = None
        self.port_entry = None 
        self.message_entry = None 
        self.topic_entry = None 
        self.rep_fac_entry = None
        self.part_entry = None

        # Controller Init 
        self.UIinit()
    
    def UIinit(self): 
        
        # REWRITE 
        # OS specific and shutdown TK 
        def close(object):
            object._running = False
            os.sys.exit(0)
            
        # End address:port designation 
        def stop_seq(object): 
            
            self.host_entry.delete(0, END)
            self.port_entry.delete(0, END)
            self.topic_entry.delete(0, END)
            # Figure out how to empty this self.message_entry.delete(0, END)
            self.rep_fac_entry.delete(0, END)
            self.part_entry.delete(0, END)
                        
            self.host_entry.config(state='normal')
            self.port_entry.config(state='normal')
            self.topic_entry.config(state='disabled')
            # Figure out how to empty this self.message_entry.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled')
            
            
            self.stop_button.config(state='disabled')
            self.start_button.config(state='disabled')
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled')
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            
            self.test_button.config(state='normal')
            self.close_button.config(state='normal')
            

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
            
            self.user.producer = Producer(self.user) 
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
            object.rep_fac_title = Label(object.input_frame, text="REP. FACTOR")
            object.part_title = Label(object.input_frame, text="NUM. PARTITIONS")
            
            
            object.host_entry = Entry(object.input_frame, foreground='black')
            object.port_entry = Entry(object.input_frame, foreground='black')
            object.topic_entry = Entry(object.input_frame, foreground='black', state='disabled')
            object.message_entry = Text(object.input_frame, foreground='black', width=15, height=5, state='disabled')
            object.rep_fac_entry = Entry(object.input_frame, foreground='black', state='disabled')
            object.part_entry = Entry(object.input_frame, foreground='black', state='disabled')
            
            object.host_title.grid(row=0, column=0)
            object.host_entry.grid(row=0, column=1, columnspan=14)
            object.port_title.grid(row=1, column=0)
            object.port_entry.grid(row=1, column=1)
            object.topic_title.grid(row=2, column=0)
            object.topic_entry.grid(row=2, column=1)
            object.message_title.grid(row=3, column=0)
            object.message_entry.grid(row=3, column=1)
            object.rep_fac_title.grid(row=4, column=0)
            object.rep_fac_entry.grid(row=4, column=1)
            object.part_title.grid(row=5, column=0)
            object.part_entry.grid(row=5, column=1)
                        
            
        # Initialize button frame 
        def init_button_frames(object):
            
            # Change button color on hover 
            def on_enter(e): 
                if e.widget.cget('state') == "normal":
                    if e.widget.cget("text") == 'Test':
                        object.test_button['background'] = 'light green'
                    elif e.widget.cget('text') == "Start/Send":
                        object.start_button['background'] = 'light green'
                    elif e.widget.cget("text") == 'Stop' :
                        object.stop_button['background'] = 'red'
                    elif e.widget.cget("text") == 'Close':
                        object.close_button['background'] = 'red'
                    elif e.widget.cget('text') == 'New Topic': 
                        object.topic_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Topics': 
                        object.topics_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Message': 
                        object.message_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Stream': 
                        object.stream_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Get': 
                        object.get_button['background'] = 'yellow'
                    elif e.widget.cget('text') == 'Listen': 
                        object.listen_button['background'] = 'yellow'
                        
                    
            # Change button color back 
            def on_leave(e): 
                if e.widget.cget("text") == 'Test':
                    object.test_button['background'] = 'white'
                elif e.widget.cget('text') == "Start/Send":
                    object.start_button['background'] = 'white'
                elif e.widget.cget("text") == 'Stop':
                    object.stop_button['background'] = 'white'
                elif e.widget.cget("text") == 'Close':
                    object.close_button['background'] = 'white'
                elif e.widget.cget('text') == 'New Topic': 
                    object.topic_button['background'] = 'white'
                elif e.widget.cget('text') == 'Topics': 
                    object.topics_button['background'] = 'white'
                elif e.widget.cget('text') == 'Message': 
                    object.message_button['background'] = 'white'
                elif e.widget.cget('text') == 'Stream': 
                    object.stream_button['background'] = 'white'
                elif e.widget.cget('text') == 'Get': 
                    object.get_button['background'] = 'white'
                elif e.widget.cget('text') == 'Listen': 
                    object.listen_button['background'] = 'white'
            
            object.button_frame = Frame(object.root, borderwidth=2, border=1)
            object.button_frame.grid(row=1, column=0, pady=50, padx=(50,25))
            
            object.topic_button = Button(object.button_frame, text="New Topic", command= lambda:msg_seq(object), width=15, state='disabled', bg = 'white')
            object.topics_button = Button(object.button_frame, text="Topics", command= lambda:msg_seq(object), width=15, state='disabled', bg = 'white')
            object.message_button = Button(object.button_frame, text="Message", command= lambda:msg_seq(object), width=15, state='disabled', bg = 'white')
            object.stream_button = Button(object.button_frame, text="Stream", command= lambda:close(object), width=15, state='disabled', bg = 'white')
            object.get_button = Button(object.button_frame, text="Get", command= lambda:close(object), width=15, state='disabled', bg = 'white')
            object.listen_button = Button(object.button_frame, text="Listen", command= lambda:close(object), width=15, state='disabled', bg = 'white')
            object.test_button = Button(object.button_frame, text="Test", command= lambda:test_seq(object), width=15, state='normal', bg = 'white')
            object.start_button = Button(object.button_frame, text="Start/Send", command= lambda:close(object), width=15, state='disabled', bg = 'white')
            object.stop_button = Button(object.button_frame, text="Stop", command= lambda:stop_seq(object), width=15, state='disabled', bg = 'white')
            object.close_button = Button(object.button_frame, text="Close", command= lambda:close(object), width=15, state='normal', bg = 'white')
            
            object.topic_button.bind("<Enter>", on_enter)
            object.topic_button.bind("<Leave>", on_leave)
            
            object.topics_button.bind("<Enter>", on_enter)
            object.topics_button.bind("<Leave>", on_leave)
            
            object.message_button.bind("<Enter>", on_enter)
            object.message_button.bind("<Leave>", on_leave)
            
            object.stream_button.bind("<Enter>", on_enter)
            object.stream_button.bind("<Leave>", on_leave)
            
            object.get_button.bind("<Enter>", on_enter)
            object.get_button.bind("<Leave>", on_leave)
           
            object.listen_button.bind("<Enter>", on_enter)
            object.listen_button.bind("<Leave>", on_leave)
            
            ## ## ## ## ## 
            
            object.test_button.bind("<Enter>", on_enter)
            object.test_button.bind("<Leave>", on_leave)
            
            object.start_button.bind("<Enter>", on_enter)
            object.start_button.bind("<Leave>", on_leave)
            
            object.stop_button.bind("<Enter>", on_enter)
            object.stop_button.bind("<Leave>", on_leave)
            
            object.close_button.bind("<Enter>", on_enter)
            object.close_button.bind("<Leave>", on_leave)
            
            
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
        
        