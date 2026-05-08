import tkinter as tkinter_library
import math

class FundamentalOperations(tkinter_library.Tk):
    def __init__(self, window_title='Aki Calculator', background_color='#2c3e50'):
        super().__init__()
        self.title(window_title)
        self.geometry('450x800')
        self.configure(background=background_color)
        
        self.main_display = tkinter_library.Entry(
            self, font = ('Arial', 32), justify = 'right', borderwidth = 10, background = '#ecf0f1', relief='flat'
        )
        self.main_display.pack(fill='x', padx=15, pady=25)

        self.button_frame = tkinter_library.Frame(self, background=background_color)
        self.button_frame.pack(expand=True, fill='both', padx=5, pady=5)

        self.protocol('WM_DELETE_WINDOW', self.exit_sequence)
    
    def execute_safe_calculation(self):
        raw_value = self.main_display.get()
        try:
            expression = raw_value.replace('×', '*').replace('÷', '/')
            expression = expression.replace('√', 'math.sqrt').replace('π', 'math.pi')

            result = eval(expression, {'__builtins__': None}, {'math': math})
            formatted_result = f'{result:.8f}'.rsplit('0').rsplit('0') if insistance(result, float) else str(result)

            self.main_display.delete(0, 'end')
            self.main_display.insert(0, formatted_result)
            return raw_value, formatted_result
        
        except ZeroDivisionError:
            self