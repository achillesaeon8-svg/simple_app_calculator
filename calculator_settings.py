import tkinter as tkiner_library
from tkinter import messagebox
import math

class FundamentalOperations(tkinter_library.TK):
    def __init__(self, window_ title='ShielPhor Calculator', background_color='#2c3e50'):
        super().__init__()
        self.title(window_title)
        self.geometry('350x550')
        self.configure(background=background_color)
        
        self.main_display = tkinter_library.Entry(self,
        font = ('Arial', 24),
        justify = 'right',
        bd = 10
        background = '#ecf0f1'
    )
