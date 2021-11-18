import os 

from objects.user import User

# Install dependencies before execution 
def satisfy_requirements(): 
    try: 
        os.system('pip install -r requirements.txt')
    except Exception as ex: 
        print(ex) 
        os.sys.exit() 

def app(): 

    you = User() 
    you.run() 

if __name__ == '__main__': 
    satisfy_requirements() 
    app() 
