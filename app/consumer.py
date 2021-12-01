from kafka import KafkaConsumer
from kafka import * 
class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 
         
        # topic info 
        self.topic_list = [] 
        self.topic_name = '' 

        # message info 
        self.messages = [] 
        
        # boolean 
        self.get = False 
        self.listen = False 
        
        # thread 
        self.show_thread = None 
        
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
