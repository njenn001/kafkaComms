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
        
        '''self.user.view.text_lines = Text(self.user.view.view_frame, width = 50, height = 15, wrap = NONE,
                 xscrollcommand = self.user.view.scroll_bar_horizontal.set,
                 yscrollcommand = self.user.view.scroll_bar_horizontal.set)'''
        
        
            
        if not self.topic_list: 
            raise RuntimeError()
        else: 
            self.user.view.show_text(self.topic_list)

        
        
        #for t in self.topic_list: 
            
        
        print(self.topic_list)