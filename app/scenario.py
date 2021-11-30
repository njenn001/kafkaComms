import os 

class Scenario(): 
    def __init__(self, os_name, py_version):
        
        # Native descriptors 
        self.os_name = os_name
        self.py_version = py_version
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Module info 
        self.n_dep = [] 
        self.c_dep = [] 
        self.satisfied = False 
        
        # Threads 
        self.check_thread = None 
        self.inst_thread = None 
        
        self.clear_screen()
        
        self.init() 
    
    # Init Scenario
    def init(self): 
        self.version_check()
        self.ind_modules() 
        self.dependecy_check() 
    
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
  
    # Dependency check 
    def dependecy_check(self):
        
        # Compare current to needed dependencies 
        def compare_modules(object): 
            caught = 0 
            for n in self.n_dep: 
                if n not in self.c_dep: 
                    
                    print(n.upper() + " is needed")
                    #os.system('pip install ' + n)
                    
                else: 
                    caught += 1 
                    #print(n.upper() + " is available")
                    self.n_dep.remove(n)
            
            print(self.n_dep)
            percent = int(caught / len(self.n_dep) * 100)
            print(str(percent) + '% of needed modules are available')
            
        # Set current dependency list 
        def set_current(object): 
            
            print('\nSetting current modules')
            if object.os_name == 'nt': 
                os.system('del ' + object.root_dir + '\c_dep.txt')
            else: 
                os.system('rm ' + object.root_dir + '/c_dep.txt')
                        
            os.system('pip list >> ' + object.root_dir + '/c_dep.txt')
            with open(object.root_dir + '/c_dep.txt', 'rb') as f: 
                line = 0 
                for req in f: 
                    if line >= 2: 
                        self.c_dep.append(req.decode().split()[0] + "==" + req.decode().split()[1])
                    line += 1 
                    
        print('\nChecking if dependecies are satisfied ...')
        set_current(self) 
        compare_modules(self)
    
    # Indicate which modules are needed
    def ind_modules(self): 
        
        print('\nSetting needed modules ...')
        
        try: 
                
            with open('app/requirements.txt', 'rb') as f: 
                for req in f: 
                    self.n_dep.append(req.decode().strip())
        except Exception as ex: 
            self.throw_exc('req')
                
    # Check version on init 
    def version_check(self): 
        
        print('\nChecking Python Version ...')
        
        if self.os_name == 'nt': 
            if self.py_version != 3.8:
                self.throw_exc('version')
            else: 
                print('\nCorrect Python version.')
        else: 
            if self.py_version != 3.8:
                self.throw_exc('version')
            else: 
                print('\nCorrect Python version.')
    
     