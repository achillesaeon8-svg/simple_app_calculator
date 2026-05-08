import tkinter as tkinter_library

class CalculatorUI:
    @staticmethod
    def draw_full_grid(app, buttons, controller, columns=4, color="#34495e"):
        for widget in app.button_frame.winfo_children():
            widget.destroy()
        for i in range(columns):
            app.button_frame.columnconfigure(i, weight=1)
        
        row_val, col_val = 0, 0
        for text in buttons:
            action = lambda x=text: controller(x)
            btn = tkinter_library.Button(
                app.button_frame, text=text, font=("Arial", 11, "bold"),
                background=color, foreground="white", relief="flat", command=action
            )
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=1, pady=1)
            col_val += 1
            if col_val >= columns:
                col_val = 0
                row_val += 1
        for r in range(row_val + 1):
            app.button_frame.rowconfigure(r, weight=1)

    @staticmethod
    def draw_basic_mode(app, controller):
        # REMOVED DEL
        keys = ['C', '(', ')', '÷', '7', '8', '9', '×', '4', '5', '6', '-', '1', '2', '3', '+', '0', '.', '=']
        CalculatorUI.draw_full_grid(app, keys, controller)

    @staticmethod
    def draw_advanced_mode(app, controller):
        keys = ['sin', 'cos', 'tan', 'log', '√', 'x²', '(', ')', '7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '-', '0', 'π', 'C', 'History', '=']
        CalculatorUI.draw_full_grid(app, keys, controller, columns=5, color="#8e44ad")

    @staticmethod
    def draw_unit_mode(app, controller):
        # REMOVED BACK
        keys = ['kg→g', 'g→kg', 'm→cm', 'cm→m', '7', '8', '9', 'C', '4', '5', '6', 'km→m', '1', '2', '3', 'm→km', '0', 'lb→kg', 'kg→lb']
        CalculatorUI.draw_full_grid(app, keys, controller, columns=4, color="#2980b9")

    @staticmethod
    def draw_currency_mode(app, controller):
        # REMOVED BACK
        keys = ['$→₱', '₱→$', 'KRW→₱', '₱→KRW', '7', '8', '9', 'C', '4', '5', '6', '¥→₱', '1', '2', '3', '₱→¥', '0', '€→₱', '₱→€']
        CalculatorUI.draw_full_grid(app, keys, controller, columns=4, color="#d35400")

    @staticmethod
    def draw_time_mode(app, controller):
        # REMOVED BACK
        keys = ['hr→min', 'min→hr', 'min→sec', 'sec→min', '7', '8', '9', 'C', '4', '5', '6', 'day→hr', '1', '2', '3', 'hr→day', '0', '.']
        CalculatorUI.draw_full_grid(app, keys, controller, columns=4, color="#27ae60")