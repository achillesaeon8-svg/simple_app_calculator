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
  def draw_basic_mode(app, controller):
    keys = ['C', '(', ')', '÷', '7', '8', '9', '×', '4', '5', '6', '-', '1', '2', '3', '+', '0', '.', '=']
    CalculatorUI.draw_full_grid(app, keys, controller)
  
  @staticmethod
  def draw_advanced_mode(app, controller):
    keys = ['sin', 'cos', 'tan', 'log', '√', 'x²', '(', ')', '7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '-', '0', 'π', 'C', 'History', '=']
    CalculatorUI.draw_full_grid(app, keys, controller, columns=5, color="#8e44ad")

  @staticmethod
  def draw_unit_mode(app, controller):
    keys = ['kg→g', 'g→kg', 'm→cm', 'cm→m', '7', '8', '9', 'C', '4', '5', '6', 'km→m', '1', '2', '3', 'm→km', '0', 'lb→kg', 'kg→lb']
    CalculatorUI.draw_full_grid(app, keys, controller, columns=4, color="#2980b9")

  @staticmethod
  def draw_currency_mode(app, controller):
    keys = ['$→₱', '₱→$', 'KRW→₱', '₱→KRW', '7', '8', '9', 'C', '4', '5', '6', '¥→₱', '1', '2', '3', '₱→¥', '0', '€→₱', '₱→€']
    CalculatorUI.draw_full_grid(app, keys, controller, columns=4, color="#d35400")

  @staticmethod
  def draw_time_mode(app, controller):
    keys = ['hr→min', 'min→hr', 'min→sec', 'sec→min', '7', '8', '9', 'C', '4', '5', '6', 'day→hr', '1', '2', '3', 'hr→day', '0', '.']
    CalculatorUI.draw_full_grid(app, keys, controller, columns=4, color="#27ae60")