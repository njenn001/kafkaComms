from kafka import * 
from tkinter import * 

class Consumer(KafkaConsumer): 
    def __init__(self, user):
        self.user = user 
        # server string 
        self.bootstrap_str = [] 
         
        # topic info 
        self.topic_list = [] 
        self.topic = '' 
       
    def get_topics(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
        self.topic_list = self.topics()
        
        '''self.user.view.text_lines = Text(self.user.view.view_frame, width = 50, height = 15, wrap = NONE,
                 xscrollcommand = self.user.view.scroll_bar_horizontal.set,
                 yscrollcommand = self.user.view.scroll_bar_horizontal.set)'''
        
        for i in self.topic_list: 
            print(i)
            self.user.view.text_lines.insert(END, str(i) + "\n")

        if not self.topic_list: 
            raise RuntimeError()
        
        #for t in self.topic_list: 
            
        
        print(self.topic_list)