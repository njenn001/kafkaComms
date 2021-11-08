from tkinter import * 
from win32api import *

from objects.controller import Controller 
from objects.view import View
 
import os 

class User(): 
    def __init__(self):
        self.ip = '' 
        self.date_time = '' 
        
        self.resolution = [] 
        self.res_str = ''

        self.root = None
        self.root_init() 
        self.app = None 
        self.app_2 = None 

    def get_resolution(self): 
        w = int(GetSystemMetrics(0) * .6 )
        h = int(GetSystemMetrics(1) / 2  )

        size_str = str(w) + 'x' + str(h) 

        self.resolution = [(w/3), (h/2)]
        self.res_str = size_str

    def root_init(self): 
        
        self.get_resolution()

        self.root=Tk()
        self.root.attributes("-topmost", True)
        self.root.title('Kafka Communications')
        self.root.geometry(self.res_str)

        self.open_controller() 

        self.root.mainloop() 

    def open_controller(self): 
        
        #self.app_2 = View(self.root, self) 
        self.app = Controller(self.root, self)
        
        os.system('clear')