from producer import Producer
from tkinter import *

import os  
import math

class View(Frame): 

    def __init__(self, root, user):
        self.user = user
        super().__init__()
        self.root = root
        
        # frame 
        self.view_frame = None 

        # entinties 
        self.scroll_bar_horizontal = None
        self.scroll_bar_vertical = None 
        self.text_lines = None   
        
        # Controller Init 
        self.UIinit()
        
    def clear_lines(self): 
        self.text_lines.delete('1.0', END)
        
    def show_text(self, arr):
        self.text_lines.config(state='normal')
        self.clear_lines() 
        for l in arr: 
          self.text_lines.insert(END, str(l) + "\n") 
        self.text_lines.config(state='disabled') 
        
    def UIinit(self): 
        
        # Initialize text lines
       
        # Initialize view frame 
        def init_view_frames(object):  
            object.view_frame = Frame(object.root)
            object.view_frame.grid(row=1, column=5, padx=(50, 50), columnspan=20)
            
            object.scroll_bar_horizontal = Scrollbar(object.view_frame, orient = 'horizontal')
            object.scroll_bar_vertical = Scrollbar(object.view_frame)
            
            object.text_lines = Text(object.view_frame, width = 50, height = 15, wrap = NONE,
                 xscrollcommand = object.scroll_bar_horizontal.set,
                 yscrollcommand = object.scroll_bar_horizontal.set, state='disabled')
    
            # insert some text into the text widget
            '''for i in range(20):
                t.insert(END,"this is some text\n")'''
            
            object.scroll_bar_horizontal.pack(side = BOTTOM, fill = X)
            object.scroll_bar_vertical.pack(side = RIGHT, fill = Y)
            object.text_lines.pack(side=TOP, fill=X)
 
        
        init_view_frames(self)
        