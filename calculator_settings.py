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
            self.update_display('Error: Division by Zero')
            return 'Error', 'Div0'
        except ValueError:
            self.update_display('Error: Math Domain')
            return 'Error', 'Domain'
        except Exception:
            self.update_display('Error: Invalid Input')
            return 'Error', 'Invalid'
        
    def update_display(self, text):
        self.main_display.delete(0, 'end')
        self.main_display.insert(0, text)

    def exit_sequence(self):
        for widget in self.winfo_children():
            widget.destroy()
        bye_label = tkinter_library.Label(self, text='Thank you for using my calculator! BYEEE', font=('Arial', 24, 'bold'), background='#2c3e50', foreground='white')

        bye_label.pack(expand=True)
        self.fade_exit(bye_label)

    def fade_exit(self, label, step=0):
        colors = ['#ffffff', '#dfe6e9', '#b2bec3', '#95a5a6', '#636e72', '#2c3e50']
        if step < len(colors):
            label.config(foreground=colors[step])
            self.after(200, lambda: self.fade_exit(label, step + 1))
        else:
            self.destroy()