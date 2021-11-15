from kafka import * 
from tkinter import * 

class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 
         
        # topic info 
        self.topic_list = [] 
        self.topic = '' 
       
    def get_topics(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
        self.topic_list = self.topics()
        
        if not self.topic_list: 
            raise RuntimeError()
        else: 
            self.user.view.show_text(self.topic_list)
