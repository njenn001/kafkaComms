import os
from kafka import KafkaConsumer
from kafka import * 

import threading 
import keyboard 

class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 
        
        # server info 
        self.bootstrap_server = '' 
         
        # topic info 
        self.topic_list = [] 
        self.topic_name = '' 

        # message info 
        self.messages = [] 
        
        # boolean 
        self.get = False 
        self.listen = False 
        
        # thread info 
        self.threads = [] 
        self.show_thread = None  
        self.key_thread = None 
        
    # GET / SET / ADD thread 
    def get_threads(self): 
        return self.threads
    def set_threads(self, threads):
        self.threads = threads 
    def add_thread(self, thread):
        self.threads.append(thread) 
        
    # GET / SET key thread 
    def get_key_thread(self): 
        return self.key_thread
    def set_key_thread(self, thread): 
        self.key_thread = thread
        
    # Kill self
    def kill(self): 
        self.close() 
        os.sys.exit()
        
        
    # Stop all threads 
    def stop_threads(self):
        try: 
            for t in self.get_threads():
                if not t.is_alive(): 
                    t.join() 
        except Exception as ex: 
            self.stop_threads()
        
    
    # Decode existing args
    def decode_args(self): 
        
        print(self.args[0][0])
        self.bootstrap_server = self.args[0][0]
        self.topic_name = self.args[1][0]
    
    # Capture incoming Strict args 
    def strict(self, args): 
        
        # Catch input key 
        def catch_key(object):
            object.add_thread(object.get_key_thread())
            t = True
            while t:
                if keyboard.is_pressed('q'):
                    print('Killing')
                    object.stop_threads() 
                    object.kill() 
                    t = False
                
                
        self.set_key_thread(threading.Thread(target=catch_key, args=([self])))
        self.key_thread.start()
        
        
        self.args = args 
        self.decode_args() 
        super().__init__(self.topic_name, bootstrap_servers=self.bootstrap_server, group_id=None, auto_offset_reset='earliest', enable_auto_commit=False)

        try:
            for m in self: 
                self.messages.append(m.value.decode())
                print(m.value.decode())                 
                          
        except Exception as ex: 
            print(ex) 

    
    # Describe a new topic 
    def set_topic_descrip(self): 
        self.topic_name = self.user.controller.topic_entry.get()


    def get_msgs(self): 
        self.set_topic_descrip()
        super().__init__(self.topic_name, bootstrap_servers=self.user.broker_id_str, group_id=None, auto_offset_reset='earliest', enable_auto_commit=False)
    
        try:
            for m in self: 
                self.messages.append(m.value.decode())
                print(m.value.decode())                 
                
                self.user.view.show_text(self.messages)
                if not self.get: 
                    break 
                
                          
        except Exception as ex: 
            print(ex) 
        
       
    def get_topics(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
        self.topic_list = self.topics()
        
        if not self.topic_list: 
            raise RuntimeError()
        else: 
            self.user.view.text_lines.config(state='normal')
            self.user.view.show_text(self.topic_list)
            self.user.view.text_lines.config(state='disabled')
