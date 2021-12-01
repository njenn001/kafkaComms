import os 
import argparse 

from scenario import Scenario
from user import User 

# Main function 
def main(): 
            
    # Decode available arguments 
    def args_decoder(args): 
        
        if not args: 
            print('none')
        elif args.setup: 
            print('Starting setup sequence ...')
                    
            # Run evaluation and resulting programs      
            scene = Scenario() 
            
        elif args.run: 
            print('Starting native sequence ...')
            
            # Run native sequence 
            you = User()
            
    # Init command parser 
    def init_parser(): 
        parser = argparse.ArgumentParser(
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description='Kafka Communication Center CLI',
                    epilog='For more help, type main.py -h')
            
        '''
        Specify different interface modes
        - setup 
        - test 
        - run 
        - producer 
        - consumer 
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
    