from kafka import * 
import json 

class Producer(KafkaProducer): 
    def __init__(self, user):
        self.user = user 

        # topic info 
        self.topic_var = None 
        self.topic_name = '' 
        self.rep_fac = '' 
        self.num_par = '' 
        
        # message info 
        self.message = []


    # Describe a new message 
    def set_msg_descrip(self): 
        self.topic_name = self.user.controller.topic_entry.get()
        self.message = self.user.controller.message_entry.get('1.0', END).splitlines()
        
        self.user.controller.message_entry.delete('1.0', END)
        
    # Describe a new topic 
    def set_topic_descrip(self): 
        self.topic_name = self.user.controller.topic_entry.get()
        self.rep_fac = self.user.controller.rep_fac_entry.get() 
        self.num_par = self.user.controller.part_entry.get() 

        self.topic_var = kafka.NewTopic[(self.topic_name, self.rep_fac, self.num_par)]


    # Make a new topic   
    def make_topic(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
         
        self.set_topic_descrip() 
        self.create_topics([self.topic_var, None, True])
        self.poll(1)

    # Send a message 
    def send_msg(self): 
        super().__init__(bootstrap_servers=self.user.broker_id_str)
         
        self.set_msg_descrip()
        self.send(self.topic_name, str(self.message[0]).encode())
        
        #self.poll(1)
