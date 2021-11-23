import os 

from scenario import Scenario

# Main function 
def main(): 
   
    # Start Windows style 
    def windows_style(os_name, py_version):    
        
        scene = Scenario(os_name, py_version)
                
    # Start Linux style
    def linux_style(os_name, py_version):
        
        scene = Scenario(os_name, py_version)
            
    
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
    