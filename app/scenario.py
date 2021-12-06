import os 
import threading 

class Scenario(): 
    def __init__(self):
        
        # Native descriptors 
        self.os_name = ''
        self.style = '' 
        self.py_version = ''
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Module info 
        self.n_dep = [] 
        self.c_dep = [] 
        self.satisfied = False 
        
        # Threads 
        self.t_list = [] 
        self.check_thread = None 
        self.inst_thread = None 
        
        # You 
        self.you = None
        
        self.init() 
    
    # Init Scenario
    def init(self): 
        if self.os_name == 'nt': 
    
            self.os_eval()
            self.ind_modules() 
            
            self.check_thread = threading.Thread(target=self.dependecy_check, args=([])) 
            self.check_thread.start() 
            
            self.stop_threads()
        else: 
            self.os_eval()
            self.ind_modules() 
            
            self.check_thread = threading.Thread(target=self.dependecy_check, args=([])) 
            self.check_thread.start() 
            
            self.stop_threads()
        
    # Empty terminal contents 
    def clear_screen(self): 
        if self.os_name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')
    
    # Throw exception with suggested fix / fix error 
    def throw_exc(self, msg): 
        
        # Python version exception 
        if msg == 'version':
            
            
            
            raise Exception("Must be using Python 3.8.") 
        
        # Requirement file exception 
        elif msg == 'req':
            
            

            raise Exception("Requirements.txt must exist.")
        
        elif msg == 'Env': 
            
            
            
            raise Exception("Windows virtual environment.")

    # Stop all running threads
    def stop_threads(self): 
        for t in self.t_list:
            t.join()

    # Dependency check 
    def dependecy_check(self):
        
        # Install required dependencies 
        def inst_modules(object): 
            
            object.t_list.append(self.inst_thread)
            for n in object.n_dep: 
                os.system('pip install ' + str(n))
                
            object.satisfied = True 
            #object.user_creator() 
        
        # Compare current to needed dependencies 
        def compare_modules(object): 
            caught = 0 
            for n in self.n_dep: 
                if n not in self.c_dep: 
                    
                    continue
                    #print(n.upper() + " is needed")
                    #os.system('pip install ' + n)
                    
                else: 
                    caught += 1 
                    #print(n.upper() + " is available")
                    self.n_dep.remove(n)
            
            print(self.n_dep)
            percent = int(caught / len(self.n_dep) * 100)
            
            if percent == 100:
                object.satisfied = True 
                 
            print(str(percent) + '% of needed modules are available')
            
        # Set current dependency list 
        def set_current(object): 
            
            print('\nSetting current modules\n')
            
            if object.os_name == 'nt': 
                os.system('del ' + object.root_dir + r'\c_dep.txt')
                os.system('pip list >> ' + object.root_dir + r'\c_dep.txt')
                with open(object.root_dir + '/c_dep.txt', 'rb') as f: 
                    line = 0 
                    for req in f: 
                        if line >= 2: 
                            self.c_dep.append(req.decode().split()[0])
                        line += 1 
            
            else: 
                os.system('rm ' + object.root_dir + '/c_dep.txt')
                os.system('pip list >> ' + object.root_dir + '/c_dep.txt')
                with open(object.root_dir + '/c_dep.txt', 'rb') as f: 
                    line = 0 
                    for req in f: 
                        if line >= 2: 
                            self.c_dep.append(req.decode().split()[0] + "==" + req.decode().split()[1])
                        line += 1       
                    
            print(self.c_dep)
                    
        print('\nChecking if dependecies are satisfied ...')
        
        self.t_list.append(self.check_thread)
        set_current(self) 
        compare_modules(self)
        
        if not self.satisfied: 
            self.inst_thread = threading.Thread(target=inst_modules, args=([self])) 
            self.inst_thread.start() 
        
        '''else: 
            self.user_creator() '''
    
    # Indicate which modules are needed
    def ind_modules(self): 
        
        print('\nSetting needed modules ...')
        
        if self.os_name != 'nt': 
            try: 
                # Find needed modules 
                with open(self.root_dir + '/../requirements.txt', 'rb') as f: 
                    for req in f: 
                        self.n_dep.append(req.decode().strip())
            except Exception as ex: 
                self.throw_exc('req')
        else: 
            try: 
                # Find needed modules 
                with open(self.root_dir + r"\..\requirements.txt", 'rb') as f: 
                    for req in f: 
                        self.n_dep.append(req.decode().strip())
            except Exception as ex: 
                self.throw_exc('req')     
            
    # Check version on init 
    def os_eval(self): 
        
        self.os_name = os.name.replace(' ', '')       
        self.py_version = float( str(os.sys.version_info[0]) + "." + str(os.sys.version_info[1]) ) 
                
        if self.os_name == 'nt': 
            self.style = 'Windows'
            print('\nChecking Python Version ...')
            if self.py_version != 3.8:
                self.throw_exc('version')
            else: 
                print('\nCorrect Python version.')
        else:
            self.style = 'Linux' 
            print('\nChecking Python Version ...')
            if self.py_version != 3.8:
                self.throw_exc('version')
            else: 
                print('\nCorrect Python version.')
    
     