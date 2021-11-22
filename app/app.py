import os 
import datetime

#from objects.user import User

'''
# Install dependencies before execution 
def satisfy_requirements(): 

    try: 
        os.system('pip install -r requirements.txt')
    except Exception as ex: 
        print(ex) 
        os.sys.exit() 

def app(): 

    you = User() 
    you.run() '''
    
    
    
# Export Exception with suggested fix / fix error 
def throw_exc(msg): 
    if msg == 'version':
        raise Exception("Must be using Python 3.8") 
    

# Main function 
def main(): 
    
    # Check Python version 
    def version_check(os_name, py_version): 
        if os_name == 'nt': 
            if py_version < 3.8 or py_version > 3.8:
                throw_exc('version')
        else: 
            if py_version < 3.8 or py_version > 3.8:
                throw_exc('version')
            
            
            #throw_exc('msg') 
            
        print(py_version)

    # Start Windows style 
    def windows_style(os_name, py_version): 
        
        print('Initializing Windows scenario')    
        
        version_check(os_name, py_version)
        
    # Start Linux style
    def linux_style(os_name, py_version):
        
        print('Initializing Linux scenario') 
        
        version_check(os_name, py_version)

    
    
    # OS evaluation
    def os_eval(): 
        os_name = os.name.replace(' ', '')
        py_version = float( str(os.sys.version_info[0]) + "." + str(os.sys.version_info[1]) ) 
        
        # OS style decider 
        if os_name == 'nt': 
            windows_style(os_name, py_version) 
        else: 
            linux_style(os_name, py_version)
     
    # Run evaluation and resulting programs      
    os_eval() 

# Listen for main 
if __name__ == '__main__': 
    
    # Run main program    
    main() 
    