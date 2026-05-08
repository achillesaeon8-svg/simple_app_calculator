import tkinter as tkinter_library

class InputHistory:
  def __init__(self):
    self.logs = []
  
  def add_entry(self, equation, result):
    self.logs.append(f'{equation} = {result}')

  def show_history_window(self):
    window = tkinter_library.Toplevel()
    window.title('Calculation Logs')
    window.geometry('300x400')
    text_area = tkinter_library.Text(window, font='Arial', 12)
    text_area.pack(expand=True. fill='both')

    if not self.logs:
      text_area.insert('1.0', 'No history yet')
    for entry in self.logs:
      text_area.insert('end', entry + '\n')
    text_area.config(state='disabled')