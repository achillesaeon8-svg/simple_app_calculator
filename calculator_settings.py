import tkinter as tkinter_library
import math

class FundamentalOperations(tkinter_library.Tk):
    def __init__(self, window_title='Aki Calculator', background_color='#2c3e50'):
        super().__init__()
        self.title(window_title)
        self.geometry('450x800')
        self.configure(background=background_color)
        
        self.main_display = tkinter_library.Entry(
            self,
            font = ('Arial', 24),
            justify = 'right',
            borderwidth = 10,
            background = '#ecf0f1'
        )
        self.main_display.pack(fill='x', padx=10, pady=20)
    
    def execute_safe_calculation(self):
        try:
            input_string = self.main_display.get()
            calculation_result = eval(input_string, {'__builtins__': None}, vars(math))
            
            self.main_display.delete(0, tkinter_library.END)
            self.main_display.insert(0, str(calculation_result))
            return input_string, calculation_result
        except ZeroDivisionError:
            messagebox.showerror('Math Error', 'Cannot divide by zero.')
        except Exception as error_message:
            messagebox.showerror('Error', f'invalid input: {error_message}')
            return None, None