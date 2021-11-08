from kafka import KafkaProducer

class Producer(KafkaProducer): 
    def __init__(self):
        self.IP = '192.168.0.101:9092'
        self.topic = '' 
        self.message = ''
        
        super().__init__(bootstrap_servers = self.IP) 
        
        
        
        #self.send('foobar', b'some_message_bytes')