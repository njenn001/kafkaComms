from objects.consumer import Consumer 

class Tester(): 
    def __init__(self, user):
        
        self.user = user        
        
    # run test sequence
    def run(self): 
        
        self.user.set_broker_info()
        self.user.consumer = Consumer(self.user)
        
        try:
            self.user.consumer.get_topics() 
            self.user.controller.host_entry.config(state='disabled')
            self.user.controller.port_entry.config(state='disabled')
            self.user.controller.test_button.config(state='disabled')
                        
            self.user.controller.topic_button.config(state='normal')    
            self.user.controller.topics_button.config(state='normal') 
            self.user.controller.message_button.config(state='normal')
            self.user.controller.stream_button.config(state='normal')
            self.user.controller.get_button.config(state='normal')
            self.user.controller.listen_button.config(state='normal')
            self.user.controller.start_button.config(state='normal')
            
            suc = True
            self.user.status_bar.refresh_status(suc)
                    
                                   
        except Exception as ex: 
            fail = False 
            self.user.status_bar.refresh_status(fail)
        
        