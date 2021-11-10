from objects.consumer import Consumer 

class Tester(): 
    def __init__(self, user):
        
        self.user = user        
        
    # run test sequence
    def run(self): 
        
        
        self.user.set_broker_info()
        self.user.consumer = Consumer(self.user)
        
        self.user.consumer.get_topics() 
        
        pass