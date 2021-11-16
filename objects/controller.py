from objects.consumer import Consumer
from objects.producer import Producer
from objects.tester import Tester 


from tkinter import *
import os  
import threading
import time 

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

        # boolean flags 
        self.topic_started = False 
        self.msg_started = False 
        self.stream_started = False 
        self.get_started = False
        self.listen_started = False  
        self.test_started = False 

        # threads
        self.msg_thread = None 
        self.get_thread = None 

        # Controller Init 
        self.UIinit()
    
    def UIinit(self): 
        
        # REWRITE 
        # OS specific and shutdown TK 
        def close(object):
            object.root.destroy() 
        
        # Start action_set or Send action 
        def start_send_seq(object): 
            
            def message_thread(object): 
                object.user.producer = Producer(object.user)

                try: 
                    object.user.producer.send_msg() 
                    time.sleep(5)     
                    object.user.producer.close()
                    
                    #object.get_thread = threading.Thread(target=get_thread, args=([object]))
                    #object.get_thread.start() 
                    
                    object.user.status_bar.refresh_action(TRUE)
                    
                    
                except Exception as ex: 
                
                    self.user.status_bar.refresh_action(FALSE)

                    print(ex)
                    
            def get_thread(object): 
                object.user.consumer = Consumer(object.user)
                
                try: 
                    object.user.consumer.get = True 
                    object.user.consumer.get_msgs()
                    time.sleep(5)
                    
                    object.user.status_bar.refresh_action(TRUE)
                        
                except Exception as ex: 
                
                    self.user.status_bar.refresh_action(FALSE)

                    print(ex)   
            
            # Send new Topic 
            if object.topic_started: 
                object.user.producer = Producer(object.user)
            
                try: 
                    object.user.producer.make_topic() 
                except Exception as ex: 
                    print(ex)

                object.topic_started = False 
            
            # Send Message 
            elif object.msg_started: 

                object.msg_thread = threading.Thread(target=message_thread, args=([object]))
                object.msg_thread.start() 
                
                object.msg_started = False 
                
                
                #object.topic_entry.delete(0, 'end')

            # Get Messages once 
            elif object.get_started: 
                
                object.get_thread = threading.Thread(target=get_thread, args=([object]))
                object.get_thread.start()
                
                object.get_started = False 

        # REWIRE THIS 
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
            
            if self.user.producer is not None: 
                print() 
                self.user.producer.close()
                self.msg_thread.join()  
            if self.user.consumer is not None: 
                self.user.consumer.close()
                self.get_thread.join()  
                
            self.user.consumer.get = False 
            
        # WORK ON THIS 
        # Reconfigure button elements 
        def reconfig(children, conf_str): 
            
            if conf_str == 'msg': 
                print()
            
            '''def enable(children): 
                for c in children: 
                    c.configure(state='normal')
            
            def disable(children): 
                for c in children: 
                    c.configure(state='disabled')'''
          
          
        # Begin get sequence 
        def get_seq(object):

            self.get_started = True 

            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.test_button.config(state='disabled')
            self.close_button.config(state='disabled')       
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled') 
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled') 
            
            self.message_entry.config(state='disabled')
            self.start_button.config(state='normal')
            self.stop_button.config(state='normal')
            self.topic_entry.config(state='normal')

            print() 

        # WORK ON THIS 
        # Begin message sequence 
        def msg_seq(object): 
            self.msg_started = True
            
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.test_button.config(state='disabled')
            self.close_button.config(state='disabled')       
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled') 
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            self.rep_fac_entry.config(state='disabled')
            self.part_entry.config(state='disabled') 
            
            self.message_entry.config(state='normal')
            self.start_button.config(state='normal')
            self.stop_button.config(state='normal')
            self.topic_entry.config(state='normal')

            print() 

        # WORK ON THIS 
        # Begin topic sequence 
        def topic_seq(object): 
            self.topic_started = True
            
            self.host_entry.config(state='disabled')
            self.port_entry.config(state='disabled')
            self.test_button.config(state='disabled')
            self.close_button.config(state='disabled')       
            self.topic_button.config(state='disabled')
            self.topics_button.config(state='disabled') 
            self.message_button.config(state='disabled')
            self.stream_button.config(state='disabled')
            self.get_button.config(state='disabled')
            self.listen_button.config(state='disabled')
            self.message_entry.config(state='disabled')

            self.start_button.config(state='normal')
            self.stop_button.config(state='normal')
            self.topic_entry.config(state='normal')
            self.rep_fac_entry.config(state='normal')
            self.part_entry.config(state='normal')

            print() 

        # WORK ON THIS 
        # Begin topic(s) sequence
        def topics_seq(object): 
            print() 

            
        # Perform tests before accessing other KAFKA elements 
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
            
            object.topic_button = Button(object.button_frame, text="New Topic", command= lambda:topic_seq(object), width=15, state='disabled', bg = 'white')
            object.topics_button = Button(object.button_frame, text="Topics", command= lambda:msg_seq(object), width=15, state='disabled', bg = 'white')
            object.message_button = Button(object.button_frame, text="Message", command= lambda:msg_seq(object), width=15, state='disabled', bg = 'white')
            object.stream_button = Button(object.button_frame, text="Stream", command= lambda:close(object), width=15, state='disabled', bg = 'white')
            object.get_button = Button(object.button_frame, text="Get", command= lambda:get_seq(object), width=15, state='disabled', bg = 'white')
            object.listen_button = Button(object.button_frame, text="Listen", command= lambda:close(object), width=15, state='disabled', bg = 'white')
            object.test_button = Button(object.button_frame, text="Test", command= lambda:test_seq(object), width=15, state='normal', bg = 'white')
            object.start_button = Button(object.button_frame, text="Start/Send", command= lambda:start_send_seq(object), width=15, state='disabled', bg = 'white')
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
        
        