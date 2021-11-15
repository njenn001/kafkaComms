from kafka import * 
from tkinter import * 

class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 
         
        # topic info 
        self.topic_list = [] 
        self.topic_name = '' 

        # message info 
        self.messages = [] 

    def get_msgs(self): 
        super().__init__(self.topic_name, bootstrap_servers=self.user.broker_id_str)
    

        try: 
            for m in self: 
                print(m) 
        except Exception as ex: 
            print(ex) 
        """
        for msg in self:
            print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))"""
       
    def get_topics(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
        self.topic_list = self.topics()
        
        if not self.topic_list: 
            raise RuntimeError()
        else: 
            self.user.view.text_lines.config(state='normal')
            self.user.view.show_text(self.topic_list)
            self.user.view.text_lines.config(state='disabled')
