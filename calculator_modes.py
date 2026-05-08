from calculator_settings import FundamentalOperations
import tkinter as tkinter_library

class CalculatorUI(FundamentalOperations):
  @staticmethod
  def draw_full_grid(app, buttons, controller, columns=4, color='#34495e')
    for widget in app.button_frame.winfo_children():
      widget.destroy()
    for i in range(columns):
      app.button_frame.columnconfigure(i, weight=1)

    row_value, column_value = 0, 0
    for text in buttons:
      action = lambda x=text: controller(x)
      tkinter_button = tkinter_library.Button(
        app.button_frame, text=text, font=('Arial', 11, 'bold'),
        background=color, foreground='white', relief='flat', command=action
      )
      tkinter_button.grid(row=row_value, column=column_value, sticky='nsew', padx=1, pady=1)
      column_value += 1
      if column_value >= columns:
        column_value = 0
        row_value += 1
    for r in range(row_value + 1):
      app.button_frame.rowconfigure(r, weight=1)

  @staticmethod
  def