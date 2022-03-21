import argparse 

# Main function 
def main(): 
          
    # Decode available arguments 
    def args_decoder(args): 
        
        if not args: 
            
            print('none')
        
        elif args.setup: 
            from scenario import Scenario
            print('Starting setup sequence ...')
                    
            # Run evaluation and resulting programs 
            scene = Scenario() 
            scene.inst_thread.start() 
            
            #time.sleep(5) 
            scene.stop_threads()             
            
        elif args.run: 
            
            from user import User 
            print('Starting native sequence ...')
            
            # Run native sequence 
            you = User()

            try: 
                
                you.run() 
            except Exception as ex: 
                
                you.throw_exec('gui')
            
        elif args.produce: 
            from user import User 
            from producer import Producer 
            print('Begin message production')
                
            # Run Strict User 
            you = User() 
            try: 
                p_info = [args.bss, args.top, args.m]
                
                you.producer = Producer(you) 
                you.producer.strict(p_info)
            except Exception as ex: 
                you.throw_exec('p_args')
            
        elif args.consume: 
            from user import User 
            from consumer import Consumer 
            print('Begin message consumption')
                
            # Run Strict Scenario 
            you = User() 
            try:
                c_info = [args.bss, args.top]
            
                you.consumer = Consumer(you) 
                you.consumer.strict(c_info)
            except Exception as ex: 
                you.throw_exec('c_args')
                
        elif args.clean: 
            from scenario import Scenario
            
            scene = Scenario() 
            scene.clean_sequence() 
                
    # Init command parser 
    def init_parser(): 
        parser = argparse.ArgumentParser(
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description='Kafka Communication Center CLI')
            
        '''
        Specify different interface modes
        - setup 
        - test 
        - run 
        - produce 
        - consume 
        - clean 
        '''
        mode_group = parser.add_mutually_exclusive_group(required=True)

        # Setup Mode 
        mode_group.add_argument('-s', '--setup', action='store_true',
                                help='Initialize environment setups.')

        # Test Mode
        mode_group.add_argument('-t', '--test', action='store_true',
                                help='Test broker connectivity.')

        # Run Mode
        mode_group.add_argument('-r', '--run', action='store_true',
                                help='Start communication center GUI.')
        
        # Produce Mode 
        mode_group.add_argument('-p', '--produce', action='store_true',
                                help='Quick message production.')
        
        # Consume Mode 
        mode_group.add_argument('-co', '--consume', action='store_true',
                                help='Quick message consumption.')
        
        # Consume Mode 
        mode_group.add_argument('-cl', '--clean', action='store_true',
                                help='Clean project directories.')
        
        
        '''
        Specify different flags
        - bootstrap server(s) : port(s)
        - topic 
        - msg
        - rep fac 
        - par num
        - loop  
        '''
        
        # Bootstrap server flag 
        parser.add_argument(
        '--bss', '--boostrap_servers', type=str, help="Specify broker IP address(es) and port number(s).", nargs='+')
        
        # Topic flag 
        parser.add_argument(
        '--top', '--topic', type=str, help="Specify cluster topic.", nargs='+')
        
        # Msg flag 
        parser.add_argument(
        '--m', '--msg', type=str, help="Write desired message.", nargs='+')
                 
        # Rep fac flag 
        parser.add_argument(
        '--rep', '--replication-factor', type=str, help="Specify replication factor.", nargs='+')
        
        # Part num flag 
        parser.add_argument(
        '--par', '--partition-number', type=str, help="Specify number of partitions.", nargs='+')
        
        # Loop flag 
        parser.add_argument(
        '--l', '--loop', type=bool, help="Set production/consumption looping.", nargs='+')
        
        return parser 
            
    # Set and capture command line arguments     
    parser = init_parser()
    args, unknown = parser.parse_known_args() 

    # Decode available arguments 
    args_decoder(args) 

# Listen for main 
if __name__ == '__main__': 
    
    # Run main program    
    main() 
    